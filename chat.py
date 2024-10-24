import os
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import trim_messages
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


def create_model():
    try:
        api_key = os.environ.get("OPENAI_API_KEY")
        os.environ["OPENAI_API_KEY"] = api_key
        model = ChatOpenAI(model="gpt-3.5-turbo")
        return model  # Return the model instance
    except Exception as e:
        print(f"Error creating model: {e}")
        raise


def call_model(state: MessagesState, model, prompt, trimmer, config):
    try:
        chain = prompt | model
        trimmed_messages = trimmer.invoke(state["messages"])
        response = chain.invoke(
            {"messages": trimmed_messages},
            config,
        )
        return {"messages": [response]}
    except Exception as e:
        print(f"Error during model invocation: {e}")
        return {"messages": ["An error occurred while processing your request."]}


def initialise_variables(thread_id, table_data):
    try:
        model = create_model()
        trimmer = trim_messages(
            max_tokens=2000,
            strategy="last",
            token_counter=model,
            include_system=True,
            allow_partial=False,
            start_on="human",
        )

        State = MessagesState
        workflow = StateGraph(state_schema=State)
        config = {"configurable": {"thread_id": thread_id}}
        system_prompt = (
            "Act as an expert data analyst and provide recommendations and answers based on the provided table data. "
            "You can ask clarifying questions about the data if needed. "
            "Please analyze the data, identify trends and patterns, and provide actionable insights and recommendations. "
            "You can use natural language to communicate and provide explanations for your findings and recommendations. "
            "Table Data is as follows:\n" + str(table_data)
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    system_prompt
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        workflow.add_edge(START, "model")
        workflow.add_node(
            "model", lambda state: call_model(state, model, prompt, trimmer, config)
        )
        memory = MemorySaver()
        app = workflow.compile(checkpointer=memory)
        print('#'*40,prompt)
        return app, config  # Return the app and config
    except Exception as e:
        print(f"Error initializing variables: {e}")
        raise
