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

                color = gameState[move[0]][move[1]][2].color
                isEmptyOrDiffColor = color == None or color != self.color
                # if both withiin bounds and overtakes an empty or diifferent color piece
                if self.withinBounds(move) and isEmptyOrDiffColor:
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
            for i in range(1,8): # as far as the Queen wants bc powerful!
                move = (pos[0]+rel[0]*i, pos[1]+rel[1]*i) 
                # if within bounds
                if self.withinBounds(move):
                    moves.append(move)
        
        return moves



def main():
    # testing Pawn
    win = GraphWin("testing", 800,700)

    q1 = Queen(True, (1,1))
    q1.draw(win)

    print(q1.calculatePossibleMoves(True, (2,2)))
    

if __name__ == "__main__": 
    from graphics import * 
    main()




    

    


