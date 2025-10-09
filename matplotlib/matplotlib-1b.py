# line_plot.py

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot
plt.plot(x, y, marker='o', color='b', linestyle='-', linewidth=2)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add labels for each point
for i in range(len(x)):
    plt.text(x[i], y[i] + 0.3, f"({x[i]}, {y[i]})", ha='center', color='blue')

# Show the plot
plt.show()
