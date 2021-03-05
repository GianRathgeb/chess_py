from tabulate import tabulate
from figure import Figure
import copy

class Board():
    def __init__(self, boardWidth=8, boardHight=8):
        self.boardWith = boardWidth
        self.boardHight = boardHight
        self.board = []
        for width in range(0, boardHight):
            self.board.append([])
            height = 0
            while height < self.boardHight:
                self.board[width].append('.')
                height += 1

    def setupBoard(self):
        for i in range(0, self.boardWith):
            self.board[1][i] = Figure(0, i, 1, True)
        for i in range(0, self.boardWith):
            self.board[self.boardHight - 2][i] = Figure(0, i, 6, False)
        for i in range(2):
            if i == 0:
                blackColor = True
                useIndex = 0
            else:
                blackColor = False
                useIndex = 7
            self.board[useIndex][0] = Figure(1, 0, useIndex, blackColor)
            self.board[useIndex][1] = Figure(2, 1, useIndex, blackColor)
            self.board[useIndex][2] = Figure(3, 2, useIndex, blackColor)
            self.board[useIndex][3] = Figure(4, 3, useIndex, blackColor)
            self.board[useIndex][4] = Figure(5, 4, useIndex, blackColor)
            self.board[useIndex][5] = Figure(3, 5, useIndex, blackColor)
            self.board[useIndex][6] = Figure(2, 6, useIndex, blackColor)
            self.board[useIndex][7] = Figure(1, 7, useIndex, blackColor)
            

    def printBoard(self):
        arrTemp = []
        for i in range (0, self.boardWith):
            arrTemp.append([])
            for j in range(0, self.boardHight):
                try:
                    arrTemp[i].append(self.board[i][j].figureTypeString)
                except:
                    arrTemp[i].append(self.board[i][j])
        print(tabulate(arrTemp))

    def removeFigure(self, posX, posY):
        # delete the object
        self.board[posY][posX] = '.'

    def isCheck(self, figure, newPosX, newPosY):
        return False

    def validateMove(self, figure, newPosX, newPosY):
        if figure.canMoveTo(newPosX, newPosY):
            if type(self.board[newPosY][newPosX] == 'str') or self.board[newPosY][newPosX].colorBlack == figure.colorBlack:
                #! Do nothing
                return False
            else:
                # Validate if user is check
                if self.isCheck(figure, newPosX, newPosY):
                    return False
                else:
                    return True
        else:
            return False

    def moveFigure(self, figure, newPosX, newPosY):
        if type(figure) == Figure:
            if self.validateMove(figure, newPosX, newPosY):
                # clear field, even if there are no figures
                self.removeFigure(newPosX, newPosY)
                self.board[newPosY][newPosX] = copy.copy(self.board[figure.positionY][figure.positionX])
                self.removeFigure(figure.positionX, figure.positionY)
                self.board[newPosY][newPosX].positionX = newPosX
                self.board[newPosY][newPosX].positionY = newPosY
            else:
                print('Make a valid move')
        else:
            print('Choose a figure')