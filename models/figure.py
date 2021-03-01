class Figure():
    def __init__(self, type, posX, posY):
        self.figureType = type
        self.positionX = posX
        self.positionY = posY


class Board():
    def __init__(self, boardWith = 8, boardHight = 8):
        self.boardWith = boardWith
        self.boardHight = boardHight
        self.board = []
