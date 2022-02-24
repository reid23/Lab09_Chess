# King Chess Piece
#%%
from ChessPiece import ChessPiece
from graphics import *
#%%
class King(ChessPiece):
    def __init__(self, color, pos, startPos):
        super().__init__(color, pos, startPos)
        self.rules=((1, 0), (1,  1),
                    (0, 1), (-1, 1),
                    (-1,0), (-1,-1),
                    (0,-1), (1,-1))

    def calculatePossibleMoves(self, gameState: list, pos: tuple) -> list:
        return []
        moves=list(self.rules)
        for counter, mov in enumerate(moves):
            if isinstance(gameState[mov[0]][mov[1]][2], ChessPiece):
                if gameState[mov[0]][mov[1]][2].color==self.color or not self.checkCheck(gameState, pos, mov, self.color) or not self.withinBounds((pos[0]+mov[0], pos[1]+pos[1])):
                    del moves[counter]
            else:
                if not self.checkCheck(gameState, pos, mov, self.color) or not self.withinBounds(self._toGlobal(pos, mov)):
                    del moves[counter]
        
        return moves

    def getAllMoves(self, gameState, pos):
            """Returns all possible moves

            Args:
                gameState: the current game state, a list of shape (8, 8, 3)
                pos (tuble): current position

            Returns:
                list of moves (filters out of bounds)
            """
            return []
            moves = []
            for rel in self.rules:
                move = (pos[0]+rel[0], pos[1]+rel[1]) 
                # if move is within bounds
                if self.withinBounds(move):
                    moves.append(move)

            return moves

    def getType(self) -> str:
        return "King"


# %%
