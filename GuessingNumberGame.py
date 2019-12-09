"""
Guess The Number

This is a programme where the computer randomly generates a number between 0 and 20.
The user needs to guess what the number is.
If the user guesses wrong, tell them their guess is either too high, or too low.
This will get you started with the random library if you haven't already used it.
"""


import random


def game():
    the_num = random.randint(0, 20)
    # print(the_num)
    user_input = 0

    while (user_input != the_num):
        user_input = int(input("Guess a number between 0-20: "))
        print("You guess: " + str(user_input))
        if (user_input < the_num):
            print("Your guess is too low.")
        elif (user_input > the_num):
            print("Your guess is too high.")
        else:
            print("You got it!")
            break


game()
