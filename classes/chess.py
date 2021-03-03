import board
import time


def validateMove(figure, posX, posY):
    return True


def moveFigure(figure, posX, posY):
    if validateMove(figure, posX, posY):
        figure.moveFigure(posX, posY)
        chess.board[posX][posY] = figure
        chess.removeFigure(posX, posY)




chess = board.Board()
chess.setupBoard()
chess.printBoard()

while True:
    moveFigure(chess.board[0][0], 4, 4)

    time.sleep(1)
    chess.printBoard()
