# bar_chart.py

import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

# Create a bar chart
plt.bar(categories, values, color='g')
plt.title("Simple Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")

# Show the plot
plt.show()
