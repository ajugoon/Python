# bar_chart.py

import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

# Create a bar chart

colours = ["red", "blue", "green"]
plt.bar(categories, values, color=colours)
plt.title("Simple Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")

# Show the plot
plt.show()
