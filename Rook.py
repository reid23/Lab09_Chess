# Rook Chess Piece (Reid)
from ChessPiece import ChessPiece

class Rook(ChessPiece):
    def __init__(self, color, pos: tuple, startPos: tuple):
        super().__init__(color, pos, startPos)

        self.rules=(
            tuple((0, i) for i in range(8))+
            tuple((0, i) for i in range(0, -8, -1))+
            tuple((i, 0) for i in range(8))+
            tuple((i, 0) for i in range(0, -8, -1))
        )
    

    def calculatePossibleMoves(self, gameState: list, pos: tuple) -> list:

        moves = self.getAllMoves(gameState, pos)
        cp = set(tuple(moves))
        for i in moves:
            if self.checkCheck(gameState, pos, self._toGlobal(pos, i), self._color):
                cp.remove(i)
        
        return list(self._toGlobal(pos, i) for i in cp)
      
    def getAllMoves(self, gameState, pos):
            """Returns all possible moves, also needlessly complicated

            Args:
                gameState: the current game state, a list of shape (8, 8, 3)
                pos (tuble): current position

            Returns:
                list of moves (filters out of bounds)
            """

            moves = self.rules
            movSet = set(moves)
            movSet.remove((0,0))
            moves = tuple(movSet)
            for mov in moves:
                if not mov in movSet:
                    continue

                move=self._toGlobal(self._curPos, mov)

                if not self.withinBounds(move):
                    movSet.remove(mov)
                    continue

                thing = gameState[move[0]][move[1]][2]
                if thing==None:
                    continue
                if isinstance(thing, ChessPiece):
                    if thing.color==self._color:
                        movSet.remove(mov)
                        counter=1

                        #this while loop just removes all moves that are beyond this point
                        #like if there's a piece in this move, then all moves past this move should be deleted
                        while True:
                            try:
                                #ok heres the confuzzlement line

                                #  remove          (0,  curY +- counter)          if current move's x is 0  otherwise remove   (curX +- counter, 0)  instead
                                movSet.remove(((0, mov[1]+ (mov[1]/abs(mov[1]))*counter) if mov[0]==0 else (mov[0]+(mov[0]/abs(mov[0]))*counter, 0)))
                            except:
                                break
                            counter += 1
                    else:
                        counter = 1
                        while True:
                            try:
                                movSet.remove(((0, mov[1]+ (mov[1]/abs(mov[1]))*counter) if mov[0]==0 else (mov[0]+(mov[0]/abs(mov[0]))*counter, 0)))
                            except:
                                break
                            counter += 1
                
            return list(movSet)
