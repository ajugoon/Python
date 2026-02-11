import tkinter as tk

# --- Configuration ---
WIDTH = 600
HEIGHT = 400
SPRITE_RADIUS = 15
FOLLOW_SPEED = 0.1  # smaller = slower movement

# --- Setup ---
root = tk.Tk()
root.title("Mouse-Following Sprite")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Initial sprite position
sprite_x = WIDTH // 2
sprite_y = HEIGHT // 2

# Create sprite (circle)
sprite = canvas.create_oval(
    sprite_x - SPRITE_RADIUS,
    sprite_y - SPRITE_RADIUS,
    sprite_x + SPRITE_RADIUS,
    sprite_y + SPRITE_RADIUS,
    fill="blue"
)

# Target position (mouse)
target_x = sprite_x
target_y = sprite_y


def update_target(event):
    global target_x, target_y
    target_x = event.x
    target_y = event.y


def move_sprite():
    global sprite_x, sprite_y

    # Move a fraction of the distance toward the target
    dx = target_x - sprite_x
    dy = target_y - sprite_y

    sprite_x += dx * FOLLOW_SPEED
    sprite_y += dy * FOLLOW_SPEED

    # Update sprite position
    canvas.coords(
        sprite,
        sprite_x - SPRITE_RADIUS,
        sprite_y - SPRITE_RADIUS,
        sprite_x + SPRITE_RADIUS,
        sprite_y + SPRITE_RADIUS
    )

    # Repeat animation
    root.after(16, move_sprite)  # ~60 FPS


# Bind mouse movement
canvas.bind("<Motion>", update_target)

# Start animation loop
move_sprite()

root.mainloop()
