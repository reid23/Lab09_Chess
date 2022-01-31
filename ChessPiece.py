# Chess Piece

class ChessPiece:
    """Defines a general chess piece for a chess game"""

    def __init__(self, color=None, pos=()):
        """Creates a new Chess Piece

        Args:
            color (bool): True if white, False if black
            pos (tuple): initial position of the pawn
        """

        self.color = color
        self.startPos = pos
        self.rules = [] # TODO: lambda or list

    def calculatePossibleMoves(self, gameState, pos):
        """Calculates all the possible moves given the game state. Returns a list of tuples representing possible moves.

        Args:
            gameState (list): a 8x8x3 matrix [rectangle object, litUp, chessPiece object]
            pos (tuple): current position
        """
        return []

    def checkCheck(self, gameState, pos, move):
        """Verifies if move will cause a checkmate. Returns True if induces a checkmate, False if not.

        Args:
            gameState (list): a 8x8x3 matrix [rectangle object, litUp, chessPiece object]
            pos (tuple (a, b) where a and b are int): Represents a possible position after a move
            move (tuple (a, b) where a and b are int): Represents a possible position after a move
        """
        # will bring the below back once everything is merged
        # newGameState = gameState.getGameState('pieces') # implemented~
        # replace with moved chess piece
        # newGameState[move[0]][move[1]][2] = newGameState[pos[0]][pos[1]][2]
        # newGameState[pos[0]][pos[1]][2] = None
        
        # for x in range(8):
        #     for y in range(8):
        #         for move in newGameState[x][y][2].getAllMoves():
        #             if not(self.withinBounds(move)):
        #                 continue
        #             if newGameState[move[0]][move[1]][2].getType() == "King" and newGameState[x][y][2].getColor() != newGameState[x][y][2].getColor():
        #                 return True
        
        return False


    def getAllMoves(self, pos):
        """Returns a list of tuples of moves from given position

        Args:
            pos (tuple (a,b)): Represents current position
        """
        return []

    def withinBounds(self, move):
        """Verifies if move is within the board. Returns True if within bounds, False if not.

        Args:
            move (tuple (a, b) where a and b are int): Represents a possible move
        """
        return 0 <= move[0] <= 7 and 0 <= move[1] <= 7 

    def getColor(self):
        """Returns color (True if white, False if black, None if empty)
        """
        return self.color

    def getType(self):
        """Returns type of chess piece as a string
        """
        return "None"





    

    


