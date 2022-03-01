# ...Alison's very short file

from graphics import *
from ChessGUI import ChessGUI
import sys


def main():

    game = ChessGUI('-q' in sys.argv or '--quiet' in sys.argv)

    try:
        while not game.isDone():
            game.update()
    except GraphicsError:
        print('[log] window closed')
    finally:
        print("Thank you for playing Chess!")

if __name__ == '__main__': main()
