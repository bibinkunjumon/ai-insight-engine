# import matplotlib.pyplot as plt

# # Step 1: Prepare your data
# data = {
#     'product_id': ['PD1004', 'PD1007', 'PD1005', 'PD1010', 'PD1003'],
#     'total_searches': [1149, 1043, 984, 983, 824]
# }

# def draw_bargraph(all_tables_data):
#     for row in all_tables_data["1.1.1"]['data']:
#         for item in row:
#             item

#     for file_key, content in all_tables_data.items():
#             print(f"\nFile: {file_key}")
#             print("Columns:", content['columns'])
#             print("Data:")
#             for row in content['data']:
#                 print(row)
#     column_names=[]
#     chart={}
#     for column in all_tables_data['1.1.1']['columns']:
#          column_names.append(column)    
#     for data in all_tables_data['1.1.1']['data']:
#         for value in data:
#             chart [column_names.pop()]:value

# # Step 2: Create the bar graph
# plt.figure(figsize=(10, 6))  # Set the size of the figure
# plt.bar(data['product_id'], data['total_searches'], color='skyblue')

# # Step 3: Add titles and labels
# plt.title('Total Searches per Product ID')
# plt.xlabel('Product ID')
# plt.ylabel('Total Searches')

# # Step 4: Show the plot
# plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
# plt.tight_layout()  # Adjust layout to make room for labels
# plt.show()

