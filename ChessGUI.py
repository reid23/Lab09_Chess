from graphics import *
from ChessBoard import Board
from Button import Button

class ChessGUI:
    """GUI for a chess game"""

    def __init__(self, chessBoard: Board):
        """Creates a new ChessGUI

        Args:
            chessBoard (ChessBoard): holds the info of a chess game
        """
        # self.chessBoard = chessBoard
        self.win = GraphWin("Chess: the ultimate game of wit", 800, 600, autoflush = False)
        self.win.setBackground("white")
        self.win.setCoords(-10,-30,150,90)
        board = chessBoard.getGameState('all') # TODO: change later
        for x in range(8):
            for y in range(8):
                board[x][y][0].draw(self.win)
        self.quitButton = Button(Point(115,-8), 50, 8, "Quit", self.win)
        self.quitButton.activate()
        self.replayButton = Button(Point(115,-20), 50, 8, "Reset", self.win)
        self.replayButton.activate()

        title = Text(Point(115, 65), "chess") 
        title.setSize(36)
        title.draw(self.win)
        subtitle = Text(Point(115, 57), "a game of wit") 
        subtitle.setSize(23)
        subtitle.draw(self.win)
        desc = Text(Point(115, 30), "\"a board game of strategic skill\nfor two players, played on a\ncheckered board. Each player\nbegins the game with sixteen\npieces that are moved and\nused to capture opposing\npieces according to precise\nrules. The object is to put the\nopponent's king under a direct\nattack from which escape is\nimpossible (checkmate).\"")
        desc.setSize(15)
        desc.draw(self.win)

        promptBox = Rectangle(Point(0,-24),Point(80,-4))
        promptBox.setFill('lightgrey')
        promptBox.setOutline("lightgrey")
        promptBox.draw(self.win)
        self.prompt = Text(Point(40,-14), "Prompt goes here")
        self.prompt.draw(self.win)

        self.win.update()

    
    def drawStartBoard(self):
        """Draws the starting board, resets the game
        """
        # self.chessBoard.reset() # TODO: NEED TO CREATE A RESET CHESS BOARD METHOD


    def updatePrompt(self, msg : str) -> None:
        """updates the prompt on the GUI

        Args:
            msg (str): new message for prompt box
        """

        self.prompt.setText(msg) # TODO: fix length of message, needs to wrap :)
    

    def updateBoard(self):
        self.win.update()
        


if __name__ == '__main__':
    b = Board()
    cGUI = ChessGUI(b)
    cGUI.updateBoard()
    
    

    

    
