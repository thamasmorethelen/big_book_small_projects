import random
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

NUMBER_OF_LOGOS = 5
# See notes in book on page 26
PAUSE_AMOUNT = 0.2
# See notes page 26
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
# Key names for logo dictionaries
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # generate some logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                                X: random.randint(1, WIDTH - 4),
                                Y: random.randint(1, HEIGHT - 4),
                                DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1
    cornerBounces = 0
    # counts how many times a logo hits a corner
    while True:
        # main loop

        for logo in logos:
            # try:

            bext.goto(logo[X], logo[Y])
            print('   ', end="   ")

            originalDirection = logo[DIR]

            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1
            # See if the logo bounces off the left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
            # See if the logo bounces off the right edge
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT
            # See if the logo boucnce off the top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] == DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT
            # See if the logo bounces off the bottum edge.
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                # change the color when the logo bounces
                logo[COLOR] = random.choice(COLORS)
            # move the logo (X moves by 2 Y moves by 1
            # characters are twice as tall as they are wide)

            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1
            if BaseException:
                bext.clear()
                logos = []
                for i in range(NUMBER_OF_LOGOS):
                    logos.append({COLOR: random.choice(COLORS),
                                            X: random.randint(1, WIDTH - 4),
                                            Y: random.randint(1, HEIGHT - 4),
                                            DIR: random.choice(DIRECTIONS)})
                    if logos[-1][X] % 2 == 1:
                        logos[-1][X] -= 1
                        # Display Number of corner bounces
                        bext.goto(5, 0)
                        bext.fg('white')
        print(f"Corner bounces: {cornerBounces}",  end= ' ')

        for logo in logos:
            # Draw the logos at the new location
            # if logo[X] > 0 and logo[Y] > 0:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end= ' ')
        bext.goto(0, 0)

        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bounce DVD Logo, by Al Sweigart')
        sys.exit
