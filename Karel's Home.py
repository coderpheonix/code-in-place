from karel.stanfordkarel import *


# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# move to the beeper, pick it up, and
# return home.
def main():
    move()
    # add your code heredef main():
    move_to_beeper()  # Move to the beeper
    pick_beeper()  # Pick up the beeper
    return_home()  # Return to the starting position
def move_to_beeper():
    move()
    turn_right()
    move()
    turn_left()
    move()

def return_home():
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_left()
    turn_left()
    turn_left()

def turn_right():
    # Turn left three times to turn right
    for _ in range(3):
        turn_left()

def turn_around():
    # Turn left twice to face the opposite direction
    turn_left()
    turn_left()
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
