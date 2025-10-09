# scatter_plot.py

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a scatter plot
plt.scatter(x, y, color='r', s=100)
plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add labels next to each point
for i in range(len(x)):
    plt.text(x[i] + 0.1, y[i], f"{y[i]}", fontsize=9, color='black')

# Show the plot
plt.show()
