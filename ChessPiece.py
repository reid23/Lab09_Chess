# A general chess piece
from graphics import Image, Point

class ChessPiece(Image):
    """Defines a general chess piece for a chess game"""

    def __init__(self, color: bool, pos: tuple):
        """Creates a new Chess Piece

        Args:
            color (bool): True if white, False if black
            pos (tuple): initial position of the pawn
        """
        super().__init__(Point(pos[0]*10+5, pos[1]*10+5), f"images/{self.__class__.__name__}{'W' if color else 'B'}.png")
        self._color = color
        self._startPos = pos
        self.rules = []
        self.image = 0
    
    def copy(self):
        return type(self)(color=self._color, pos=self._startPos)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self._color}, {self._startPos})"

    def __str__(self):
        return f"{'White' if self._color else 'Black'} {self.__class__.__name__}"
    
    def __hash__(self):
        return hash(repr(self))
    
    def __eq__(self, other):
        return isinstance(other, type(self)) and self._color==other.color
    
    @property
    def startPos(self):
        """shouldn't be used directly, just enables doing ChessPiece.startPos to get the position without violating encapsulation (ie this is read-only)"""
        return self._startPos
    
    @property
    def color(self):
        """shouldn't be used directly, just enables doing ChessPiece.color to get the color without violating encapsulation (ie this is read-only)"""
        return self._color

    @staticmethod
    def _toGlobal(pos: tuple, mov: tuple) -> tuple:
        """adds the arguments elementwise to give the end position of a relative movement $mov from an absolute starting position $pos

        Args:
            pos (list|tuple): global initial position
            mov (list|tuple): relative movement

        Returns:
            tuple: the end global position
        """
        return tuple(map(sum, zip(pos, mov)))
        #non-vectorized expansion:
        #for i in range(len(pos)):
        # output[i] = pos[i] + mov[i]
        #basically just adds elementwise

    def calculatePossibleMoves(self, gameState: list, pos: tuple) -> list:
        """Calculates all the possible moves given the game state. Returns a list of tuples representing possible moves.

        Args:
            gameState (list): a 8x8x3 matrix [rectangle object, litUp, chessPiece object]
            pos (tuple): current position
        Returns:
            list: a list of the tuples representing all possible moves.
        """
        return []

    # TODO: MOVE INTO CHESS BOARD BC CIRCULAR IMPORT :>
    def checkCheck(self, gameState: list, pos: tuple, move: tuple, color: bool) -> bool:
        """Verifies if move will cause a checkmate. Returns True if induces a checkmate, False if not.

        Args:
            gameState (list): a 8x8x3 matrix [rectangle object, litUp, chessPiece object]
            pos (tuple (a, b) where a and b are int): Represents a possible position after a move
            move (tuple (a, b) where a and b are int): Represents a possible position after a move
            color (booll): the color of the current piece being moved. If own king is being 
        """

        # will bring the below back once everything is merged
        newGameState = gameState.getGameState('pieces') # implemented~
        # replace with moved chess piece
        newGameState[move[0]][move[1]][2] = newGameState[pos[0]][pos[1]][2]
        newGameState[pos[0]][pos[1]][2] = None
        curColor = newGameState[move[0]][move[1]][2].color
        
        for x in range(8):
            for y in range(8):
                for move in newGameState[x][y][2].getAllMoves(gameState, (x,y)): # filtered for bounds already
                    nextColor = newGameState[move[0]][move[1]][2].color
                    # make sure that own king will not be in a checkmate
                    # if isinstance(newGameState[move[0]][move[1]][2].isInstance(), King) and nextColor == color:
                        # return True
        
        return False

    def getAllMoves(self, pos):
        """Returns a list of tuples of moves from given position

        Args:
            pos (tuple (a,b)): Represents current position
        """
        return []

    def withinBounds(self, move: tuple) -> bool:
        """Verifies if move is within the board. Returns True if within bounds, False if not.

        Args:
            move (tuple (a, b) where a and b are int): Represents a possible move
        """
        return 0 <= move[0] <= 7 and 0 <= move[1] <= 7 
