from graphics import Rectangle, Point
import numpy as np #only needed for 

class Board:
    def __init__(self, *pieces):
        """constructor for board class. 

        Args:
            *pieces (piece objects): the chess pieces for this board.
        """
        self.pieces=pieces
        self.gameState = self._empty(8,8,3)
        for p in pieces:
            self.putThing(p, p.getStartPos()) #add this to pieces
        for x, y in [[x, y] for x in range(8) for y in range(8)]:
            self.putThing(Rectangle(Point(x-0.5, y-0.5), Point(x+0.5, y+0.5)), (x, y), thingType='tile')
            self.putThing(bool(x%2 ^ y%2), (x, y), thingType='lit') #white true, black false
            #the bool() part just does xor(x is even, y is even)
    
    def getGameState(self, elements='all'):
        """gets the current game state, with the elements specified

        Args:
            elements (str, optional): 'all', or a combination of 'pieces', 'lit', or 'tiles'. Defaults to 'all'.

        Raises:
            NotImplemented: because I haven't implemented the elements functionality yet.

        Returns:
            list: the current game state, a list of shape (8, 8, 3).  the 3 may be a 1 or 2 if less elements are requested.
        """
        if not elements=='all':
            raise NotImplemented('sorry havent implemented this yet, will do soon')
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
                            if actuallyRemove: self.gameState[y][x][z]=replacement
                    except TypeError:
                        if k==thing:
                            poses.append([x,y,z])
                            if actuallyRemove: self.gameState[y][x][z]=replacement
        return poses



if __name__ == '__main__':
    #just some test cases
    B=Board()
    B.test()

    B.putThing('test', (5,7))

    print(B.unPutThing('test', False))

    B.putThing('test', (3,4))

    print(B.unPutThing(str, False))

    B.unPutThing('test')

    print(B.unPutThing(str, False))
