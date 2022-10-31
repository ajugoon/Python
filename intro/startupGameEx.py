Splash = """
  # copy and paste your ASCII art here #
"""
print (Splash)

def question1():
  
    print ("Question #1: What colour of jellybean did you choose?")
    print ("\u001b[33m Question #1: What colour of jellybean choose?\u001b[0m")

    print("")
    print("1. Purple")
    print("2. Blue")
    print("3. Red")
    print("")
  
    response1 = int(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == 1:
        print("Please Try Again")
        print("")
        question1()
   
  
    elif response1 == 2:
        print("Great Job!")
        print("")
        print("Now we will move on to question number 2!")
        print("")
        question2()
    
  
    elif response1 == 3:
        print ("Please Try Again")
        print ("")
        question1()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question1()


def question2():
  
    print ("Question #2: What colour of skittles candy did you choose?")
    print ("\u001b[33m Question #2: What colour of skittles candy did you choose?\u001b[0m")

    print("")
    print("1. Purple")
    print("2. Blue")
    print("3. Red")
    print("")
  
    response2 = int(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response2 == 1:
        print("Please Try Again")
        print("")
        question2()
   
  
    elif response2 == 2:
        print("Great Job!")
        print("")
        print("Now we will move on to question number 3!")
        # call question 3 here...
        print("")
  
    elif response2 == 3:
        print ("Please Try Again")
        print ("")
        question2()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question2()


validChoice = False
# global start

while (validChoice == False):
    #global validChoice
    #global start
    
    print("Welcome to the Game!!!")
    start = int(input("Please Type 1 or 2 to select one of the options\n"))
    if start == 1:
        print("We will now commence the game!")
        print("")
        validChoice = True
        question1() # here we call the first question directly
    elif start == 2:
        print("I will now show you all the Commands and Instructions")
        print("")
        validChoice = True
    else:
        # this will take us back to the beginning of the loop to see this menu again
        print("This is not a valid choice, please try again")
        print("")
