# This is a program that adds 5 names to an empty list

# This is where we create the "empty" list
names_list = [] #no contents at the current time 

for position in range (0, 5): 

    myname = str(input("Please enter a name: \n")) # input from keyboard

    print("The name you entered is: " + myname) # shows the name to the user

    # names_list[position] = myname # keeps updating the list
    
    names_list.append(str(myname)) # keeps updating the list

    print(names_list)
