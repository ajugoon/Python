# bar_chart.py

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Ask user for the CSV file name
filename = input("Enter the CSV file name (including .csv): ")

try:
    # Step 2: Read the CSV file
    data = pd.read_csv(filename)
    print("File loaded successfully!")
    print("Here are the columns in your file:\n", list(data.columns))

    # Step 3: Ask which columns to plot
    x_col = input("Enter the column name for the X-axis: ")
    y_col = input("Enter the column name for the Y-axis: ")


    # Step 4: Plot the bar graph
    plt.figure(figsize=(8, 5))
    plt.bar(data[x_col], data[y_col], color='skyblue', edgecolor='black')
    plt.title(f"{y_col} by {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: File not found. Please check the file name and try again.")
except KeyError:
    print("Error: One or both of the specified columns were not found in the file.")
except Exception as e:
    print("An unexpected error occurred:", e)

