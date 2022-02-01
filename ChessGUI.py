from graphics import *
from ChessBoard import Board


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
        
        return pieces

    

    
