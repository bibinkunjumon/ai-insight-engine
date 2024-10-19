import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI environments
import matplotlib.pyplot as plt
import numpy as np

def draw_bargraph(all_tables_data,analysis_code,xlabel,ylabel,graphlabel):
    # Extract column names and data
    # columns = all_tables_data[analysis_code]['columns']
    data_rows = all_tables_data[analysis_code]['data']
    
    # Initialize lists for x and y values
    x_labels = []
    y_values = []

    # Iterate over the data rows to populate x and y values
    for data in data_rows:
        x_labels.append(data[0])  # Product ID
        y_values.append(data[1])   # Total Searches

    # Set up the bar colors
    colors = ['skyblue', 'lightgreen'] * (len(y_values) // 2 + 1)  # Alternate colors

    # Plotting the bar graph
    plt.figure(figsize=(12, 7))
    bar_positions = np.arange(len(x_labels))  # The x locations for the groups

    plt.bar(bar_positions, y_values, color=colors[:len(y_values)])
    plt.title(graphlabel, fontsize=18, fontweight='bold')
    plt.xlabel(xlabel, fontsize=16,fontweight='bold')
    plt.ylabel(ylabel, fontsize=16,fontweight='bold')
    plt.xticks(bar_positions, x_labels, rotation=45, fontsize=12)
    
    # Adding grid lines for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

 # Adding value labels on top of the bars
    for i, value in enumerate(y_values):
        # Adjust the y position to be above the bar
        plt.text(i, value + max(y_values) * 0.02, str(value), ha='center', fontsize=10, fontweight='bold')
    print(y_values)
    # Save the graph as an image
    plt.tight_layout()
    plt.subplots_adjust(top=0.9, bottom=0.2)  # Adjust margins
    plt.savefig(f'static/images/{analysis_code}.png')  # Save the image
    print(f"{analysis_code} - Image Writed")
    plt.close()  # Close the plot to free up memory
