# ...Alison's very short file

from graphics import *
from ChessGUI import ChessGUI

# if the game does not run at first, make sure to do the following in command line:
# python -m pip install requests


def main():
    game = ChessGUI()
    try:
        while not game.isDone():
            game.update()
        print("Thank you for playing Chess!")
    except:
        print("Thank you for playing Chess!")

if __name__ == '__main__': main()
