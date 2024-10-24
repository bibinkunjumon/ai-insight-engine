from generate_data import process_tables
from analytical_fns import draw_bargraph
import csv

def generate_tables_graphs():
    # global all_tables_data,headrow_tables_data,data_refresh
    all_tables_data = process_tables("fulldata")
    headrow_tables_data = process_tables("headrow")

    draw_bargraph(headrow_tables_data,"1.1.1","Product Names","Total Searches",'Bar Graph - Total Searches per Product',"1.1.1")
    draw_bargraph(headrow_tables_data,"1.1.2","Product Names","Search to Purchase Ratio",'Bar Graph - High Search Low Purchase Products','1.1.2')
    draw_bargraph(headrow_tables_data,"1.1.3","Product Names","Total Searches",'Bar Graph - Low Search Products','1.1.3')
    draw_bargraph(headrow_tables_data,"1.2.1","Product Names","Cart Additions",'Bar Graph - Products Left in Cart',"1.2.1")
    draw_bargraph(headrow_tables_data,"1.3.1","Product Names","Search to Purchase Ratio",'Bar Graph - Most Purchased Products','1.3.1')
    draw_bargraph(headrow_tables_data,"1.3.2","Product Names","Search to Purchase Ratio",'Bar Graph - Least Purchased Products','1.3.2')
    #Section Wise Graphs with full data
    draw_bargraph(all_tables_data,"1.1.1","Product Names","Total Searches",'Bar Graph - Total Searches per Product','1.1.1fulldata')

    data_refresh = False
    return all_tables_data,headrow_tables_data,data_refresh

# Sample topics
topics = {
    "1.1": "Product Search Analytics- Analytics Dashboard",
    "1.2": "Cart Abandonment Analytics- Analytics Dashboard",
    "1.3": "Purchase Analytics- Analytics Dashboard",
    "1.4": "Customer Behavior Analytics- Analytics Dashboard",
    "2.1": "Stock Recommendations- Inventory Optimization",
    "2.2": "Procurement Suggestions- Inventory Optimization",
    "2.3": "Pricing Strategy Analysis- Inventory Optimization",
    "3.1": "Automated Offers and Discounts- Sales Booster Features",
    "3.2": "Cross-Selling and Upselling- Sales Booster Features"
}

def read_table_data(filepath):
    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        table_data = "\n".join([",".join(row) for row in data])
        return table_data
    
topic_files_dict ={
    "1.1":['1.1.1','1.1.2','1.1.3'],
    "1.2":['1.2.1','1.2.2'],
    "1.3":['1.3.1','1.3.2'],
    "1.4":['1.4.1','1.4.2'],
    "2.1":['2.1.1','2.1.2','2.1.3'],
    "2.2":['2.2.1','2.2.2','2.2.3'],
    "2.3":['2.3.1'],
    "3.1":['3.1.1','3.1.2','3.1.3'],
    '3.2':['3.2.1','3.2.2']
}