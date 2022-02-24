# Pawn Chess Piece
from ChessPiece import ChessPiece # remove later

class Pawn(ChessPiece):
    def __init__(self, color, pos, startPos=(-1,-1)):
        """Creates a new Pawn

        Args:
            color (bool): True if white, False if black
            pos (tuple): initial position of the pawn
        """
        super().__init__(color, pos, startPos)
        if color: # white
            self.rules = [(0,1),(0,2),(1,1),(-1,1)]
        else:
            self.rules = [(0,-1),(0,-2),(1,-1),(-1,-1)]
        self.startPos = startPos
             
    def calculatePossibleMoves(self, gameState, pos):
        """Calculates all the possible moves given the game state. Returns a list of tuples representing possible moves.

        Args:
            gameState (list): a 8x8x3 matrix [rectangle object, litUp, chessPiece object]
            pos (tuple): current position
        """

        moves = []
        for rel in self.rules:
            move = (pos[0]+rel[0], pos[1]+rel[1]) 
            # if both withiin bounds and overtakes an empty or diifferent color piece
            if self.withinBounds(move):
                if gameState[move[0]][move[1]][2] != None:
                    color = gameState[move[0]][move[1]][2].color
                    if color == self.color: # same color, just break
                        continue
                # if move does not cause a checkmate and is not something of the same color
                if (not self.checkCheck(gameState, pos, move, self.color)):
                    # if special move
                    if rel == (0,2):
                        # only append if in starting position
                        if pos == self.startPos:
                            if gameState[move[0]][move[1]][2] == None and gameState[move[0]][move[1]-1][2] == None:   
                                moves.append(move)
                    elif rel == (0,-2):
                        if pos == self.startPos:
                            if gameState[move[0]][move[1]][2] == None and gameState[move[0]][move[1]+1][2] == None:   
                                moves.append(move)
                    elif rel in [(1,1),(-1,1),(1,-1),(-1,-1)]:
                        if gameState[move[0]][move[1]][2] != None:
                            color = gameState[move[0]][move[1]][2].color
                            if color != self.color: # different color
                                moves.append(move)
                    elif rel in [(0,1),(0,-1)]:
                        if gameState[move[0]][move[1]][2] == None:
                            moves.append(move)
                    else:
                        moves.append(move)
        
        return moves

    def getType(self):
        """Returns type of chess piece as a string
        """
        return "Pawn"

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

            # if  within bounds
            if self.withinBounds(move):
                # if special move
                if rel == (0,2) or rel == (0,-2):
                    # only append if in starting position
                    if pos == self.startPos:
                        moves.append(move)
                else:
                    moves.append(move)
        
        return moves

    def getType(self) -> str:
        return "Pawn"
    

def main():
    # testing Pawn
    p1 = Pawn(True, (1,1))
    print(p1.calculatePossibleMoves(True, (0,0)))

if __name__ == "__main__": main()




    

    


