#%%
from ChessPiece import ChessPiece
#%%
class King(ChessPiece):
    def __init__(self, color, pos='dont pass'):
        super().__init__(color, (4, 1) if color else (3, 7))
        self.rules=((1, 0), (1,  1),
                    (0, 1), (-1, 1),
                    (-1,0), (-1,-1),
                    (0,-1), (1,-1))

    def calculatePossibleMoves(self, gameState: list, pos: tuple) -> list:
        moves=list(self.rules)
        for counter, mov in enumerate(moves):
            if isinstance(gameState[mov[0]][mov[1]][2], ChessPiece):
                if gameState[mov[0]][mov[1]][2].color==self.color or not self.checkCheck(gameState, pos, mov) or not self.withinBounds(map(sum,zip(pos, mov))):
                    del moves[counter]
            else:
                if not self.checkCheck(gameState, pos, mov) or not self.withinBounds(self._toGlobal(pos, mov)):
                    del moves[counter]
        
        return moves


# %%
