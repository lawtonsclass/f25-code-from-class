# sudo apt install python3-tk python3-pil python3-pil.imagetk

import tkinter as tk
from PIL import Image, ImageTk
import random
import time

# Open the image file
image = Image.open('cat.png')
pixels = image.load()

# Get the image dimensions
width, height = image.size

# Create a Tkinter window
root = tk.Tk()
root.title("fade")

# Convert the image to a format Tkinter can display
tk_image = ImageTk.PhotoImage(image)

# Create a canvas to display the image
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Add the image to the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

class Pixel:
    def __init__(self, x, y, r, g, b):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b

    # comparison to prefer lighter pixels (and break ties on x/y coordinates)
    def __lt__(self, other):
        my_lightness = (self.r + self.g + self.b) / 3
        other_lightness = (other.r + other.g + other.b) / 3
        return my_lightness > other_lightness or \
               my_lightness == other_lightness and self.x < other.x or \
               my_lightness == other_lightness and self.x == other.x and self.y < other.y

# add every pixel in the image into a heap
import heapq
heap = []
for x in range(width):
    for y in range(height):
        r, g, b, _ = pixels[x, y]
        heapq.heappush(heap, Pixel(x, y, r, g, b))

def pop_brightest_pixels_and_change_to_white():
    global tk_image
    for _ in range(5000):
        if len(heap) > 0:
            p = heapq.heappop(heap)

            # Change the pixel to white (255, 255, 255)
            pixels[p.x, p.y] = (255, 255, 255)

    # Update the image after modification
    tk_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

# Function to continuously update the image
def update_image():
    pop_brightest_pixels_and_change_to_white()
    root.after(1, update_image)  # Re-run this function every 1 ms

# Start the image update loop
root.after(1000, update_image)

# Run the Tkinter event loop
root.mainloop()
