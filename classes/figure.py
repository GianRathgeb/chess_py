from tabulate import tabulate

class Figure():
    def __init__(self, typeStr, type, posX, posY, colorBlack):
        self.figureType = type
        self.figureTypeString = typeStr
        self.positionX = posX
        self.positionY = posY
        self.colorBlack = colorBlack

# Types:
#     Pawn = 0
#     Rook = 1
#     Knight = 2
#     Bishop = 3
#     Queen = 4
#     King = 5


class Board():
    def __init__(self, boardWidth=8, boardHight=8):
        self.boardWith = boardWidth
        self.boardHight = boardHight
        self.board = []
        for width in range(0, boardHight):
            self.board.append([])
            for height in range(0, boardHight):
                self.board[width].append('e.g.')
        
    def setupBoard(self):
        for i in range(0, self.boardWith):
            self.board[1][i] = Figure('pawn', 0, i, 1, True)
        for i in range(0, self.boardWith):
            self.board[self.boardHight - 2][i] = Figure('pawn', 0, i, 1, False)
        for i in range(2):
            if i == 0:
                blackColor = True
                useIndex = 0
            else:
                blackColor = False
                useIndex = 7
            self.board[useIndex][0] = Figure('rook', 1, 0, useIndex, blackColor)
            self.board[useIndex][1] = Figure('knight', 2, 1, useIndex, blackColor)
            self.board[useIndex][2] = Figure('bishop', 3, 2, useIndex, blackColor)
            self.board[useIndex][3] = Figure('queen', 4, 3, useIndex, blackColor)
            self.board[useIndex][4] = Figure('king', 5, 4, useIndex, blackColor)
            self.board[useIndex][5] = Figure('bishop', 3, 5, useIndex, blackColor)
            self.board[useIndex][6] = Figure('knight', 2, 6, useIndex, blackColor)
            self.board[useIndex][7] = Figure('rook', 1, 7, useIndex, blackColor)
            

    def printBoard(self):
        arrTemp = []
        arrTemp = self.board[:]
        for rowNum, row in enumerate(self.board):
            for fieldNum, field in enumerate(row):
                try:
                    arrTemp[rowNum][fieldNum] = field.figureTypeString
                except:
                    pass
        print(tabulate(arrTemp))
        

test = Board()
test.setupBoard()
print(test.board[6][0].figureType)

test.printBoard()


