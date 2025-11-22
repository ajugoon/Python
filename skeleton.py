# Skeleton program for Designing Data Summative
# Y10 Design Coding

# This program assumes three .csv files exist for the illustrative purposes

# Import the packages needed to process data (pandas and matplotlib)
import pandas as pd
import matplotlib.pyplot as plt

# Function definitions will be defined at the top of the python 
def runMenu():

	# Present the User with a Menu to explore options
	print ("What data would you like to explore today?")
	print ("")
	print ("1. Homelessness data")
	print ("2. Climate data")
	print ("3. Wellbeing data")

	choice = int(input("What data would you like to explore today?\n"))

	validChoice = False

	while(not validChoice):

		global data1, data2, data3, col1, col2, pie1, pie2

		# Read CSV files that you wish to analyse based on the menu chase
		if choice == 1:

			validChoice = True

			# Use Pandas to open up each of the datafiles based on user selection
			data1 = pd.read_csv("datafile1.csv")
			print("✅ All data about Homelessness loaded successfully!\n")
			print(data1)

			# Convert each column in the dataset into a list
			columns_as_lists = {col: data1[col].tolist() for col in data1.columns}

			# print them out for visual verification
			for col, lst in columns_as_lists.items():
				print(f"{col}: {lst}")

			# Place each column into its own list
			col1 = data1["Month"].tolist()
			col2 = data1["Sales"].tolist()

			print (col1)
			print (col2)

			# Step 2: Perform some analysis
			average_sales = data1["Sales"].mean()
			print(f"\n📊 💜 The average monthly sales: {average_sales:.2f}\n")
			plotBarGraph(col1, col2)


		elif choice == 2:

			validChoice = True

			data2 = pd.read_csv("datafile2.csv")
			print("✅ All data about Climate Change loaded successfully!\n")
			print(data2)

			# Convert each column in the dataset into a list
			columns_as_lists = {col: data2[col].tolist() for col in data2.columns}

			# Print them out for visual verification
			for col, lst in columns_as_lists.items():
				print(f"{col}: {lst}")

			# Place each column into its own list
			col1 = data2["Month"].tolist()
			col2 = data2["Sales"].tolist()

			print (col1)
			print (col2)

			# Step 2: Perform some analysis
			average_sales = data2["Sales"].mean()
			print(f"\n📊 💜 The average monthly sales: {average_sales:.2f}\n")
			plotLineGraph(col1, col2)


		elif choice == 3:
			data3 = pd.read_csv("datafile3.csv")
			print("✅ All data about Wellbeing loaded successfully!\n")
			print(data3)
			validChoice = True


			# Convert each column in the dataset into a list
			columns_as_lists = {col: data3[col].tolist() for col in data3.columns}

			# Print them out for visual verification
			for col, lst in columns_as_lists.items():
				print(f"{col}: {lst}")

			# Place each column into its own list
			col1 = data3["Time"].tolist()
			col2 = data3["Activity"].tolist()
			
			print (col1)
			print (col2)

			plotPieChart(col1, col2)


		else:
			print ("Please make a valid selection")

def plotBarGraph(xValues, yValues):

	# Plot a bar chart
	plt.figure(figsize=(8, 5))
	plt.bar(xValues, yValues, color='lightgreen', edgecolor='black')
	plt.title("Monthly Sales")
	plt.xlabel("Month")
	plt.ylabel("Sales")
	plt.xticks(rotation=45)
	plt.tight_layout()
	plt.show()

def plotLineGraph(xValues, yValues):

	# Create a line plot
	plt.plot(xValues, yValues, marker='o', color='b', linestyle='-', linewidth=2)
	plt.title("Monthly Sales")
	plt.xlabel("Month")
	plt.ylabel("Sales")

	# Add labels for each point
	for i in range(len(xValues)):
		plt.text(xValues[i], yValues[i] + 0.3, f"({xValues[i]}, {yValues[i]})", ha='center', color='blue')

	# Show the plot
	plt.show()

def plotPieChart(pcSizes, pcLabels):

	# Create the pie chart: 'pcSizes' are percentages, and 'pcLabels' are labels
	plt.pie(pcSizes, labels=pcLabels, autopct='%1.1f%%')

	# Add a title
	plt.title("How My Time is Spent")

	# Show the plot
	plt.show()



#########################################################################################

### This is the main program ###

runMenu()

