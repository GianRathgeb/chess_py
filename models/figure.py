class Figure():
    def __init__(self, type, posX, posY):
        self.figureType = type
        self.positionX = posX
        self.positionY = posY


class Board():
    def __init__(self, boardWidth = 8, boardHight = 8):
        self.boardWith = boardWidth
        self.boardHight = boardHight
        self.board = []
        for width in range(0, boardHight):
            self.board.append([])
            for height in range(0, boardHight):
                self.board[width].append(None)

print(Board().board)

