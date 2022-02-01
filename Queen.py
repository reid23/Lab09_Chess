# Queen Chess Piece
from ChessPiece import ChessPiece # remove later

class Queen (ChessPiece):
    """Defines a Queen chess piece for a chess game"""

    def __init__(self, color, pos):
        """Creates a new Queen!

        Args:
            color (bool): True if white, False if black
            pos (tuple): initial position of the pawn
        """
        super().__init__(color, pos)
        self.rules = ((0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0))
             
    def calculatePossibleMoves(self, gameState, pos):
        """Calculates all the possible moves given the game state. Returns a list of tuples representing possible moves.

        Args:
            gameState (list): a 8x8x3 matrix [rectangle object, litUp, chessPiece object]
            pos (tuple): current position
        """

        moves = []
        for rel in self.rules:
            for i in range(1,8): # as far as the Queen wants bc powerful!
                move = (pos[0]+rel[0]*i, pos[1]+rel[1]*i) 
                # if move does not cause a checkmate, is within bounds, and will not overlap w/ same color piece
                color = not self.color # gameState[move[0]][move[1]][2].getColor() # will bring this back once merged :>
                if (not self.checkCheck(gameState, pos, move)) and self.withinBounds(move) and color != None and color != self.color:
                    moves.append(move)
        return moves


def main():
    # testing Pawn
    q1 = Queen(True, (1,1))
    print(q1.calculatePossibleMoves(True, (2,2)))
    

if __name__ == "__main__": main()




    

    


