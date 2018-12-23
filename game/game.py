import os
import sys


def clear():
    os.system('cls')


# welcome screen and user input
name = input("What is your name challenger?\n")
play_game = input("{} are you ready to face my Champion(Y/N)\n".format(name))


if play_game == "y":
    # show weapons list
    # choose 1 of 3 weapons
    while True:
        nMove = input("")
        if nMove == "EXIT":
            sys.exit()

    # "in front of you stands a "", wielding a """
    # do you strike left, center, right
    # using random(0, 1) cpu will move left or right
    # if hit -health
    # swap turns
else:
    print("Maybe another time")
    pause = input('')






