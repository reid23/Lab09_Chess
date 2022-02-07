# Bishop Chess Piece
from ChessPiece import ChessPiece

class Bishop(ChessPiece):
    def __init__(self, color, pos=tuple):
        super().__init__(color, (4, 1) if color else (3, 7))

        self.rules=(
            tuple((i, i) for i in range(8)), 
            tuple((i, -i) for i in range(8)), 
            tuple((-i, i) for i in range(8)), 
            tuple((-i, -i) for i in range(8)),
        )

    def calculatePossibleMoves(self, gameState: list, pos: tuple) -> list:
        nxs, nys, pxs, pys = (list(i) for i in self.rules)

        #need to check:
        #   is spot occupied by own color piece
        #   is spot blocked by any piece
        #   self.checkCheck
        #   within bounds

        for counter, mov in enumerate(nxs):
            if not self.withinBounds(self._toGlobal(pos, mov)): #if the move is outside the board...
                del nxs[counter+1:]
                break
            if isinstance(gameState[mov[0]][mov[1]][2], ChessPiece):
                del nxs[counter+1:] #remove all moves blocked by this piece
                if gameState[mov[0]][mov[1]][2].color==self.color or self.checkCheck(gameState, pos, mov):
                    del nxs[counter] #delete this space too if it's the same color as me or if it would cause a checkmate
                break #then break, no more deciding to do for this section
            if self.checkCheck(gameState, pos, mov): #even if it's not a piece, we shouldn't allow check/checkmate
                del nxs[counter]
                continue
            
        
        
        return list(set(tuple(nxs)+tuple(nys)+tuple(pxs)+tuple(pys))) #make tuple to make hashable, make set and back to remove duplicates