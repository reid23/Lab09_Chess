# Chess GUI (Alison)
from graphics import *
from ChessBoard import Board
from Button import Button
from Text import getSnippet, loadWikiWords

class ChessGUI:
    """GUI for a chess game"""

    def __init__(self):
        """Creates a new ChessGUI

        Args:
            chessBoard (ChessBoard): holds the info of a chess game
        """
        # board
        self.win = GraphWin("Chess: the ultimate game of wit", 800, 600, autoflush = False)
        self.win.setBackground("white")
        self.win.setCoords(-10,-30,150,90)
        self.chessBoard = Board()

        # buttons
        self.quitButton = Button(Point(115,-8), 50, 8, "Quit", self.win)
        self.quitButton.activate()
        self.replayButton = Button(Point(115,-20), 50, 8, "Reset", self.win)
        self.replayButton.activate()

        # title on the side
        title = Text(Point(115, 65), "chess") 
        title.setSize(36)
        title.draw(self.win)
        subtitle = Text(Point(115, 57), "a game of wit") 
        subtitle.setSize(23)
        subtitle.draw(self.win)
        self.words=loadWikiWords()
        self.desc = Text(Point(115, 30), '')
        self.desc.setSize(15)
        self.desc.draw(self.win)

        # prompt box
        promptBox = Rectangle(Point(0,-24),Point(80,-4))
        promptBox.setFill('lightgrey')
        promptBox.setOutline("lightgrey")
        promptBox.draw(self.win)
        self.prompt = Text(Point(40,-14), "Prompt goes here")
        self.prompt.draw(self.win)

        # draw the numbers and letters for coords
        for i in range(8):
            Text(Point(10*i+5, 82.5), chr(i+ord('a'))).draw(self.win)
        for i in range(8):
            Text(Point(82.5, 10*i+5), i+1).draw(self.win)

        self.done = False
        self.curPlayer = True # true for white, start with white

        self.resetGame()
        self.prevState = self.chessBoard.copy()
        self.updateWin()
        self.desc.setText("\"a board game of strategic skill\nfor two players, played on a\ncheckered board. Each player\nbegins the game with sixteen\npieces that are moved and\nused to capture opposing\npieces according to precise\nrules. The object is to put the\nopponent's king under a direct\nattack from which escape is\nimpossible (checkmate).\"")



        # MOVE STATES
        self.hasSelected = False
        self.clickedLitPiece = False
        self.curLitUp = []

        self.newMessage = ""

    
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
        self.prevState = self.chessBoard.copy()

        for x in range(8):
            for y in range(8):
                self.chessBoard.getThing(x, y, 0).undraw()
                self.chessBoard.getThing(x, y, 0).draw(self.win)
                piece = self.chessBoard.getThing(x, y, 2)
                if piece != None:
                    piece.undraw()
                    piece.draw(self.win)
        
        self.curPlayer = True
        self.hasSelected = False
        self.clickedLitPiece = False
        self.newMessage = "Welcome to a new game of chess! It is White's turn."
        self.updatePrompt("Welcome to a new game of chess! It is White's turn.")

    @staticmethod
    def textWrap(text, width, center=True):
        """wraps given text to limit line size to $width, and optionally centers the text in the lines (default left justified)

        Args:
            text (str): the input string to wrap
            width (int): the line length limit (the max width of the text block)
            center (bool, optional): whether to center the text. Defaults to True.

        Returns:
            str: the wrapped text
        """
        # there's a whole library for text wrapping
        # but noooo we can't use it
        # have you even read george orwell's 1984?!?! /s
        # 
        # seriously though :( text is pain
        # like time zone stuff
        # implementing it from scratch might give a deeper understanding but
        # I'm willing to bet it'll also give me depression

        # split into words, but don't remove the spaces
        text=text.replace(' ', ' SplitHere®©™').split("SplitHere®©™") #break into words


        lines=[''] #init lines, which will be [line_1, line_2, line_3, ..., line_n]
        
        for word in text:
            if width-len(lines[-1]) >= len(word): #if there's space left in the line
                lines[-1] = lines[-1]+word #add the word to the line
            else:
                lines.append(word) #else add the word to the next line
        
        if center:
            for counter, line in enumerate(lines):
                lines[counter] = line.center(width) #center each line using the str.center method, just centering to width

        return '\n'.join(lines) #convert the list of lines to a string with actual newline chars
        






    def updatePrompt(self, msg : str) -> None:
        """updates the prompt on the GUI

        Args:
            msg (str): new message for prompt box
        """
        self.chessBoard.checkCzechCheque(msg)
        s=ChessGUI.textWrap(msg, width=65)
        self.prompt.setText(s)

    def updateWin(self):
        self.drawDiff(self.chessBoard-self.prevState)
        self.desc.setText(ChessGUI.textWrap(getSnippet(self.words), 40))
        self.win.update()
        
    
    def coordClicked(self, pt):
        curX = pt.getX()
        curY = pt.getY()
        self.newMessage = "It is White's turn! Click a white piece to move." if self.curPlayer else "It is Black's turn! Click a black piece to move."
        if (curX < 0 or curY < 0 or curX > 80 or curY > 80):
            return False
        curX = int(curX/10)
        curY = int(curY/10)

        curPos = (int(curX), int(curY)) # current tile clicked
        
        if curPos in self.curLitUp: # if the tile is lit up
            self.clickedLitPiece = True # we can mve the piece!
            # move that piece there!
            prevPiece = self.chessBoard.getThing(curPos[0],curPos[1], 2)
            self.chessBoard.putThing(self.chessBoard.getThing(self.origPiecePos[0],self.origPiecePos[1], 2), curPos, 'piece')
            self.chessBoard.getThing(self.origPiecePos[0],self.origPiecePos[1], 2).setPos(self.origPiecePos,curPos)
            self.chessBoard.putThing(None, self.origPiecePos, 'piece')

            if prevPiece == None: # if nothing there, just print message that piece was mvoed
                self.newMessage = "White" if self.curPlayer else "Black"
                self.newMessage += f" moved {self.chessBoard.getThing(*curPos, 2).__class__.__name__} to {chr(ord('a')+curPos[0])}{str(curPos[1] + 1)}."
            else: # otherwise, a piece was captured. Print what happened.
                self.newMessage = "White's " if self.curPlayer else "Black's "
                self.newMessage += self.chessBoard.getThing(curPos[0],curPos[1], 2).getType() + " captured "
                self.newMessage += "Black's " if self.curPlayer else "White's "
                self.newMessage += prevPiece.getType() + " at " + chr(ord('a')+curPos[0]) + str(curPos[1] + 1) + "."
            
            # reset all lit up tiles
            for pos in self.curLitUp: 
                self.chessBoard.putThing(False, pos, 'lit')
            
            self.curLitUp = [] # reset cur lit up list

            # upgrade pawn to queen if at the end of the board
            curPiece = self.chessBoard.getThing(curPos[0], curPos[1],2)
            if (curPiece.getType() == 'Pawn' and (curPos[1] == 0 or curPos[1] == 7)):
                self.chessBoard.changeToQueenAt(curPos)
                self.chessBoard.putThing(None, self.origPiecePos, 'piece')
                self.newMessage += " The pawn has reached the opposing end and has been upgraded as a result!"
            return True # finish. user did interact with board, so return true
        
        elif self.hasSelected: # otherwise if has selected a piece to move but chose somewhere else...
            for pos in self.curLitUp: # reset all tiles
                self.chessBoard.putThing(False, pos, 'lit')
            self.curLitUp = []
        
        if self.chessBoard.getThing(*curPos,2) == None: # not a valid move
            if self.hasSelected:
                self.newMessage = "That is not a valid move."
                self.newMessage += " Please click on a white piece." if self.curPlayer else " Please click on a black piece."
            self.hasSelected = False
            if self.clickedLitPiece: # already clicked a lit piece
                for pos in self.curLitUp: # reset the board
                    self.chessBoard.putThing(False, pos, 'lit')
            self.curLitUp = []
            return False 

        if self.chessBoard.getThing(curX,curY,2).color == self.curPlayer:
            # has selected a piece of the correct color
            self.hasSelected = True
            self.origPiecePos = curPos
            self.newMessage = "White " if self.curPlayer else "Black "
            self.newMessage += "has selected " + self.chessBoard.getThing(curPos[0],curPos[1], 2).getType() + " at " + chr(ord('a')+curPos[0]) + str(curPos[1] + 1) + " to move."
            if self.clickedLitPiece: # already clicked a lit piece
                for pos in self.curLitUp:
                    self.chessBoard.putThing(False, pos, 'lit')
            self.curLitUp = self.chessBoard.lightUpSquares((curX,curY))
            if len(self.curLitUp) == 0:
                self.newMessage = "That piece does not have any legal moves. Please pick another piece"
            else:
                self.newMessage += " Please select a move from the indicated options."
            # self.updatePrompt(self.newMessage) # update the prompt!
            return True

        return False
        # base case
        

    def update(self):
        """updates the board

        Returns:
            [bool]: Returns true if done
        """
        pt = self.win.getMouse()
        cont = True
        end, winner = self.chessBoard.checkCheckmate()
        if end: # if checkmate detected
            if winner: # if white won
                self.newMessage = "White won! Black king is in checkmate."
            else: # black won
                self.newMessage = "Black won! White king is in checkmate."
            self.updatePrompt(self.newMessage) # update the prompt bx
            cont = False # finish

        if self.quitButton.clicked(pt): # if quit button pressed
            self.done = True
            self.win.close()
            return
        elif self.replayButton.clicked(pt): # if replay button pressed
            self.done = False
            self.resetGame()
        elif cont and self.coordClicked(pt): # as long as no checkmate is detected, continue with coord clicked method
            # next step of turn is to choose square... just a progression of steps for turn
            # 1) select piece to move (if the coord clicked is not your piece, do not use it)
            # 2) select place to move that piece.
            if (self.hasSelected and self.clickedLitPiece):
                self.hasSelected = False
                self.clickedLitPiece = False
                self.curPlayer = not self.curPlayer # change the player!
                if self.curPlayer:
                    self.updatePrompt(self.newMessage+" It is White's turn!")
                else:
                    self.updatePrompt(self.newMessage+" It is Black's turn!")
            else:
                self.updatePrompt(self.newMessage)
        else: # base case
            self.updatePrompt(self.newMessage)
            for pos in self.curLitUp:
                self.chessBoard.putThing(False, pos, 'lit')
            self.hasSelected = False

        end, winner = self.chessBoard.checkCheckmate() # well check again ig
        if end:
            if winner:
                self.newMessage = "White won! Black king is in checkmate."
            else:
                self.newMessage = "Black won! White king is in checkmate."
            # self.updatePrompt(self.newMessage)
            cont = False
        
        self.updateWin() # update the board! get diff from previous state, set previous state to current state

    def isDone(self):
        """Returns if window should be closed

        Returns:
            [bool]: true if done, false if not
        """
        return self.done
    
    def drawDiff(self, changes, start=False):
        """Draws the difference of the board given a list of the changes

        Args:
            changes (list): list of tuples of coordinates to change
            start (bool, optional): Determines if first draw of the game. Defaults to False.
        """
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
                    
        for change in changes: # for each change
            x = change[0][0]
            y = change[0][1]

            prevTile = self.prevState.getThing(x,y,0)
            curTile = self.chessBoard.getThing(x,y,0)
            prevTile.undraw() # undraw stuff
            curTile.undraw()

            if change[0][2] == 1 and change[1]:
                curTile.setFill(color_rgb(149, 222, 146))
            else:
                if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                    curTile.setFill('grey')
                else:
                    curTile.setFill(color_rgb(245, 245, 242))

            curTile.draw(self.win)

            # redraw pieces
            curPiece = self.chessBoard.getThing(x,y,2)
            prevPiece = self.prevState.getThing(x,y,2)
            if prevPiece != None: # undraw previous piece
                prevPiece.undraw()
            if curPiece != None:
                curPiece.undraw()
                curPiece.draw(self.win)

        # change the prev state to cur state
        self.prevState = self.chessBoard.copy()

if __name__ == '__main__':
    # unit testing yeet
    cGUI = ChessGUI()
    cGUI.updatePrompt("haha I changed your long string of text now it's this other long useless string of text wow incredible thislabhaspushedmetotheedjeofsanity <- that was reid. now it is alison. I will continue this very long string of text because it is my duty to break the expectations of this lab for relatively short lines of code muahahaha")
    cGUI.updateWin()

    while not cGUI.isDone():
        cGUI.update()
    

    

    
