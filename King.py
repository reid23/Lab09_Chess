# King Chess Piece (Reid)
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
        moves=self.getAllMoves(gameState, pos)
        movSet = set(moves)
        for mov in moves:
            if self.checkCheck(gameState, pos, self._toGlobal(pos, mov), self._color):
                movSet.remove(mov)
        
        return tuple(self._toGlobal(pos, mov) for mov in list(movSet))

    def getAllMoves(self, gameState, pos):
        """Returns all possible moves

        Args:
            gameState: the current game state, a list of shape (8, 8, 3)
            pos (tuble): current position

        Returns:
            list of moves (filters out of bounds)
        """

        movSet = []
        for rel in self.rules:
            mov = (rel[0]+pos[0], rel[1]+pos[1])
            if not self.withinBounds(mov): 
                continue
            movSet.append(mov)
        # print(self.color, movSet)
        return movSet

    def getType(self) -> str:
        return "King"


# %%
