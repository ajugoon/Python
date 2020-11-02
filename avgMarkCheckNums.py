# This is a program that determines the average of 5 numerical grades
# Author: Mr. Jugoon
# UCC October 30th, 2020

# This variable stores my total. It has been initalized to '0' to make it an integer
total = 0 # always an integer

# This variable stores my average. It has been initalized to '0.0' to make it a float
average = 0.0 # always a float

amountOfNums = 0 # keeps track of the amount of numbers we have submitted

while amountOfNums < 5: # remember that the first number is the "0th" number

    data = str(input("Please enter a number: \n")) # input from keyboard

    if (data.isnumeric() == False):
        print("The data is not numeric and/or negative value entered")
        continue # causes the loop to re-test its condition

    else: # it means the data is numeric, convert from string to int

        mynum = int(data)
     
        if (mynum < 0 or mynum > 100):
            print("Number has to be between 0 to 100 inclusive")
            continue # causes the loop to re-test its condition

    print("Your number is: " + str(mynum)) # shows the number to the user
    amountOfNums += 1 # increment by 1
    total = total + mynum # keeps updating "total" by adding "mynum"
    print("Your total is: " + str(total)) # shows the total to the user
    print("The amount of numbers is: " + str(amountOfNums)) # shows the number of actual numbers to the user

average = total / 5

print("The average is " + str(average))
