# Pawn Chess Piece
from ChessPiece import ChessPiece # remove later

class Pawn (ChessPiece):
    def __init__(self, color, pos):
        """Creates a new Pawn

        Args:
            color (bool): True if white, False if black
            pos (tuple): initial position of the pawn
        """
        super().__init__(color, pos)
        if color: # white
            self.rules = [(0,1),(1,1),(-1,1),(0,2)]
        else:
            self.rules = [(0,-1),(1,-1),(-1,-1),(0,-2)]
             
    def calculatePossibleMoves(self, gameState, pos):
        """Calculates all the possible moves given the game state. Returns a list of tuples representing possible moves.

        Args:
            gameState (list): a 8x8x3 matrix [rectangle object, litUp, chessPiece object]
            pos (tuple): current position
        """

        moves = []
        for rel in self.rules:
            move = (pos[0]+rel[0], pos[1]+rel[1]) 
            # if move does not cause a checkmate, is within bounds, and will not overlap w/ same color piece
            color = not(self.color) # gameState[move[0]][move[1]][2].getColor() # will bring this back once merged :>
            if not(self.checkCheck(gameState, pos, move)) and self.withinBounds(move) and color != None and color != self.color:
                moves.append(move)
        return moves

    def getType(self):
        """Returns type of chess piece as a string
        """
        return "Pawn"
    

def main():
    # testing Pawn
    p1 = Pawn(True, (1,1))
    print(p1.calculatePossibleMoves(True, (0,0)))

if __name__ == "__main__": main()




    

    


