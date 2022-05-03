from tkinter import *

# TODO Figure out project structure (all the relevant classes)
# Create files for each class
# Create structure for all relevant images/gifs/other assets

# TODO Create playable ship
# get basic image

# TODO Create projectile(s)

# TODO Create 1 Enemy type (with plans for more in the future)
# setup class hierarchy duh
# get basic image, basic gif for bonus points

# TODO Create Scoreboard

# TODO Pause Game


# TODO Create basic GUI with Tkinter

# -------------------------- UI -------------------------- #

BACKGROUND_COLOR = "#000"

window = Tk()
window.title("Space Invaders")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=1200, height=720, bg=BACKGROUND_COLOR, highlightthickness=0)

window.mainloop()
