# Here is a program that plays music in the background
# You have to install the "playsound" package
# At the command prompt in the terminal window type: 
# pip3 install playsound
# pip3 install PyObjC (but only if you get a message about it)

# We can re-size the terminal here
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=150))

from playsound import playsound
playsound('bensound.mp3', 0)

# The variable tracks if we have made a vaild choice from the menu system
validChoice = False

# This is a function that runs our menu system
# It will be called as long as a valid choice has not been made

def runMenu():

    global validChoice

    print("\u001b[33m Welcome to Cineplex!!!\u001b[0m")
    print("\u001b[34m Welcome to Cineplex!!!\u001b[0m")
    print("\u001b[35m Welcome to Cineplex!!!\u001b[0m")
    print("\u001b[36m Welcome to Cineplex!!!\u001b[0m")
    print("\u001b[37m Welcome to Cineplex!!!\u001b[0m")
    print(" Welcome to Cineplex :)")

    # This is how we do a multiline print for the ASCII ART
    # Try to find a sample that displays well and does not appear to be mis-formatted

    print(""" 

    +-+-+-+-+-+ +-+-+-+-+-+-+-+
    |M|o|v|i|e| |T|i|m|e|!|!|!|
    +-+-+-+-+-+ +-+-+-+-+-+-+-+     
                
    """)
    
    print("Please choose your category!")
    print("1. Toddler: age 0-2 inclusive")
    print("2. Youth: age 3-12 inclusive")
    print("3. Teenager: age 13-18 inclusive")
    print("4. Adult: age 19-64 inclusive")
    print("5. Senior: age 65+")

    category = int(input("What is your age group? \n"))

    if category == 1:
        print("No charge for this customer!")
        validChoice = True
        
    elif category == 2:
        print ("You pay $5.00 plus tax")
        validChoice = True

    elif category == 3:
        print ("You pay $11.50 plus tax")
        validChoice = True
        
    elif category == 4:
        print ("You pay $15.50 plus tax")
        validChoice = True

    elif category == 5:
        print ("You pay $5.00 plus tax")
        validChoice = True

    else:
        print ("This is not a valid choice")
        print ("Please choose again!")
        
        validChoice = False

def doMoreStuff():

    # Copy and paste these if you are looking for some colour in the terminal window!
    print("\u001b[33m Do more stuff here!!!\u001b[0m")
    print("\u001b[34m Do more stuff here!!!\u001b[0m")
    print("\u001b[35m Do more stuff here!!!\u001b[0m")
    print("\u001b[36m Do more stuff here!!!\u001b[0m")
    print("\u001b[37m Do more stuff here!!!\u001b[0m")

# Game starts at this point
# We must call the menu function in order to see our first set of choices

while validChoice == False:
    
    # Call your first function which is IN THE WHILE LOOP
    runMenu()

# Call your second function which is OUTSIDE OF THE WHILE LOOP
doMoreStuff()

print("Now we have a choice and we can move on with the game!")

