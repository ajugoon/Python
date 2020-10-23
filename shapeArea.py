# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Mr. Jugoon
# Upper Canada College

# Put down some options for the user to choose from...

# Here is the menu choice options
print("1. Circle")
print("2. Square")
print("3. Triangle")
print(" ")
print("Choose one of the options above")

shapeoption = int(input("Please choose your shape...  \n"))

# Here is where we decide to calculate the area of a circle
if shapeoption == 1:
    print("We are calculating the area of a Circle")
    mydata = float(input("What is the radius? \n"))
    print("The area of a Circle is: " + str(3.14 * mydata * mydata) + " sq. units")


else:
    print ("This is not a valid choice")
    print ("Please enter a valid shape choice.")


# This is a way to gracefully exit the program
input("Press ENTER to quit the program...")
