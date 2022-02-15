class noPiece(ChessPiece):
    def __init__(self, *args, **kwargs):
        super().__init__(None, (420, 420))
        self._color = None

    def calculatePossibleMoves(self, gameState: list, pos: tuple) -> list:
        return []