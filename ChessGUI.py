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
        # for x in range(8):
        #     for y in range(8):
        #         self.chessBoard.getThing(x,y,0).draw(self.win)
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

        for i in range(8):
            Text(Point(10*i+5, 82.5), chr(i+ord('a'))).draw(self.win)
        for i in range(8):
            Text(Point(82.5, 10*i+5), i+1).draw(self.win)

        self.done = False

        self.updatePrompt("ghello there my name is alison this is a test because i don't know what else to say hello hello everything is awesome no i'm not qutoing a movieeee")

        self.curPlayer = True # true for white, start with white

        self.resetGame()
        self.prevState = self.chessBoard.copy()
        self.updateWin()

        # MOVE STATES
        self.hasSelected = False

        self.curLitUp = []

        self.clickedLitPiece = False

    
    def resetGame(self):
        """Draws the starting board, resets the game
        """

        for x in range(8):
            for y in range(8):
                piece = self.chessBoard.getThing(x, y, 2)
                if piece != None:
                    piece.undraw()
                self.chessBoard.getThing(x, y, 0).undraw()
        
        # copyBoard = self.chessBoard.copy()
        self.chessBoard.reset()
        self.prevState = self.chessBoard.copy()
        # self.drawDiff(self.chessBoard-copyBoard, True)

        for x in range(8):
            for y in range(8):
                self.chessBoard.getThing(x, y, 0).undraw()
                self.chessBoard.getThing(x, y, 0).draw(self.win)
                piece = self.chessBoard.getThing(x, y, 2)
                if piece != None:
                    # print(piece.curPos)
                    piece.undraw()
                    piece.draw(self.win)
        
        self.curPlayer = True
        self.hasSelected = False
        self.clickedLitPiece = False


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
        for j in range(8):
            for i in range(8):
                # print(self.prevState.getThing(i,7-j,2), "(", id(self.prevState.getThing(i,7-j,2)), ")", end=" ")
                print(self.prevState.getThing(i,7-j,2),end=" ")
            print()

        print("------")
        for j in range(8):
            for i in range(8):
                # print(self.chessBoard.getThing(i,7-j,2), "(", id(self.chessBoard.getThing(i,7-j,2)), ")",end=" ")
                print(self.chessBoard.getThing(i,7-j,2), end=" ")
            print()

        print(self.chessBoard-self.prevState)
        self.drawDiff(self.chessBoard-self.prevState)
        
        self.win.update()
        
    
    def coordClicked(self, pt):
        self.prevState = self.chessBoard.copy()
        # returns tuple of grid cooord that has been pressed
        # TODO IMPLEMENT
        print("=======", self.curPlayer)
        curX = pt.getX()
        curY = pt.getY()
        if (curX < 0 or curY < 0 or curX > 80 or curY > 80):
            return False
        curX = int(curX/10)
        curY = int(curY/10)
        print("------",curX,curY)

        curPos = (curX, curY)
        
        if curPos in self.curLitUp:
            self.clickedLitPiece = True
            # move that piece there!
            self.chessBoard.putThing(self.chessBoard.getThing(self.origPiecePos[0],self.origPiecePos[1], 2), curPos, 'piece')
            self.chessBoard.getThing(self.origPiecePos[0],self.origPiecePos[1], 2).setPos(self.origPiecePos,curPos)
            self.chessBoard.putThing(None, self.origPiecePos, 'piece')
            for pos in self.curLitUp:
                self.chessBoard.putThing(False, pos, 'lit')
            self.curLitUp = []
            return True
        elif self.hasSelected:
            for pos in self.curLitUp:
                self.chessBoard.putThing(False, pos, 'lit')
            self.curLitUp = []
        
        if self.chessBoard.getThing(curX,curY,2) == None:
            self.hasSelected = False
            if self.clickedLitPiece: # already clicked a lit piece
                for pos in self.curLitUp:
                    self.chessBoard.putThing(False, pos, 'lit')
            self.curLitUp = []
            return False
        if self.chessBoard.getThing(curX,curY,2).color == self.curPlayer:
            self.hasSelected = True
            self.origPiecePos = curPos
            if self.clickedLitPiece: # already clicked a lit piece
                for pos in self.curLitUp:
                    self.chessBoard.putThing(False, pos, 'lit')
            self.curLitUp = self.chessBoard.lightUpSquares((curX,curY))
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
            # next step of turn is to choose square... idk just a progression of steps for turn
            # 1) select piece to move
            # 2) select place to move that piece
            # IF THE COORD CLICKED IS NOT YOUR PIECE, DO NOT USE IT
            print("YO COORD CLICKED!")

            print("has selected a piece:", self.hasSelected)
            print("has clicked a piece:", self.clickedLitPiece)
            print("cur player:", self.curPlayer)
            if (self.hasSelected and self.clickedLitPiece):
                self.hasSelected = False
                self.clickedLitPiece = False
                self.curPlayer = not self.curPlayer
                print("CHANGED PLAYER")
        else:
            print("has selected a piece:", self.hasSelected)
            print("has clicked a piece:", self.clickedLitPiece)
            print("cur player:", self.curPlayer)
            for pos in self.curLitUp:
                self.chessBoard.putThing(False, pos, 'lit')
            self.hasSelected = False

        
        
        self.updateWin()

    def isDone(self):
        """Returns if window should be closed

        Returns:
            [bool]: true if done, false if not
        """
        return self.done
    
    def drawDiff(self, changes, start=False):   
        if start:
            # redraw the entire base   
            for x in range(8):
                for y in range(8):
                    prevTile = self.prevState.getThing(x,y,0)
                    curTile = self.chessBoard.getThing(x,y,0)
                    prevTile.undraw()
                    curTile.undraw()

                    if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                        curTile.setFill('grey')
                    else:
                        curTile.setFill(color_rgb(245, 245, 242))

                    curTile.draw(self.win)
                    
        for change in changes:
            x = change[0][0]
            y = change[0][1]
            print(change,end="  ")
            print("===",x,y, end = "     ")
            print(self.prevState.getThing(x,y,change[0][2]))


            if (change[0][2] == 1):
                # curTileOn = self.chessBoard.getThing(x,y,1)
                prevTile = self.prevState.getThing(x,y,0)
                curTile = self.chessBoard.getThing(x,y,0)
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
                

            # if (change[0][2] == 2):
                #     # change piece??
                print("____DFSDL:FKJSDL:KFJSDL:KFJL:SDKFKSDLF")
                curPiece = self.chessBoard.getThing(x,y,2)
                prevPiece = self.prevState.getThing(x,y,2)
                    # print(curPiece, prevPiece)
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
    
    

    

    
