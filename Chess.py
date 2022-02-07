
from graphics import *
from ChessGUI import ChessGUI


def main():
    gamee = ChessGUI()
    while not gamee.isDone():
        gamee.update()

if __name__ == '__main__': main()
