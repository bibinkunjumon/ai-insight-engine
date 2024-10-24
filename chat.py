import getpass
import os
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import trim_messages
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def create_model():
    try:
        api_key = os.environ.get('OPENAI_API_KEY')
        os.environ["OPENAI_API_KEY"] = api_key
        model = ChatOpenAI(model="gpt-3.5-turbo")
        return model  # Return the model instance
    except Exception as e:
        print(f"Error creating model: {e}")
        raise  # Re-raise the exception for further handling

def call_model(state: MessagesState, model, prompt, trimmer, config):
    try:
        chain = prompt | model
        trimmed_messages = trimmer.invoke(state["messages"])
        response = chain.invoke(
            {"messages": trimmed_messages}, config,
        )
        return {"messages": [response]}
    except Exception as e:
        print(f"Error during model invocation: {e}")
        return {"messages": ["An error occurred while processing your request."]}

def initialise_variables(thread_id):
    try:
        model = create_model()
        trimmer = trim_messages(
            max_tokens=65,
            strategy="last",
            token_counter=model,
            include_system=True,
            allow_partial=False,
            start_on="human",
        )

        State = MessagesState
        workflow = StateGraph(state_schema=State)
        config = {"configurable": {"thread_id": thread_id}}
        prompt = ChatPromptTemplate.from_messages(  
            [
                (
                    "system",
                    "You are a helpful assistant. Answer all questions to the best of your ability.",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        workflow.add_edge(START, "model")
        workflow.add_node("model", lambda state: call_model(state, model, prompt, trimmer, config))  # Pass necessary parameters
        memory = MemorySaver()
        app = workflow.compile(checkpointer=memory)
        return app, config  # Return the app and config
    except Exception as e:
        print(f"Error initializing variables: {e}")
        raise  # Re-raise the exception for further handling

# Step 4
# try:
#     app, config = initialise_variables()  # Initialize variables and get app
#     query = "Hi! I'm Bob."
#     input_messages = [HumanMessage(query)]
#     output = app.invoke({"messages": input_messages}, config)
#     output["messages"][-1].pretty_print()  # Output contains all messages in state
# except Exception as e:
#     print(f"An error occurred during execution: {e}")