from tkinter import *#Tk, Toplevel, Canvas, Button
import time

# delay program start to open up powerpoint first
time.sleep(3)

# setting the starting coordinate of the line so that
# on motion it is possible to immediately draw it
def set_first(event):
    points.extend([event.x, event.y])

# on motion append new coordinates to the list and if there are
# 4 (the minimum), create a new line and save the id
# otherwise update the existing line
def append_and_draw(event):
    global line
    points.extend([event.x, event.y])
    if len(points) == 4:
        line = canvas.create_line(points, **line_options)
    else:
        canvas.coords(line, points)

# when released clear the list to not waste space
# and not necessarily but also set "id" to None
def clear_list(event=None):
    global line
    points.clear()
    line = None


line = None  # this is a reference to the current line (id)
points = []  # list to keep track of current line coordinates
line_options = {'fill':'yellow','width':15}  # dictionary to allow easier change of line options
# in python 3.8 and later, you can use 'alpha':0.2 to make the solid line opaque (should try)

# just a variable to more easily store the transparent color
transparent_color = 'grey15'

# creating the root window which will help with drawing the line
# because it will "block" mouse because `-alpha` (0.01 seems to be the lowest value)
# attribute is used, however it makes everything transparent on the window
# so need another window to "host" the canvas

root = Tk()
root.attributes('-alpha', 0.01)
root.attributes('-fullscreen', True)

# just press Esc key to close the whole thing, otherwise
# it is only doable by pressing Alt + F4 or turning off
# the computer
root.bind('<Escape>', lambda e: root.quit())

# create the host window, because it allows to have only
# one transparent color while keeping the other opaque and
# visible
top = Toplevel(root)
frame = Frame(top, bg='grey15')
frame.pack(side='top', fill='x')

# function to clear the canvas, this should be called when pressing next/prev slide buttons too
def clear_canvas():
    canvas.delete("all")

btn_next = Button(frame, bd=2, text="Next Slide")
btn_prev = Button(frame, bd=2, text="Previous Slide")
btn_clear = Button(frame, bd=2, text="Clear Highlight", command=clear_canvas)
btn_keyboard = Button(frame, bd=2, text="Keyboard")

btn_next.pack(side='left')
btn_prev.pack(side='left')
btn_clear.pack(side='left')
btn_keyboard.pack(side='left')

top.configure(bg=transparent_color)
top.attributes('-transparentcolor', transparent_color)
top.attributes('-topmost', True)
top.attributes('-fullscreen', True)

# set the focus to root because that is where events are bound
root.focus_set()

# create the canvas to draw on
canvas = Canvas(top, bg=transparent_color, highlightthickness=0)
canvas.pack(fill='both', expand=True)

# bind all the events to `root` which "blocks" mouse
# but is also almost (because it has a very small alpha value
# it is not entirely invisible but human eye won't notice much)
# invisible
root.bind('<Button-1>', set_first)
root.bind('<B1-Motion>', append_and_draw)
root.bind('<ButtonRelease-1>', clear_list)

root.mainloop()