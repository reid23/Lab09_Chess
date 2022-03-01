# King Chess Piece (Reid)

from ChessPiece import ChessPiece
class King(ChessPiece):
    def __init__(self, color, pos, startPos):
        super().__init__(color, pos, startPos)
        self.rules=((1, 0), (1,  1),
                    (0, 1), (-1, 1),
                    (-1,0), (-1,-1),
                    (0,-1), (1,-1))

    def calculatePossibleMoves(self, gameState: list, pos: tuple) -> list:

        movSet = []
        for rel in self.rules:
            mov = (rel[0]+pos[0], rel[1]+pos[1])
            if not self.withinBounds(mov): 
                continue
            if gameState[mov[0]][mov[1]][2] != None:
                color = gameState[mov[0]][mov[1]][2].color
                if color == self.color: # same color, just break
                    continue
            if not self.checkCheck(gameState, pos, mov, self._color):
                movSet.append(mov)
        return movSet

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
            if gameState[mov[0]][mov[1]][2] != None:
                color = gameState[mov[0]][mov[1]][2].color
                if color == self.color: # same color, just break
                    continue
            movSet.append(mov)
        # print(self.color, movSet)
        return movSet


# %%
