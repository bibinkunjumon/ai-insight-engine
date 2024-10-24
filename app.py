from flask import Flask, render_template, request, jsonify
import requests
import os
from utils import generate_tables_graphs, topics,read_table_data,topic_files_dict
from langchain_core.messages import HumanMessage
from chat import initialise_variables

app = Flask(__name__)

all_tables_data = {}
headrow_tables_data = {}
data_refresh = True
# Declare chatapp as a global variable
thread_id = "as123"
chatapp, config = initialise_variables(thread_id,"")

from time import sleep


@app.route("/update_tables_graphs", methods=["POST"])
def update_tables_graphs():
    global all_tables_data, headrow_tables_data, data_refresh
    all_tables_data, headrow_tables_data, data_refresh = generate_tables_graphs()
    sleep(5)  # for user feeling
    return jsonify(
        {"message": "Data updated successfully! Table is Upto Date & Graphs redrawn"}
    )


@app.route("/")  # Home Page
def dashboard():
    global data_refresh, headrow_tables_data, all_tables_data
    if data_refresh:  # Only when first start automatic refresh
        update_tables_graphs()
        # all_tables_data,headrow_tables_data,data_refresh = generate_tables_graphs()
    return render_template("home/home_page.html", all_tables_data=headrow_tables_data)


# Analytics Dashboard viewall
@app.route("/analytics", endpoint="AnalyticsDashboard")
def analytics_dashboard():
    global headrow_tables_data
    return render_template(
        "analytics_dashboard/analytic_page.html", all_tables_data=headrow_tables_data
    )


# Inventory Dashboard  viewall
@app.route("/inventory", endpoint="InventoryDashboard")
def inventory_dashboard():
    global headrow_tables_data
    return render_template(
        "inventory_optimization/inventory_page.html",
        all_tables_data=headrow_tables_data,
    )


# SalesBoost Dashboard  viewall
@app.route("/salesboost", endpoint="SalesBoostDashboard")
def salesboost_dashboard():
    global headrow_tables_data
    return render_template(
        "sales_booster_features/sales_boost_page.html",
        all_tables_data=headrow_tables_data,
    )


# Sectionwise detailed analytics
@app.route(
    "/analytics/section/<section_number>", endpoint="analytics_section"
)  # Analytics Dashboard viewall
def analytics_section(section_number):
    global all_tables_data
    image_path = f"static/images/{section_number}fulldata.png"
    image_exists = os.path.exists(image_path)
    return render_template(
        f"detailed_sections/{section_number}.html",
        all_tables_data=all_tables_data,
        image_exists=image_exists,
    )


# Chat Interface
@app.route("/chatpage", endpoint="ChatPage")
def index():
    return render_template("chat/chatpage.html", topics=topics)


last_selected_topic = None

@app.route("/chat", methods=["POST"])
def chat():
    global chatapp, config, thread_id, last_selected_topic
    user_message = request.json.get("message")
    selected_topic = request.json.get("topic")
    if not user_message:
        return jsonify({"response": "Please enter a message."})
    table_data = ""
    if selected_topic != last_selected_topic and selected_topic is not None:
        if selected_topic in topic_files_dict:
            if topic_files_dict[selected_topic]:
                for item in topic_files_dict[selected_topic]:
                    table_data += "\n" + read_table_data(f'data_processed/{item}.csv')
        # Invoke the function to initialize variables
        chatapp, config = initialise_variables(thread_id,table_data) 
        last_selected_topic = selected_topic  

    input_messages = [HumanMessage(user_message)]
    try:
        output = chatapp.invoke({"messages": input_messages}, config, timeout=20)
    except requests.exceptions.Timeout:
        return jsonify({"response": "The request timed out. Please try again later."})
    except Exception as e:
        return jsonify({"response": f"An error occurred: {str(e)}"})

    # Extract the response message
    response_message = output["messages"][-1].content

    return jsonify({"response": response_message})


if __name__ == "__main__":
    app.run(debug=True)
