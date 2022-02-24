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
            moves = []
            for rel in self.rules:
                move = self._toGlobal(pos, rel)
                # if move is within bounds
                if not self.withinBounds(move):
                    continue
                if isinstance(gameState[move[0]][move[1]][2], ChessPiece):
                    if gameState[move[0]][move[1]][2].color!=self._color:
                        moves.append(rel)
                else:
                    moves.append(rel)

            return moves

    def getType(self) -> str:
        return "King"


# %%
