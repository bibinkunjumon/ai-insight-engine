import os
import pandas as pd

def read_csv(file_path):
    """Reads a CSV file and returns its columns and the first few rows of data."""
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)
        table_columns = data.columns.tolist()
        # table_data = data.values.tolist()  # Convert to list of lists
        table_data = data.head().values.tolist()  # Convert to list of lists
        return table_columns, table_data

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None, None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

def process_tables():
    # Directory containing the CSV files
    data_directory = "data"
    # Dictionary to store data from all CSV files
    all_data = {}
    # List all CSV files in the directory
    csv_files = [f for f in os.listdir(data_directory) if f.endswith('.csv')]

    # Loop through each CSV file and read it
    for csv_file in csv_files:
        file_path = os.path.join(data_directory, csv_file)  # Construct full file path
        columns, data = read_csv(file_path)  
        
        # Store the columns and data in the dictionary
        if columns is not None and data is not None:
            file_key = os.path.splitext(csv_file)[0]  # Use filename without extension as key
            all_data[file_key] = {
                'columns': columns,
                'data': data
            }
    return all_data

    # for file_key, content in all_data.items():
    #     print(f"\nFile: {file_key}")
    #     print("Columns:", content['columns'])
    #     print("Data:")
    #     for row in content['data']:
    #         print(row)