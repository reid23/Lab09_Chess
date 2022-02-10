from graphics import Rectangle, Point, color_rgb
import numpy as np #only needed for test func
import os
from Pawn import Pawn
from Queen import Queen
from Knight import Knight
from King import King
from Bishop import Bishop
from Rook import Rook

class Board:
    def __init__(self, *pieces, board=None):
        """constructor for board class. 

        Args:
            *pieces (piece objects): the chess pieces for this board.
            board (list): a pre-set board, if needed.  Don't pass.
        """
        if not pieces:
            pieces={
                Pawn(True, (0,1)),
                Pawn(False, (0,6)),

                Pawn(True, (1,1)),
                Pawn(False, (1,6)),

                Pawn(True, (2,1)),
                Pawn(False, (2,6)),

                Pawn(True, (3,1)),
                Pawn(False, (3,6)),

                Pawn(True, (4,1)),
                Pawn(False, (4,6)),

                Pawn(True, (5,1)),
                Pawn(False, (5,6)),

                Pawn(True, (6,1)),
                Pawn(False, (6,6)),

                Pawn(True, (7,1)),
                Pawn(False, (7,6)),

                Knight(True, (1,0)),
                Knight(True, (6,0)),
                Knight(False, (1,7)),
                Knight(False, (6,7)),

                Rook(True, (0,0)),
                Rook(True, (7,0)),
                Rook(False, (0,7)),
                Rook(False, (7,7)),

                Bishop(True, (2,0)),
                Bishop(True, (5,0)),
                Bishop(False, (2,7)),
                Bishop(False, (5,7)),

                King(True, (4,0)),
                King(False, (4,7)),
                Queen(True, (3,0)),
                Queen(False, (3,7)),
            }
        self.n=0
        self.iterReturns='squares'
        self.pieces=set(pieces)
        self.descriminator=lambda x: True
        if board!=None:
            self.gameState=board
        else:
            self.gameState = self._empty(8,8,3)
            # for p in pieces:
                # self.putThing(p, p.startPos) #add this to pieces
            for x, y in [[x, y] for x in range(8) for y in range(8)]:
                r = Rectangle(Point(10*x,10*y), Point(10*(x+1),10*(y+1)))
                r.setOutline("white")
                if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                    r.setFill('grey')
                else:
                    r.setFill(color_rgb(245, 245, 242))
                self.putThing(r, (x, y), thingType='tile')
                self.putThing(False, (x, y), thingType='lit') #white true, black false
                #the bool() part just does xor(x is even, y is even)
    
    def __eq__(self, other):
        return self.gameState==other.getGameState()

    def copy(self):
        return Board(board=self.gameState)
    
    def reset(self):
        self.gameState = self._empty(8,8,3)
        for p in self.pieces:
            self.putThing(p, p.startPos) #add this to pieces
        for x, y in [[x, y] for x in range(8) for y in range(8)]:
            r = Rectangle(Point(10*x,10*y), Point(10*(x+1),10*(y+1)))
            r.setOutline("white")
            if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                r.setFill('grey')
            else:
                r.setFill(color_rgb(245, 245, 242))
            self.putThing(r, (x, y), thingType='tile')
            self.putThing(False, (x, y), thingType='lit') #white true, black false

    def getGameState(self, elements='all'):
        """gets the current game state, with the elements specified

        Args:
            elements (str, optional): 'all', or a combination of 'pieces', 'lit', or 'tiles'. Defaults to 'all'.

        Raises:
            NotImplemented: because I haven't implemented the elements functionality yet.

        Returns:
            list: the current game state, a list of shape (8, 8, 3).  the 3 may be a 1 or 2 if less elements are requested.
        """
        # if not elements=='all':
        #     raise NotImplemented('sorry havent implemented this yet, will do soon')
        match elements:
            case 'all':
                return self.gameState.copy()
            case 'tile':
                return self.gameState[0].copy()
            case 'lit':
                return self.gameState[1]
            case 'piecesOnBoard':
                return self.gameState[2].copy()
            case 'pieces':
                return self.pieces.copy()



        return self.gameState

    def test(self): #just for testing to see if correct squares are lit up
        print(np.array([[i[1] for i in j] for j in self.gameState]))
    
    @staticmethod
    def _empty(*shape, initialVal=None):
        """generates a list with the given shape, whose values are initialVal

        Args:
            *shape (int, multiple values accepted): integers describing the length of each dimension of the requested list.
            initialVal (any, optional): the values in the list. Defaults to None.

        Returns:
            list: the requested list
        """
        shape=list(shape)
        shape.reverse()
        output=(initialVal,)
        for i in shape:
            output=output*i
            output=(output,)
        return Board.convert(output[0]) #convert to list, and take out extra dimension from previous line on last iteration
    
    @staticmethod
    def convert(t): #recursion go brrrrr
        """converts a tuple to a list recursively

        Args:
            t (tuple): the input tuple

        Returns:
            list: the same thing as the input, but as a list
        """
        if isinstance(t, tuple):
            return list(Board.convert(i) for i in t)
        else:
            return t


    def T(self, arr=None):
        """transposes the input 2d array

        Args:
            arr (list, optional): array to transpose. Defaults to self.gameState.

        Returns:
            list: copy of arr, transposed.
        """
        if arr==None: arr=self.gameState

        output=arr.copy()

        for i in range(len(arr)):
            for j in range(len(i)):
                output[i][j]=arr[j][i]

        return output

    def lightUpSquares(self, clickedSquare: tuple):
        if self.gameState[clickedSquare[0]][clickedSquare[1]][2]!=None:
            rule=lambda x: x in self.gameState[clickedSquare[0]][clickedSquare[1]][2].calculatePossibleMoves(self.getGameState('pieces'))
            self.putThingRule(True, rule, thingType='lit')
        
    def __sub__(self, other):
        """subtraction between board classes.  don't call directly, do changes=oldBoard-newBoard

        Args:
            other (the other board): a board object, the new state

        Raises:
            NotImplementedError: if $other isn't a board object

        Returns:
            tuple: the differences in the form ((x, y, z), thing), where (x, y, z) describes the position and the thing is the new thing.
        """
        if not isinstance(other, Board):
            raise NotImplementedError
        
        output=[]
        for i in range(8):
            for j in range(8):
                for k in range(1,3):
                    if not other.getThing(i, j, k)==self.gameState[i][j][k]:
                        output.append(((i, j, k), self.gameState[i][j][k]))
        return tuple(output)

    def putThing(self, thing, position, thingType='piece'):
        """puts $thing into the board at $position

        Args:
            thing (any): the object to place in the board
            position (tuple): a 2-tuple of ints describing the position (x, y) in the board to place $thing. ints should be 0-7, inclusive.
            thingType (str, optional): the type of thing: 'piece', 'tile', or 'lit'.  if you want to set a tile's light status, pass 'lit'. Defaults to 'piece'.
        """
        match thingType:
            case 'tile':
                self.gameState[position[1]][position[0]][0]=thing
            case 'lit':
                self.gameState[position[1]][position[0]][1]=thing
            case 'piece':
                self.gameState[position[1]][position[0]][2]=thing
                self.pieces.add(thing)


    def checkCzechCheque(self, *args, **kwargs): #haha obfuscation go brrrrrr
        os.system('osascript -e "Set Volume 10"')
        os.system(f'say "{str(args)}, {str(kwargs)}"')

    def putThingRule(self, thing, rule, thingType='piece'):
        """puts $thing into all of the places where $thingType things can go, and where rule(xPos, yPos) evaluates to True

        Args:
            thing (any): the thing to insert
            rule (function): a function that returns true if $thing should be inserted at (x, y) in the board.  takes the tuple (x, y) where x and y are ints from 0-7.
            thingType (str, optional): the type of thing: 'piece', 'tile', or 'lit'. Piece means a piece object, tile means a rectangle, and lit means a bool saying whether a square is lit.. Defaults to 'piece'.
        """
        for x in range(8):
            for y in range(8):
                if rule((x, y)):
                    self.putThing(thing, (x, y), thingType=thingType)

    def unPutThing(self, thing, actuallyRemove=True, replacement=None):
        """finds and removes $thing from the board, and replaces it with $replacement.  Only actually does this if $actuallyremove

        Args:
            thing (any): the thing to look for
            actuallyRemove (bool, optional): whether or not to actually remove the thing or just find it. Defaults to True.
            replacement (any, optional): what to replace the object with. Defaults to None.

        Returns:
            list: the locations of the things found, in form [[x, y, z], [x2, y2, z2], ...]
        """
        poses=[]
        for y, i in enumerate(self.gameState):
            for x, j in enumerate(i):
                for z, k in enumerate(j):
                    try:
                        if isinstance(k, thing):
                            poses.append([x,y,z])
                            if actuallyRemove: 
                                self.gameState[y][x][z]=replacement
                                if k in self.pieces: self.pieces.remove(k)
                    except TypeError:
                        if k==thing:
                            poses.append([x,y,z])
                            if actuallyRemove: 
                                self.gameState[y][x][z]=replacement
                                if k in self.pieces: self.pieces.remove(k)
        return poses
    
    def getThing(self, x, y, z=None):
        if z==0:
            return self.gameState[x][y][z]
        elif z==1:
            return self.gameState[x][y][z]
        elif z==2:
            return self.gameState[x][y][z]
        return self.gameState[x][y].copy()

    def __call__(self, things='all', descriminator=None):
        """call method for board, for generating an iterable for for loops.  ie 'for _ in Board(): pass'

        Args:
            things (str, optional): the things to iterate through: 'all', 'lit', 'title', 'piecesInBoard', 'pieces', 'rows', or 'columns'. Defaults to 'all', giving a len-3 list.
            descriminator (str|function, optional): returns True only if output should be kept, like "lambda x: x.getColor()=='Black'" or whatever to only iterate through the black pieces. Screens outputs. Defaults to None.

        Returns:
            Board: this board object, passed to for loop with correct instance vars for appropriate iteration
        """


        if descriminator==None: self.descriminator=lambda x: True
        else: self.descriminator=descriminator

        self.iterReturns=things
        return self

    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.iterReturns=='all':

            if self.n==65: raise StopIteration

            while True:
                output = self.gameState[int(self.n/8.05)][self.n%8].copy()
                if self.descriminator(output): break
                self.n+=1

        elif self.iterReturns=='tile':

            if self.n==65: raise StopIteration

            while True:
                output = self.gameState[int(self.n/8.05)][self.n%8][0]
                if self.descriminator(output): break
                self.n+=1
        
        elif self.iterReturns=='lit':

            if self.n==65: raise StopIteration

            while True:
                output = self.gameState[int(self.n/8.05)][self.n%8][1]
                if self.descriminator(output): break
                self.n+=1

        elif self.iterReturns=='piecesInBoard':

            if self.n==65: raise StopIteration

            while True:
                output = self.gameState[int(self.n/8.05)][self.n%8][2]
                if self.descriminator(output): break
                self.n+=1

        elif self.iterReturns=='pieces':

            if self.n==len(self.pieces): raise StopIteration

            while True:
                output = list(self.pieces)[self.n]
                if self.descriminator(output): break
                self.n+=1


        elif self.iterReturns=='rows':

            if self.n==8: raise StopIteration

            while True:
                output=self.gameState[self.n].copy()
                if self.descriminator(output): break
                self.n+=1
        

        elif self.iterReturns=='columns':

            if self.n==8: raise StopIteration

            while True:
                output=self.T()[self.n].copy()
                if self.descriminator(output): break
                self.n+=1

        self.n+=1
        return output









if __name__ == '__main__':
    old=Board()
    new=Board()

    moves = {
        (0,0),
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
    }

    new.putThing(True, (5,5), thingType='lit')
    new.putThingRule(True, lambda x: x in moves, thingType='lit')

    print(new-old)

