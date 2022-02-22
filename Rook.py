# Pawn Chess Piece
from ChessPiece import ChessPiece

class Rook(ChessPiece):
    def __init__(self, color, pos: tuple, startPos: tuple):
        super().__init__(color, pos, startPos)

        self.rules=(
            tuple((0, i) for i in range(8)), 
            tuple((0, i) for i in range(0, -8, -1)), 
            tuple((i, 0) for i in range(8)), 
            tuple((i, 0) for i in range(0, -8, -1)),
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
                if gameState[mov[0]][mov[1]][2].color==self.color or self.checkCheck(gameState, pos, mov, self._color):
                    del nxs[counter] #delete this space too if it's the same color as me or if it would cause a checkmate
                break #then break, no more deciding to do for this section
            if self.checkCheck(gameState, pos, mov, self._color): #even if it's not a piece, we shouldn't allow check/checkmate
                del nxs[counter]
                continue
            
        return list(set(tuple(nxs)+tuple(nys)+tuple(pxs)+tuple(pys))) #make tuple to make hashable, make set and back to remove duplicates
      
    # def getAllMoves(self, pos):
        # needs to return list of possible moves only constrained by bounds (so it doesn't matter if it overtakes own piece?)
        # other option: getAllmoves given game state, which is just calculatePossibleMoves but WITHOUT using checkCheck...
    def getAllMoves(self, gameState, pos):
            """Returns all possible moves

            Args:
                gameState: the current game state, a list of shape (8, 8, 3)
                pos (tuble): current position

            Returns:
                list of moves (filters out of bounds)
            """

            nxs, nys, pxs, pys = (list(i) for i in self.rules)

            #need to check:
            #   is spot occupied by own color piece
            #   is spot blocked by any piece
            #   self.checkCheck
            #   within bounds

            for moves in [nxs, nys, pxs, pys]:
                for counter, mov in enumerate(moves):
                    if not self.withinBounds(self._toGlobal(pos, mov)): #if the move is outside the board...
                        del nxs[counter+1:]
                        break
                    if isinstance(gameState[mov[0]][mov[1]][2], ChessPiece):
                        del nxs[counter+1:] #remove all moves blocked by this piece
                        if gameState[mov[0]][mov[1]][2].color==self.color:
                            del nxs[counter] #delete this space too if it's the same color as me or if it would cause a checkmate
                        break #then break, no more deciding to do for this section
                    if self.checkCheck(gameState, pos, mov): #even if it's not a piece, we shouldn't allow check/checkmate
                        del nxs[counter]
                        continue
            
                
            return list(set(tuple(nxs)+tuple(nys)+tuple(pxs)+tuple(pys)))

    def getType(self) -> str:
        return "Rook"
