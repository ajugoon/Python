import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file
data = pd.read_csv("sales.csv")
print("✅ Data loaded successfully!\n")
print(data)

# Step 2: Perform some analysis
average_sales = data["Sales"].mean()
print(f"\n📊 💜 The average monthly sales: {average_sales:.2f}\n")

# Step 3: Plot a bar chart
plt.figure(figsize=(8, 5))
plt.bar(data["Month"], data["Sales"], color='lightgreen', edgecolor='black')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
