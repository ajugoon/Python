# This is the same game as before, but now there is a score for
# each of the obstacles hit based on their colour.


import tkinter as tk
import random
import math

# --- Configuration ---
WIDTH = 600
HEIGHT = 400

SPRITE_RADIUS = 15
OBSTACLE_RADIUS = 12

FOLLOW_SPEED = 0.1
OBSTACLE_SPEED = 4

# --- Setup ---
root = tk.Tk()
root.title("Avoid the Falling Object")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# --- Score Variables ---
green_score = 0
red_score = 0

score_label = tk.Label(root, text="Green: 0    Red: 0", font=("Arial", 14))
score_label.pack(pady=10)

# --- Player sprite ---
sprite_x = WIDTH // 2 
sprite_y = HEIGHT // 2
target_x = sprite_x
target_y = sprite_y

sprite = canvas.create_oval(
    sprite_x - SPRITE_RADIUS,
    sprite_y - SPRITE_RADIUS,
    sprite_x + SPRITE_RADIUS,
    sprite_y + SPRITE_RADIUS,
    fill="blue"
)

# --- Obstacle 1 (Red) ---
obstacle_x = random.randint(OBSTACLE_RADIUS, WIDTH - OBSTACLE_RADIUS)
obstacle_y = -OBSTACLE_RADIUS

obstacle = canvas.create_oval(
    obstacle_x - OBSTACLE_RADIUS,
    obstacle_y - OBSTACLE_RADIUS,
    obstacle_x + OBSTACLE_RADIUS,
    obstacle_y + OBSTACLE_RADIUS,
    fill="red"
)

# --- Obstacle 2 (Green) ---
obstacle2_x = random.randint(OBSTACLE_RADIUS, WIDTH - OBSTACLE_RADIUS)
obstacle2_y = -OBSTACLE_RADIUS

obstacle2 = canvas.create_oval(
    obstacle2_x - OBSTACLE_RADIUS,
    obstacle2_y - OBSTACLE_RADIUS,
    obstacle2_x + OBSTACLE_RADIUS,
    obstacle2_y + OBSTACLE_RADIUS,
    fill="green"
)

def update_score_label():
    score_label.config(text=f"Green: {green_score}    Red: {red_score}")

def reset_obstacle():
    global obstacle_x, obstacle_y
    obstacle_x = random.randint(OBSTACLE_RADIUS, WIDTH - OBSTACLE_RADIUS)
    obstacle_y = -OBSTACLE_RADIUS 

def reset_obstacle2():
    global obstacle2_x, obstacle2_y
    obstacle2_x = random.randint(OBSTACLE_RADIUS, WIDTH - OBSTACLE_RADIUS)
    obstacle2_y = -OBSTACLE_RADIUS 

def update_target(event):
    global target_x, target_y
    target_x = event.x
    target_y = event.y

def check_collision():
    distance = math.hypot(sprite_x - obstacle_x, sprite_y - obstacle_y)
    return distance < SPRITE_RADIUS + OBSTACLE_RADIUS

def check_collision2():
    distance = math.hypot(sprite_x - obstacle2_x, sprite_y - obstacle2_y)
    return distance < SPRITE_RADIUS + OBSTACLE_RADIUS

def move_objects():
    global sprite_x, sprite_y
    global obstacle_y, obstacle2_y
    global green_score, red_score

    # --- Move player toward mouse ---
    dx = target_x - sprite_x
    dy = target_y - sprite_y
    sprite_x += dx * FOLLOW_SPEED
    sprite_y += dy * FOLLOW_SPEED

    canvas.coords(
        sprite,
        sprite_x - SPRITE_RADIUS,
        sprite_y - SPRITE_RADIUS,
        sprite_x + SPRITE_RADIUS,
        sprite_y + SPRITE_RADIUS
    )

    # --- Move obstacles downward ---
    obstacle_y += OBSTACLE_SPEED
    obstacle2_y += OBSTACLE_SPEED

    canvas.coords(
        obstacle,
        obstacle_x - OBSTACLE_RADIUS,
        obstacle_y - OBSTACLE_RADIUS,
        obstacle_x + OBSTACLE_RADIUS,
        obstacle_y + OBSTACLE_RADIUS
    )

    canvas.coords(
        obstacle2,
        obstacle2_x - OBSTACLE_RADIUS,
        obstacle2_y - OBSTACLE_RADIUS,
        obstacle2_x + OBSTACLE_RADIUS,
        obstacle2_y + OBSTACLE_RADIUS
    )

    # --- Reset if off screen ---
    if obstacle_y > HEIGHT + OBSTACLE_RADIUS:
        reset_obstacle()

    if obstacle2_y > HEIGHT + OBSTACLE_RADIUS:
        reset_obstacle2()

    # --- Collision Detection ---
    if check_collision():
        red_score += 1
        update_score_label()
        reset_obstacle()

    if check_collision2():
        green_score += 1
        update_score_label()
        reset_obstacle2()

    root.after(16, move_objects)

# --- Bind mouse movement ---
canvas.bind("<Motion>", update_target)

# --- Start loop ---
move_objects()
root.mainloop()