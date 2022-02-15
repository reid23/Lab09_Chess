
from graphics import *
from ChessGUI import ChessGUI


def main():
    game = ChessGUI()
    while not game.isDone():
        game.update()

if __name__ == '__main__': main()
