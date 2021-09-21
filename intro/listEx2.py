# List Introduction Example
# This example is seeking to provide a more interactive experience
# to experimenting with lists. By providing menu options, we can build 
# a system that allows te user to choose what to examine and see the 
# intended results
# Mr. J
# UCC 
# September 21, 2021

print ("")
print ("")
print("Welcome to Fun with Lists")
print ("")
print("Here are your Options...")
print ("")
print("1. Update")
print("2. Find a Subset")
print("3. Append")
print("4. Delete")
print ("")
print ("")

city_list = ['Saskatoon', 'Toronto', 'Edmonton', 'Halifax', 'Montreal', 'Fredericton']

print("Current Data:")
print(city_list)
print ("")
print ("")

option = int(input("What would you like to do? \n"))

if option == 1:
    print("You have chosen to do an update...")
    position = int(input("What position would you like to update (choose between 0 to 5!!!) \n"))
    newinfo = input("What is the new data? \n")
    city_list[position] = newinfo
    print(city_list)
    print ("")
    print ("")

elif option == 2:
    print ("You have chosen to find a subset...")
    # print(city_list[1:3])
    print ("")
    print ("")

elif option == 3:
    print ("You have chosen to do an append...")
    # city_list.append("St. John's")
    # city_list.append("Charlottetown")
    # city_list.append("Yellowknife")
    print(city_list)
    print ("")
    print ("")

elif option == 4:
    print ("You have chosen to delete...")
    # del city_list[3]
    # print ("performing deletion on position 3")
    print (city_list)
    print ("")
    print ("")

else:
    print ("This is not a valid choice")
    print ("Have a great day anyway!")
    print ("")
    print ("")


# This is a way to gracefully exit the program
input("Press ENTER to quit the program...")

