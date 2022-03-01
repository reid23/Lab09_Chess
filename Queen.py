# Queen Chess Piece (Alison)
from ChessPiece import ChessPiece # remove later

class Queen (ChessPiece):
    """Defines a Queen chess piece for a chess game"""

    def __init__(self, color, pos,startPos):
        """Creates a new Queen!

        Args:
            color (bool): True if white, False if black
            pos (tuple): initial position of the pawn
        """
        super().__init__(color, pos,startPos)
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
                move = (pos[0]+rel[0]*i, pos[1]+rel[1]*i) #convert to absolute position
                # if both withiin bounds and overtakes an empty or diifferent color piece
                if self.withinBounds(move):
                    if gameState[move[0]][move[1]][2] != None:
                        color = gameState[move[0]][move[1]][2].color
                        if color != self.color:
                            if (not self.checkCheck(gameState, pos, move, self.color)):
                                moves.append(move)
                        break # no need to continue in this direction
                    
                    # if move does not cause a checkmate
                    if (not self.checkCheck(gameState, pos, move, self.color)):
                        moves.append(move)
        
        return moves



def main():
    # testing queen
    win = GraphWin("testing", 800,700)

    q1 = Queen(True, (1,1))
    q1.draw(win)

    print(q1.calculatePossibleMoves(True, (2,2)))
    

if __name__ == "__main__": 
    from graphics import * 
    main()
