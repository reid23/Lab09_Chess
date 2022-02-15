from graphics import *
from numpy import piecewise
from ChessBoard import Board
from Button import Button
from Pawn import Pawn
from Queen import Queen
from Knight import Knight
from King import King
from Bishop import Bishop
from Rook import Rook

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
        # self.chessBoard.reset()
        for x in range(8):
            for y in range(8):
                self.chessBoard.getThing(x,y,0).draw(self.win)
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

        self.done = False

        self.updatePrompt("ghello there my name is alison this is a test because i don't know what else to say hello hello everything is awesome no i'm not qutoing a movieeee")

        self.curPlayer = True # true for white, start with white

        self.prevState = Board()
        # self.prevState.reset()
        # for i in range(8):
        #     for j in range(8):
        #         if (i%3 == 0):
        #             self.prevState.putThing(True, (i,j), 'lit')
        #         self.prevState.putThing(Pawn(True,(i,j)), (i,j), 'piece')

        self.resetGame()
        self.updateWin()

        # MOVE STATES
        self.hasSelected = False

    
    def resetGame(self):
        """Draws the starting board, resets the game
        """

        for x in range(8):
            for y in range(8):
                piece = self.chessBoard.getThing(x, y, 2)
                if piece != None:
                    piece.undraw()
                self.chessBoard.getThing(x, y, 0).undraw()
        self.chessBoard.reset()

        for x in range(8):
            for y in range(8):
                self.chessBoard.getThing(x, y, 0).draw(self.win)
                piece = self.chessBoard.getThing(x, y, 2)
                print(piece, "----")
                if piece != None:
                    print(piece.curPos)
                    piece.draw(self.win)
        
        self.curPlayer = True
        self.hasSelected = False


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
        for i in range(7):
            for j in range(7):
                print(self.prevState.getThing(i,j,1),end=" ")
            print()
        self.drawDiff(self.prevState - self.chessBoard)
        # print(self.prevState - self.chessBoard)
        self.win.update()
        
    
    def coordClicked(self, pt):
        # returns tuple of grid cooord that has been pressed
        # TODO IMPLEMENT
        print("BLUB DO THIS LDKFS:DLKFJ:LSDKFJ")
        curX = pt.getX()
        curY = pt.getY()
        if (curX < 0 or curY < 0 or curX > 80 or curY > 80):
            return False
        curX = int(curX/10)
        curY = int(curY/10)
        
        for x in range(8):
            for y in range(8):
                if self.chessBoard.getThing(x,y,2).color == self.curPlayer:
                    self.chessBoard.lightUpSquares((x,y))
                    return True
        return False


    def update(self):
        """[summary]

        Returns:
            [bool]: Returns true if done
        """
        pt = self.win.getMouse()
        
        if self.quitButton.clicked(pt):
            self.done = True
            self.win.close()
            return
        
        if self.replayButton.clicked(pt):
            self.done = False
            self.resetGame()

        if self.coordClicked(pt):
            self.hasSelected = True
        
        self.updateWin()

    def isDone(self):
        """Returns if window should be closed

        Returns:
            [bool]: true if done, false if not
        """
        return self.done
    
    def drawDiff(self, changes):
        for change in changes:
            x = change[0][0]
            y = change[0][1]
            # print(change,end="  ")
            # print("===",x,y, end = "     ")
            # print(self.prevState.getThing(x,y,change[0][2]))


            if (change[0][2] == 1):
                # curTileOn = self.chessBoard.getThing(x,y,1)
                curTile = self.chessBoard.getThing(x,y,0)
                prevTile = self.prevState.getThing(x,y,0)
                prevTile.undraw()
                curTile.undraw()

                if change[1]:
                    curTile.setFill(color_rgb(149, 222, 146))
                else:
                    if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                        curTile.setFill('grey')
                    else:
                        curTile.setFill(color_rgb(245, 245, 242))

                curTile.draw(self.win)
                

            if (change[0][2] == 2):
                # change piece??
                curPiece = self.chessBoard.getThing(x,y,2)
                prevPiece = self.prevState.getThing(x,y,2)
                print(curPiece, prevPiece)
                if prevPiece != None:
                    prevPiece.undraw()
                if curPiece != None:
                    curPiece.undraw()
                    curPiece.draw(self.win)
                    

        # change the prev state to cur state
        self.prevState = self.chessBoard.copy()

if __name__ == '__main__':
    cGUI = ChessGUI()
    cGUI.updatePrompt("hello there my name is alison this is a test because i don't know what else to say hello hello everything is awesome no i'm not qutoing a movieeee")
    cGUI.updateWin()

    while not cGUI.isDone():
        cGUI.update()
    
    

    

    
