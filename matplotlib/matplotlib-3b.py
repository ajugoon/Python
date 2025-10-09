# bar_chart.py

import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

# Create a bar chart
plt.bar(categories, values, color='g')
plt.title("Simple Bar Chart")
plt.grid(True)
plt.xlabel("Category")
plt.ylabel("Value")

# Add value labels above each bar
for i, value in enumerate(values):
    plt.text(i, value + 0.2, str(value), ha='center', color='black')

# Show the plot
plt.show()
