import random
from secrets import choice
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the module BEXT')
    print("To install bext follow the instructions in the link below")
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Costants
WIDTH, HEIGHT = bext.size()
WIDTH -= 1

NUMBER_OF_LOGOS = 5 # See notes in book on page 26
PAUSE_AMOUNT = 0.2 # See notes page 26
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
#Key names for logo dictionaries
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    #generate some logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
                        logos.append({COLOR: random.choice(COLORS),
                        X: random.randint(1, WIDTH - 4),
                        Y: random.randint(1, HEIGHT - 4),
                        DIR: random.choice(DIRECTIONS)}
        )
                        if logos[-1][X] % 2 == 0:
                            logos[-1][X] -+ 1
    cornerBounces = 0 # counts how many times a logo hits a corner
    while True: # main loop
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('    ', end=" ")

            originalDirection = logo[DIR]

            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT -1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1