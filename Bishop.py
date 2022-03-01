# Bishop Chess Piece (Reid)
from ChessPiece import ChessPiece

class Bishop(ChessPiece):
    def __init__(self, color, pos, startPos):
        super().__init__(color, pos,startPos)

        self.rules = ((1,1),
                     (1,-1),
                     (-1,1),
                     (-1,-1))

    def calculatePossibleMoves(self, gameState: list, pos: tuple) -> list:
        """Calculates all the possible moves given the game state. Returns a list of tuples representing possible moves.

        Args:
            gameState (list): a 8x8x3 matrix [rectangle object, litUp, chessPiece object]
            pos (tuple): current position
        """

        moves = []
        for rel in self.rules:
            for i in range(1,8): # up to 8 squares
                move = self._toGlobal(pos, (rel[0]*i, rel[1]*i)) #convert to absolute position
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
            for i in range(1,8): # up to 8 squares
                move = self._toGlobal(pos, (rel[0]*i, rel[1]*i)) #convert to absolute position
                # if both withiin bounds and overtakes an empty or diifferent color piece
                if self.withinBounds(move):
                    if gameState[move[0]][move[1]][2] != None:
                        color = gameState[move[0]][move[1]][2].color
                        if color != self.color:
                            moves.append(move)
                        break # no need to continue in this direction
                    
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
            for i in range(1,8): # up to 8 squares
                move = self._toGlobal(pos, (rel[0]*i, rel[1]*i)) #convert to absolute position
                # if both withiin bounds and overtakes an empty or diifferent color piece
                if self.withinBounds(move):
                    if gameState[move[0]][move[1]][2] != None:
                        color = gameState[move[0]][move[1]][2].color
                        if color != self.color:
                            moves.append(move)
                        break # no need to continue in this direction
                    
                    moves.append(move)
        
        return moves
        
        
    def getType(self) -> str:
        return "Bishop"