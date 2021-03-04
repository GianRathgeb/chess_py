class Figure():
    def __init__(self, type, posX, posY, colorBlack):
        self.figureType = type
        self.figureTypeString = figureTypes[type]
        self.positionX = posX
        self.positionY = posY
        self.colorBlack = colorBlack

    def moveFigure(self, newPosX, newPosY):
        self.positionX = newPosX
        self.positionY = newPosY

figureTypes = {
    0: 'pawn',
    1: 'rook',
    2: 'knight',
    3: 'bishop',
    4: 'queen',
    5: 'king'
}
