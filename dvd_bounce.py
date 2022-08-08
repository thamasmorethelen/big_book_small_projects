import bext
import random


width, height = bext.size()
try:
    while True:
        bext.fg('random')
        bext.bg('random')
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        bext.goto(x, y)
        print('*', end='')
except KeyboardInterrupt:
    pass