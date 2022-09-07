import random
from urllib import response

print('''Carrot in a Box, by Al Sweigart al@inventwithpython.py
        \rThis is a bluffing game for two human players.
        \rEach player has a box. One box has a carrot in it.
        \rTo win, you must have the box with the carrot in it.
        \n
        \rThis is a very simple and silly game.
        \n
        \rThe first player looks into their box (the second player must close their eyes).
        \rThe first player than says "There is a carrot in my box" or "There is not a carrot in my box"
        \rThe second player then gets to decide if they want to swap boxes or not.
        ''')

input("Press any key to play... ")

player1 = input("Human player 1, enter your name: ")
player2 = input("Human player 2, enter your name: ")
player_names = player1[:11].center(11) + '     ' + player2[:11].center(11)
print('''HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
''')

print()
print(player_names)
print()
print(f'{player1}, your have a RED box in front of you.')
print(f'{player2}, you have a GOLD box in front of you.')
print(f'{player1}, you will get to look into your box.')
print(f"{player2.upper()}, close your eyes and don't look!!!!")
input(f"When {player2} has their eyes closed, press enter... ")
print()

print(f"{player1} here is the inside of your box")

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
     ___VV____
    |   VV    |
    |   VV    |
    |___||____|    __________
   /    ||   /|   /         /|
  +---------+ |  +---------+ |
  |   RED   | |  |   GOLD  | |
  |   BOX   | /  |   BOX   | /
  +---------+/   +---------+/
   (carrot!)''')
    print(player_names)
else:
    print('''
     _________
    |         |
    |         |
    |_________|    __________
   /         /|   /         /|
  +---------+ |  +---------+ |
  |   RED   | |  |   GOLD  | |
  |   BOX   | /  |   BOX   | /
  +---------+/   +---------+/
  (no carrot!)''')
    print(player_names)

input('Press Enter to continue...')
print('\n' * 100)
print(f"{player1} tell {player2} to open their eyes.")
input('Press Enter to continue...')

print()
print(f"{player1} say one of the following sentences to {player2}...")
print('''\r1) There is a carrot in my box.
        \r2) There is not a carrot in my box.''')
print()
print("Press enter to continue.")
print()
print(f"{player2} do you want to want to swap boxes with {player1} 'YES' or 'NO'")
while True:
    response = input('\r>>>  ').upper()
    if not response.startswith('Y') or response.startswith('N'):
        print(f"{player2} please enter 'YES' or 'NO'")
    else:
        break
firstBox = 'RED ' # Keep the space after 'D'
secondBox = 'GOLD'
if response.startswith('Y'):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox
print('''HERE ARE THE BOXES:

   __________     __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   {}  | |    |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox, secondBox))
print(player_names)
input("Press enter to reveal the winner....")
print()
if carrotInFirstBox:
    print('''
    ___VV____      _________
   |   VV    |    |         |
   |   VV    |    |         |
   |___||____|    |_________|
  /    ||   /|   /         /|
 +---------+ |  +---------+ |
 |   {}  | |    |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox, secondBox))
else:
    print('''
    _________      ___VV____
   |         |    |   VV    |
   |         |    |   VV    |
   |_________|    |___||____|
  /         /|   /    ||   /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox, secondBox))
print(player_names)
if carrotInFirstBox:
    print(f"{player1} is the winner!")
else:
    print(f"{player2} is the winner!")
print('Thanks for playing!')