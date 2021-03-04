import board
import time
import constants


def validateMove(figure, posX, posY):
    return True






chess = board.Board()
chess.setupBoard()
chess.printBoard()

while True:
    figPosY = int(input("Please enter Y for figure start: "))
    figPosX = int(input("Please enter X for figure start: "))
    newPosY = int(input("Please enter Y for figure move: "))
    newPosX = int(input("Please enter X for figure move: "))
    chess.moveFigure(chess.board[figPosY][figPosX], newPosX, newPosY)


    time.sleep(1)
    chess.printBoard()
