# This is a program that determines the average of 5 numerical grades

# This variable stores my total. It has been initalized to '0' to make it an integer
total = 0 # always an integer

# This variable stores my average. It has been initalized to '0.0' to make it a float
average = 0.0 # always a float

for num in range (0, 5): 

    mynum = int(input("Type in your number \n")) # input from keyboard
    print("Your number is: " + str(mynum)) # shows the number to the user
    total = total + mynum # keeps updating "total" by adding "mynum"

average = total / 5

print("The average is " + str(average))
