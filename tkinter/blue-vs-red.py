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

# --- Player sprite ---

# Note: "//" means 'floor' division
# Divides two numbers and then rounds the result down to the nearest whole number

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

# --- Obstacle ---
obstacle_x = random.randint(OBSTACLE_RADIUS, WIDTH - OBSTACLE_RADIUS)
obstacle_y = -OBSTACLE_RADIUS # places the center of the obstacle just above the visible screen.

obstacle = canvas.create_oval(
    obstacle_x - OBSTACLE_RADIUS,
    obstacle_y - OBSTACLE_RADIUS,
    obstacle_x + OBSTACLE_RADIUS,
    obstacle_y + OBSTACLE_RADIUS,
    fill="red"
)


def reset_obstacle():
    global obstacle_x, obstacle_y

    # Pick a random x-position for the center of the circle,
    # but make sure the entire circle stays inside the screen
    obstacle_x = random.randint(OBSTACLE_RADIUS, WIDTH - OBSTACLE_RADIUS)

    # places the center of the obstacle just above the visible screen
    obstacle_y = -OBSTACLE_RADIUS 


def update_target(event):
    global target_x, target_y
    target_x = event.x
    target_y = event.y


def check_collision():
    distance = math.hypot(sprite_x - obstacle_x, sprite_y - obstacle_y)
    return distance < SPRITE_RADIUS + OBSTACLE_RADIUS


def move_objects():
    global sprite_x, sprite_y, obstacle_y

    # --- Move player toward mouse ---
    dx = target_x - sprite_x
    dy = target_y - sprite_y
    sprite_x += dx * FOLLOW_SPEED
    sprite_y += dy * FOLLOW_SPEED

    # Move the shapes to a new position
    canvas.coords(
        sprite,
        sprite_x - SPRITE_RADIUS,
        sprite_y - SPRITE_RADIUS,
        sprite_x + SPRITE_RADIUS,
        sprite_y + SPRITE_RADIUS
    )

    # --- Move obstacle downward ---
    obstacle_y += OBSTACLE_SPEED

    canvas.coords(
        obstacle,
        obstacle_x - OBSTACLE_RADIUS,
        obstacle_y - OBSTACLE_RADIUS,
        obstacle_x + OBSTACLE_RADIUS,
        obstacle_y + OBSTACLE_RADIUS
    )

    # --- Reset if off screen ---
    if obstacle_y > HEIGHT + OBSTACLE_RADIUS:
        reset_obstacle()

    # --- Collision ---
    if check_collision():
        reset_obstacle()

    root.after(16, move_objects)  # 16 ms ~ 60 FPS


# --- Bind mouse movement ---
canvas.bind("<Motion>", update_target)

# --- Start loop ---
move_objects()
root.mainloop()
