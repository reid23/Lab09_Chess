# ...Alison's very short file

from graphics import *
from ChessGUI import ChessGUI


def main():
    game = ChessGUI()
    try:
        while not game.isDone():
            game.update()
    except:
        print("Thank you for playing Chess!")

if __name__ == '__main__': main()
