import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# -------------------------------------------------
# CONFIGURATION SECTION
# -------------------------------------------------

# Width and height of the game window
WIDTH = 600
HEIGHT = 400

# Number of rows and columns in our grid
ROWS = 2
COLS = 3

# Padding creates space between squares
SQUARE_PADDING = 20


# -------------------------------------------------
# CREATE MAIN WINDOW AND CANVAS
# -------------------------------------------------

# Create the main application window
root = tk.Tk()
root.title("Trivia Grid Game")

# Create a drawing area (canvas) where shapes will appear
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()


# -------------------------------------------------
# CREATE TRIVIA QUESTIONS
# -------------------------------------------------

# Each question is a tuple:
# (question text, correct answer)
questions = [
    ("What planet is known as the Red Planet?", "mars"),
    ("What is the largest ocean on Earth?", "pacific"),
    ("How many continents are there?", "7"),
    ("What gas do plants breathe in?", "carbon dioxide"),
    ("Who wrote Hamlet?", "shakespeare"),
    ("What is 9 x 9?", "81")
]

# Shuffle the questions so they appear in random positions
random.shuffle(questions)


# -------------------------------------------------
# CREATE GRID OF SQUARES
# -------------------------------------------------

# We will store all square IDs here
squares = []

# This dictionary will store information about each square
# The key will be the square ID
# The value will be question, answer, and reveal status
square_data = {}

# Calculate how wide and tall each grid space should be
square_width = WIDTH // COLS
square_height = HEIGHT // ROWS

# Loop through rows and columns to create grid layout
for row in range(ROWS):
    for col in range(COLS):

        # Calculate square coordinates
        x1 = col * square_width + SQUARE_PADDING
        y1 = row * square_height + SQUARE_PADDING
        x2 = (col + 1) * square_width - SQUARE_PADDING
        y2 = (row + 1) * square_height - SQUARE_PADDING

        # Draw the square
        square = canvas.create_rectangle(
            x1, y1, x2, y2,
            fill="lightblue"
        )

        # Take one question from the shuffled list
        question, answer = questions.pop()

        # Store information about this square
        square_data[square] = {
            "question": question,
            "answer": answer,
            "revealed": False  # This keeps track if it was already clicked
        }

        # Save square ID to list
        squares.append(square)


# -------------------------------------------------
# FUNCTION TO HANDLE MOUSE CLICKS
# -------------------------------------------------

def handle_click(event):
    """
    This function runs every time the user clicks
    on the canvas.
    The 'event' object contains information about
    where the mouse was clicked.
    """

    # Find the canvas object closest to where the mouse was clicked
    clicked = canvas.find_closest(event.x, event.y)

    # If nothing was clicked, stop the function
    if not clicked:
        return

    # Get the ID number of the clicked object
    square = clicked[0]

    # If the clicked object is not one of our squares, stop
    if square not in square_data:
        return

    # If this square has already been revealed, stop
    if square_data[square]["revealed"]:
        return

    # Get the question and correct answer for this square
    question = square_data[square]["question"]
    correct_answer = square_data[square]["answer"]

    # Show a popup asking the user the question
    user_answer = simpledialog.askstring("Trivia Question", question)

    # If the user cancels the popup, stop
    if user_answer is None:
        return

    # Compare the user's answer to the correct answer
    # We convert both to lowercase and remove extra spaces
    if user_answer.lower().strip() == correct_answer:
        # If correct, change square color to green
        canvas.itemconfig(square, fill="lightgreen")
        messagebox.showinfo("Result", "Correct!")
    else:
        # If incorrect, change square color to red
        canvas.itemconfig(square, fill="salmon")
        messagebox.showinfo("Result", f"Incorrect! Answer: {correct_answer}")

    # Mark this square as revealed so it cannot be clicked again
    square_data[square]["revealed"] = True


# -------------------------------------------------
# CONNECT MOUSE CLICK TO FUNCTION
# -------------------------------------------------

# This tells tkinter:
# "When the left mouse button is clicked on the canvas,
# run the handle_click function."
canvas.bind("<Button-1>", handle_click)


# -------------------------------------------------
# START THE PROGRAM
# -------------------------------------------------

# Start the tkinter event loop
# This keeps the window open and listening for events
root.mainloop()