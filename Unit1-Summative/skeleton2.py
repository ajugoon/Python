# Skeleton program for Designing Data Summative
# This program demonstrates the use of "filters" that are built into Pandas
# Y10 Design Coding

# This program assumes the use of nyse.csv to exist in order to work

# Import the packages needed to process data (pandas and matplotlib)
import pandas as pd
import matplotlib.pyplot as plt

# Function definitions will be defined at the top of the python 
def runMenu():

	# Present the User with a Menu to explore options
	print ("What data would you like to explore today?")
	print ("")
	print ("1. Display NYSE data in the terminal")
	print ("2. Display NYSE data as a graph")

	choice = int(input("What data would you like to explore today?\n"))

	validChoice = False

	while(not validChoice):

		global data1, data2, data3, col1, col2, column1, lower, upper

		# Read CSV files that you wish to analyse based on the menu chase
		if choice == 1:

			validChoice = True

			# Use Pandas to open up each of the datafiles based on user selection
			data1 = pd.read_csv("nyse.csv")
			
			print("File loaded successfully!")
			print("Here are the columns in your file:\n", list(data1.columns))

			viewCol1 = input("What is the first column are you interested in viewing? Hint: Ticker\n")
			viewCol2 = input("What is second column are you interested in viewing? Hint: Industry_Tag\n")
			searchCol = input("What column are you filtering by? Hint: Close\n")
			lower = float(input("What is your lower parameter? Hint: 6\n"))
			upper = float(input("What is your upper paramter? Hint 100\n"))

			# this filter will only display results on the terminal
			filter1(viewCol1, viewCol2, searchCol, lower, upper)

		elif choice == 2:

			validChoice = True

			# Use Pandas to open up each of the datafiles based on user selection
			data1 = pd.read_csv("nyse.csv")
			
			print("File loaded successfully!")
			print("Here are the columns in your file:\n", list(data1.columns))

			column1 = input("What is the first column are you interested in? Hint: Ticker\n")
			print ("This will be the x-axis (independent variable)")
			column2 = input("What is the second column are you interested in? Hint: Volume\n")
			print ("This will be the y-axis (dependent variable)")
			lower = float(input("What is your lower parameter? Hint: 10000\n"))
			upper = float(input("What is your upper paramter? Hint 100000\n"))

			# this filter will display results on the terminal and display a bar graph
			filter2(column1, column2, lower, upper)

		else:
			print ("Please make a valid selection")


# Filtering data between two values - option 1
def filter1(first_column, second_column, search_column, value1, value2):

	filtered = data1[(data1[search_column] >= value1) & (data1[search_column] <= value2)]
	result = filtered[[first_column, second_column]]
	print(result)


# Filtering data between two values - option 2

def filter2(column1, column2, min1, max1):

	# column1 = x-axis
	# column2 = y-axis
	# min1 = lower limit of values being searched
	# max1 = upper limit of values being searched

	result = data1[data1[column2].between(min1, max1)][[column1, column2]]
	print(result)

	col1 = result[column1].tolist()
	col2 = result[column2].tolist()
	plotBarGraph(col1, col2)


'''

# Filtering data between two dates
def filter3(value1, value2):

	data1["date"] = pd.to_datetime(data1["date"])
	filtered = data1[data1["date"].between("2024-01-01", "2024-12-31")]
	print(filtered)


# Filtering data between two dates
def filter4(value1, value2):

	filtered = data1[data1["col1"].between(10, 20) & data1["col2"].between(50, 100)]
	print(filtered)

def filter5(value1, value2):

	filtered = data1[data1["age"] > 18]
	print(filtered)

def filter6(value1, value2):

	filtered = data1[(data1["age"] > 18) & (data1["city"] == "Toronto")]
	print(filtered)

'''

def plotBarGraph(xValues, yValues):

	# Plot a bar chart
	plt.figure(figsize=(8, 5))
	plt.bar(xValues, yValues, color='lightgreen', edgecolor='black')
	plt.title("Volume of Stocks Traded")
	plt.xlabel("Company")
	plt.ylabel("Volume")
	plt.xticks(rotation=45)
	plt.tight_layout()
	plt.show()


#########################################################################################

### This is the main program ###

runMenu()

