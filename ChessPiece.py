# A general chess piece (Reid)
from graphics import Image, Point

class ChessPiece(Image):
    """Defines a general chess piece for a chess game"""

    def __init__(self, color: bool, pos: tuple, startPos : tuple):
        """Creates a new Chess Piece

        Args:
            color (bool): True if white, False if black
            pos (tuple): initial position of the pawn
        """
        super().__init__(Point(pos[0]*10+5, pos[1]*10+5), f"images/{self.__class__.__name__}{'W' if color else 'B'}.png")
        self._color = color
        self._curPos = pos
        self._startPos = startPos
        self.rules = []
        self.image = 0

    def _move(self, x, y, absolute=True):
        if absolute:
            dx, dy = x-self.anchor.getX(), y-self.anchor.getY()
        else:
            dx, dy = x, y
        self.anchor.move(dx, dy)

    def copy(self):
        """returns a copy of the peice

        Returns:
            type(self): a copy of self.
        """
        return type(self)(color=self._color, pos=self._curPos, startPos=self._startPos)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._color}, {self._curPos})"

    def __str__(self) -> str:
        return f"{'White' if self._color else 'Black'} {self.__class__.__name__}"
    
    def __hash__(self) -> int:
        """hash yoself. just so we can put peices into a set

        Returns:
            int: the unique hash representing this object
        """
        return hash(repr(self))
    
    def __eq__(self, other) -> bool:
        """equality implementation for chess pieces

        Args:
            other (ChessPiece): the other piece

        Returns:
            bool: whether the pieces are identical
        """
        return isinstance(other, type(self)) and self._color==other.color and self._curPos==other.curPos
    
    def setPos(self, oldPos: tuple, newPos: tuple):
        self._move((newPos[0]-oldPos[0])*10, (newPos[1]-oldPos[1])*10, False)
        self._curPos = (int(newPos[0]), int(newPos[1]))
    
    @property
    def curPos(self) -> tuple:
        """shouldn't be used directly, just enables doing ChessPiece.curPos to get the position without violating encapsulation (ie this is read-only)"""
        return self._curPos
    
    @property
    def color(self) -> bool:
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
        return (pos[0]+mov[0], pos[1]+mov[1])
        

    def calculatePossibleMoves(self, gameState: list, pos: tuple) -> list:
        """Calculates all the possible moves given the game state. Returns a list of tuples representing possible moves.

        Args:
            gameState (list): a 8x8x3 matrix [rectangle object, litUp, chessPiece object]
            pos (tuple): current position
        Returns:
            list: a list of the tuples representing all possible moves.
        """
        return []

    
    def checkCheck(self, gameState: list, pos: tuple, move: tuple, color: bool) -> bool:
        """Verifies if move will cause a checkmate. Returns True if induces a checkmate, False if not.

        Args:
            gameState (list): a 8x8x3 matrix [rectangle object, litUp, chessPiece object]
            pos (tuple (a, b) where a and b are int): Represents a possible position after a move
            move (tuple (a, b) where a and b are int): Represents a possible position after a move
            color (bool): the color of the current piece being moved. If own king is being 
        """
        
        # will bring the below back once everything is merged
        newGameState = self._empty(8,8,3)

        for x in range(3):
            for i in range(8):
                for j in range(8):
                    if (newGameState[i][j][x] != None and x != 1):
                        newGameState[i][j][x] = gameState[i][j][x].copy()
                    else:
                        newGameState[i][j][x] = gameState[i][j][x]

        # replace with moved chess piece
        newGameState[move[0]][move[1]][2] = newGameState[pos[0]][pos[1]][2]
        newGameState[pos[0]][pos[1]][2] = None
        
        curColor = newGameState[move[0]][move[1]][2].color
            
        for x in range(8):
            for y in range(8):
                if newGameState[x][y][2] == None or newGameState[x][y][2].color == color:
                    continue #don't care about same color piece loL
                for move1 in newGameState[x][y][2].getAllMoves(newGameState, (x,y)): # filtered for bounds already
                    if newGameState[move1[0]][move1[1]][2] == None:
                        continue
                    nextColor = newGameState[move1[0]][move1[1]][2].color
                    # make sure that own king will not be in a checkmate
                    if newGameState[move1[0]][move1[1]][2].getType() == "King" and nextColor == color:
                        return True
        
        return False


    @staticmethod
    def _empty(*shape: int, initialVal=None) -> list:
        """generates a list with the given shape, whose values are initialVal

        Args:
            *shape (int, multiple values accepted): integers describing the length of each dimension of the requested list.
            initialVal (any, optional): the values in the list. Defaults to None.

        Returns:
            list: the requested list
        """
        shape=list(shape)
        shape.reverse()
        output=(initialVal,)
        for i in shape:
            output=output*i
            output=(output,)
        return ChessPiece._convert(output[0]) #convert to list, and take out extra dimension from previous line on last iteration
    
    @staticmethod
    def _convert(t): #recursion go brrrrr
        """converts a tuple to a list recursively

        Args:
            t (tuple): the input tuple

        Returns:
            list: the same thing as the input, but as a list
        """
        if isinstance(t, tuple):
            return list(ChessPiece._convert(i) for i in t)
        else:
            return t

    def getAllMoves(self, gamestate: list, pos: tuple) -> list:
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
    
    def getType(self) -> str:
        """[summary]

        Returns:
            str: string of thing
        """
        return self.__class__.__name__
