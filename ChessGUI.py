from graphics import *
from ChessBoard import Board
from Pawn import Pawn
from Queen import Queen
from Knight import Knight

class ChessGUI:
    """GUI for a chess game"""

    def __init__(self, chessBoard):
        """Creates a new ChessGUI

        Args:
            chessBoard (ChessBoard): holds the info of a chess game
        """
        self.chessBoard = chessBoard
        self.startingPieces = self._createStartingChessPieces()

        self.game
    
    def drawStartBoard(self):
        """Draws the starting board, resets the game
        """
        self.chessBoard = Board()

    def _createStartingChessPieces(self):
        """Returns a list of the starting chess pieces and their positions
        """
        pieces = []
        # add all pieces
        for i in range(8):
            pieces.append(Pawn(True, (i,1)))
            pieces.append(Pawn(False, (i,6)))

        pieces.append(Knight(True, (1,0)))
        pieces.append(Knight(True, (6,0)))
        pieces.append(Knight(False, (1,7)))
        pieces.append(Knight(False, (6,7)))

        # pieces.append(Rook(True, (0,0)))
        # pieces.append(Rook(True, (7,0)))
        # pieces.append(Rook(False, (0,7)))
        # pieces.append(Rook(False, (7,7)))

        # pieces.append(Bishop(True, (2,0)))
        # pieces.append(Bishop(True, (5,0)))
        # pieces.append(Bishop(False, (2,7)))
        # pieces.append(Bishop(False, (5,7)))

        # pieces.append(King(True, (4,0)))
        # pieces.append(King(False, (4,7)))
        pieces.append(Queen(True, (3,0)))
        pieces.append(Queen(False, (3,7)))
        
        return pieces

    

    
