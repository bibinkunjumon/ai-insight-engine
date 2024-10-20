from flask import Flask, render_template, request,jsonify
import pandas as pd
import os
# from generate_data import process_tables
# from analytical_fns import draw_bargraph
from utils import generate_tables_graphs

app = Flask(__name__)

all_tables_data = {}
headrow_tables_data = {}
data_refresh = True


from time import sleep
@app.route('/update_tables_graphs', methods=['POST'])
def update_tables_graphs():
    global all_tables_data,headrow_tables_data,data_refresh
    all_tables_data,headrow_tables_data,data_refresh = generate_tables_graphs()  
    sleep(10) # for user feeling
    return jsonify({"message": "Data updated successfully! Table is Upto Date & Graphs redrawn"})

@app.route('/') #Home Page
def dashboard():
    global data_refresh,headrow_tables_data,all_tables_data
    if data_refresh: #Only when first start automatic refresh
        all_tables_data,headrow_tables_data,data_refresh = generate_tables_graphs()
    return render_template('home/home_page.html',all_tables_data = headrow_tables_data)

@app.route('/analytics', endpoint='AnalyticsDashboard') # Analytics Dashboard viewall
def analytics_dashboard():
    global headrow_tables_data
    return render_template('analytics_dashboard/analytic_page.html',all_tables_data=headrow_tables_data)

@app.route('/analytics/section/<section_number>', endpoint='analytics_section') # Analytics Dashboard viewall
def analytics_section(section_number):
    global all_tables_data
    # draw_bargraph(all_tables_data,"1.1.1","Product Names","Total Searches",'Bar Graph - Total Searches per Product',f'{section_number}fulldata')
    image_path = f'static/images/{section_number}fulldata.png'
    image_exists = os.path.exists(image_path)
    return render_template(f'analytics_dashboard/ad_section/{section_number}.html',all_tables_data = all_tables_data, image_exists=image_exists)

@app.route('/inventory', endpoint='InventoryDashboard') # Inventory Dashboard  viewall
def inventory_dashboard():
    global all_tables_data
    return render_template('inventory_optimization/inventory_page.html',all_tables_data=all_tables_data)

@app.route('/salesboost', endpoint='SalesBoostDashboard') # SalesBoost Dashboard  viewall
def salesboost_dashboard():
    global all_tables_data
    return render_template('sales_booster_features/sales_boost_page.html',all_tables_data=all_tables_data)

if __name__ == '__main__':
    app.run(debug=True)
