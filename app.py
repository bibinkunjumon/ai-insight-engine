from flask import Flask, render_template, request
import pandas as pd
from generate_data import process_tables
from analytical_fns import draw_bargraph
app = Flask(__name__)

all_tables_data = {}

@app.route('/') #Home Page
def dashboard():
    global all_tables_data
    all_tables_data = process_tables()
    print(all_tables_data.get("1.1.1"))
    return render_template('home/home_page.html',all_tables_data = all_tables_data)

@app.route('/analytics', endpoint='AnalyticsDashboard') # Analytics Dashboard viewall
def analytics_dashboard():
    global all_tables_data
    draw_bargraph(all_tables_data,"1.1.1","Product Names","Total Searches",'Bar Graph - Total Searches per Product')
    print(all_tables_data.get("1.1.2"))
    draw_bargraph(all_tables_data,"1.1.2","Product Names","Search to Purchase Ratio",'Bar Graph - High Search Low Purchase Products')
    return render_template('analytics_dashboard/analytic_page.html',all_tables_data=all_tables_data)

@app.route('/inventory', endpoint='InventoryDashboard') # Inventory Dashboard  viewall
def inventory_dashboard():
    global all_tables_data
    return render_template('inventory_optimization/inventory_page.html',all_tables_data=all_tables_data)

@app.route('/salesboost', endpoint='SalesBoostDashboard') # SalesBoost Dashboard  viewall
def analytics_dashboard():
    global all_tables_data
    return render_template('sales_booster_features/sales_boost_page.html',all_tables_data=all_tables_data)

# if __name__ == '__main__':
#     app.run(debug=True)
