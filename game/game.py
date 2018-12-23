import os
import sys


def clear():
    os.system('cls')


# welcome screen and user input
name = input("Type EXIT to exit game\nWhat is your name challenger?\n")
play_game = input("{} are you ready to face my Champion(Y/N)\n".format(name))
if play_game == "y":

    # show weapons list
    # player weapon select

    # "in front of you stands a "", wielding a """
    # do you strike left, center, right
    while True:
        # game loop
        nMove = input("")
        if nMove == "EXIT":
            sys.exit()

    # using random(0, 3) cpu will move left or right or not
    # if hit -health
    # swap turns
else:
    print("Maybe another time")
    pause = input('')
