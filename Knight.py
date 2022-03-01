# Knight Chess Piece (Alison)
from ChessPiece import ChessPiece 

class Knight (ChessPiece):
    """Defines a Knight chess piece for a chess game"""

    def __init__(self, color, pos, startPos):
        """Creates a new Knight!

        Args:
            color (bool): True if white, False if black
            pos (tuple): initial position of the pawn
        """
        super().__init__(color, pos, startPos)
        self.rules = ((2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2))
             
    def calculatePossibleMoves(self, gameState, pos):
        """Calculates all the possible moves given the game state. Returns a list of tuples representing possible moves.

        Args:
            gameState (list): a 8x8x3 matrix [rectangle object, litUp, chessPiece object]
            pos (tuple): current position
        """

        moves = []
        for rel in self.rules:
            move = self._toGlobal(pos, rel)
            # if both withiin bounds and overtakes an empty or diifferent color piece
            if self.withinBounds(move):
                if gameState[move[0]][move[1]][2] != None:
                    color = gameState[move[0]][move[1]][2].color
                    if color == self.color:
                        continue # just break

                # if move does not cause a checkmate
                if (not self.checkCheck(gameState, pos, move, self.color)):
                    moves.append(move)
        
        return moves

    def getAllMoves(self, gameState, pos):
        """Returns all possible moves

        Args:
            gameState: the current game state, a list of shape (8, 8, 3)
            pos (tuble): current position

        Returns:
            list of moves (filters out of bounds)
        """
        moves = []
        for rel in self.rules:
            move = (pos[0]+rel[0], pos[1]+rel[1]) 
            # if move is within bounds
            if self.withinBounds(move):
                moves.append(move)

        return moves
        
def main():
    # testing knight
    kn1 = Knight(True, (1,1))
    print(kn1.calculatePossibleMoves([[[True]*8]*8]*3, (5,5)))
    # [(7, 6), (7, 4), (6, 7), (6, 3), (3, 6), (3, 4), (4, 7), (4, 3)]
    # looks good?

if __name__ == "__main__": main()




    

    


