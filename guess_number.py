# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code

num_range = 100
num_random = 0

# helper function to start and restart the game
def new_game():
    global num_range
    print("Here: " + str(num_range))
    if num_range == 100:
        num_random = random.randrange(0, 100)
    elif num_range == 1000:
        num_random = random.randrange(0, 1000)
    
    print("Starting a new Game.. Range is " + str(num_range)) 
    print(num_random)

# define event handlers for control panel
def range100():
    global num_range
    # button that changes range to range [0,100) and restarts
    num_range = 100
    new_game()

def range1000():
    global num_range
    # button that changes range to range [0,1000) and restarts
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    
    # remove this when you add your code
    pass
   
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame

frame.start()
new_game()

# always remember to check your completed program against the grading rubric