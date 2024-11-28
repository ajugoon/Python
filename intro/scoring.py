
score = 0 # add this for score

def question1_MC():

    global score # add this for score

    print ("Question #1: What school do you attend?")

    print("")
    print("1. St. Mike's")
    print("2. UCC")
    print("3. RSGC")
    print("")
  
    response1 = int(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == 1:
        print("Incorrect")
        print("")
        print("Now we will move on to question 2")
        print("")
        # question2()
   
  
    elif response1 == 2:
        print("Great Job!")
        score = score + 10 # add this for score
        print ("You now have: " + str(score) + " points") # add this for score
        print("")
        print("Now we will move on to question number 2!")
        print("")
        # question2()
    
  
    elif response1 == 3:
        print("Incorrect")
        print("")
        print("Now we will move on to question 2")
        print("")
        # question2()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question1()


### Your Game Starts Here ###
### MAIN GAME LOOP ###

validChoice = False

while (validChoice == False):
    
    
    print("Welcome to the Game!!!")
    print("")
    print("Type 0 for TUTORIAL")
    print("Type 1 for MULTIPLE CHOICE")
    print("Type 2 for YES-NO QUESTIONS")
    print("")

    start = int(input("Your choice? \n"))
    print("")
    
    if start == 0:
        print("We will now look at the TUTORIAL!")
        print("")
        validChoice = True
        # tutorial() # here we call the TUTORIAL directly

    elif start == 1:
        print("We will now look at the MULTIPLE CHOICE QUESTIONS!")
        print("")
        validChoice = True
        question1_MC() # here we call the first MC question directly

    elif start == 2:
        print("We will now look at the YES-NO QUESTIONS!")
        print("")
        validChoice = True
        # question_YN() # here we call the first YES-NO question directly

    else:
        # this will take us back to the beginning of the loop to see this menu again
        print("This is not a valid choice, please try again")
        print("")




    
    