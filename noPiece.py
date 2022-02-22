from ChessPiece import ChessPiece
class noPiece(ChessPiece):
    def __init__(self, *args, **kwargs):
        super().__init__(None, (420, 420))

    def calculatePossibleMoves(self, gameState: list, pos: tuple) -> list:
        return []