# Loop Example
# This program asks for 4 integers and calculates the average value

print ("This program will ask for 4 numbers and calculate the average...")

# Here we use the FOR Loop

print ("Please enter the numbers at the prompt")

number = 0
total = 0
for x in range(0, 4):
	number = int(input("enter a number..."))
	total = total + number
	print ("Number is: " + str(number))
	print ("Total is: " + str(total))
	print ("****************")

print ("Average is: " + str(total/4))





