import csv,os
# Step 1: Define the mapping of product IDs to names
product_mapping = {
    "PD1001": "Face Serum",
    "PD1002": "Gaming Mouse",
    "PD1003": "Power Bank",
    "PD1004": "Scented Candles",
    "PD1005": "Wireless Earbuds",
    "PD1006": "Yoga Mat",
    "PD1007": "Hydro Bottle",
    "PD1008": "Running Shoes",
    "PD1009": "Cotton Sheets",
    "PD1010": "Comfort Pillow"
}

# Step 2: Read the input CSV file
input_filename = 'data/2.1.2.csv'
output_filename = 'data_processed/2.1.2.csv'

with open(input_filename, 'r') as input_file, open(output_filename, 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write the header
    writer.writerow(["Date","Product Name","Current Stock Level","Optimal Stock Quantity"])
    # Process each row in the input file
    next(reader)  # Skip the header
    for row in reader:
        col1, col2,col3,col4= row
        product_name = product_mapping.get(col2, col2)  # Fallback to product_id if not found
        writer.writerow([col1,product_name,col3,col4])

