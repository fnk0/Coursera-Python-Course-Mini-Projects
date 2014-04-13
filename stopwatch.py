# template for "Stopwatch: The Game"
# Program written by Marcus Gabilheri

import simplegui

# define global variables


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass

# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
  pass

def stop():
  pass

def reset():
  pass


# define event handler for timer with 0.1 sec interval


# define draw handler

def draw(canvas):
	canvas.draw_text("Hello World!", [100, 100], 24, "Green")
	canvas.draw_circle([100, 100], 2, 2, "Red")


# create frame

frame = simplegui.create_frame("Stopwatch The Game", 300, 200)

# register event handlers

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frame

frame.start()

# Please remember to review the grading rubric
