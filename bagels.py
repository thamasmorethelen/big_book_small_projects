import random
# # # User must guess three digit number
# # # If they guess a number and it it in the wrong place return pico
# #         # ex: number = 123. user guesses 132. print pico
# #         # if user guesses 412 print pico pico
# #         # if user guesses a number and it's in the right place print fermi
# #         # if the user doesn't guess any correct numbers print bagels
# #         # users have just 10 guesses before the project quits


def make_three():
    num = []
    for i in range(3):
        i = random.randint(1, 9)
        num += [str(i)]
    return num


def welcome():
    print("""
        \nBagels, a deductive logic game.
        \rBy Al Sweigart al@inventwithpython.com
        \rI'm thinking of a 3-digit number. Try to guess what it is.
        \rHere are some clues:
        \rWhen I say Pico that means one digit is correct. pico pico mean two are correct.
        \rWhen I say fermi one digit is correct and in the right position.
        \rBegels means no digit is correct.
        \rYou have 10 guesses
    """)


def bagels():
    welcome()
    num = make_three()
    print(num)
    guess = ''
    count = 0
    guess_count = 0
    message = ''
    play_again = True
    while play_again:
        guess_count += 1
        guess = list((input(f'''
                            \r{message}
                            \rGuess #{guess_count} ''')))
        message = ''
        count = 0
        guess = list(guess)
        for i in range(len(guess)):
            if guess[i] not in num:
                count += 1
            if count == 3:
                message = 'Bagels'
            if guess[i] == num[i]:
                message += 'Fermi '
            if guess[i] in num and guess[i] != num[i]:
                message += 'Pico '
        print(count)
        if len(guess) != 3:
            input('Oh no! Try again. Remember 3 digits... ')

        if guess == num:
            print(f'Wow! you did it! And it only took {guess_count} times!!')
            play_again = input('Would you like [N/Y]: ').lower()
            if play_again == 'y' or play_again == 'yes':
                print('Yay!')
                guess_count = 0
                message = ''
            else:
                print('Bye Bye!')
                play_again = False
        if guess_count == 10:
            print('oh no! Game over!')
            play_again = input('Would you like [N/Y]: ').lower()
            if play_again == 'y' or play_again == 'yes':
                print('Yay!')
                guess_count = 0
                message = ''
            else:
                print('Bye Bye!')
                play_again = False
            



if __name__ == "__main__":
    bagels()

# # l = ['1','2',3]
# # a = ['a', 'b', 3]
# # count = 0
# # for i in l:
# #     for j in a:
# #         if i == j:
# #             count += 1
# # print(count)

