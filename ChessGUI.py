from graphics import *
from ChessBoard import Board
from Button import Button

class ChessGUI:
    """GUI for a chess game"""

    def __init__(self):
        """Creates a new ChessGUI

        Args:
            chessBoard (ChessBoard): holds the info of a chess game
        """
        # self.chessBoard = chessBoard
        self.win = GraphWin("Chess: the ultimate game of wit", 800, 600, autoflush = False)
        self.win.setBackground("white")
        self.win.setCoords(-10,-30,150,90)
        self.chessBoard = Board()
        board = self.chessBoard.getGameState('all') # TODO: change later
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

        self.done = False

    
    def drawStartBoard(self):
        """Draws the starting board, resets the game
        """
        # self.chessBoard.reset() # TODO: NEED TO CREATE A RESET CHESS BOARD METHOD


    def updatePrompt(self, msg : str) -> None:
        """updates the prompt on the GUI

        Args:
            msg (str): new message for prompt box
        """
        l = len(msg)
        prev = 0
        cur = 70
        s = ""
        while cur < l:
            s += msg[prev:cur]
            if msg[cur] != " ":
                s+="-"
            else:
                cur+=1
            s+="\n"
            prev = cur
            cur += 70
        s+=msg[prev:]
        self.prompt.setText(s) # TODO: fix length of message, needs to wrap :)
    

    def updateWin(self):
        self.win.update()

    def update(self):
        pt = self.win.getMouse()
        
        if self.quitButton.clicked(pt):
            self.done = True
            self.win.close()
            return

        self.updateWin()

    def isDone(self):
        """Returns if window should be closed

        Returns:
            [bool]: true if done, false if not
        """
        return self.done

        


if __name__ == '__main__':
    b = Board(None)
    cGUI = ChessGUI(b)
    cGUI.updatePrompt("ghello there my name is alison this is a test because i don't know what else to say hello hello everything is awesome no i'm not qutoing a movieeee")
    cGUI.updateWin()

    while not cGUI.isDone():
        cGUI.update()
    
    

    

    
