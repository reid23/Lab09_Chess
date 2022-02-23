# Pawn Chess Piece
from ChessPiece import ChessPiece
from King import King

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

                match gameState[move[0]][move[1]][2]:
                    case ChessPiece(color=self._color):
                        movSet.remove(mov)
                        for i in list(movSet):
                            match i:
                                case (0, y) if mov[0]==0 and y/abs(y)==mov[1]/abs(mov[1]) and y>mov[1]:
                                    movSet.remove(i)
                                case (x, 0) if mov[1]==0 and x/abs(x)==mov[0]/abs(mov[0]) and x>mov[0]:
                                    movSet.remove(i)

                    case ChessPiece(color=color) if color!=self._color:
                        for i in list(movSet):
                            match i:
                                case (0, y) if mov[0]==0 and y/abs(y)==mov[1]/abs(mov[1]) and y>mov[1]:
                                    movSet.remove(i)
                                case (x, 0) if mov[1]==0 and x/abs(x)==mov[0]/abs(mov[0]) and x>mov[0]:
                                    movSet.remove(i)
                    
            return list(movSet)


                    



    def getType(self) -> str:
        return "Rook"


#%%
class foo:
    def __init__(self, bar):
        self.bar=bar
        self.banana=True

class sub_foo(foo):
    def __init__(self, bar, bar2):
        super().__init__(bar)
        self.bar2=bar2


# %%
var=sub_foo(1,2)
match var:
    case None:
        print('ooooh')
    case foo(bar=2):
        print('foo(1)')
    case sub_foo(bar=2,bar2=2):
        print('sub_foo(1,2)')
    case foo(bar=1, banana=val) if val!=False:
        print('banana')
# %%
