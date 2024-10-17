from flask import Flask, render_template, request
import pandas as pd
from generate_data import process_tables

app = Flask(__name__)

all_tables_data = {}

@app.route('/') #Home Page
def dashboard():
    global all_tables_data
    all_tables_data = process_tables()
    return render_template('home/home_page.html',all_tables_data = all_tables_data)

@app.route('/analytics', endpoint='AnalyticsDashboard') # Analytics Dashboard viewall
def analytics_dashboard():
    global all_tables_data
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
