from piece import Piece
class Player:
    ''' Defines the actions and qualities of a player in a game of Tic-Tac-Toe '''

    __player = 0
    __canMove = False
    __name = ''
    __piece = Piece()

    def __init__(self, name):
        self.__player += 1
        self.name = name
        self.__piece = Piece(self)

    def __init__(self):
        return;
    
    def __str__(self):
        return self.name
    
    def move(self, board, piece, posX, posY):
        board.placePiece(piece, posX, posY)
    
    
    def getPlayer(self):
        return self.__player
    
    def getName(self):
        return self.name
    
    def isTurn(self):
        self.__canMove = True

    def canMove(self):
        return self.__canMove
    
    def getPiece(self):
        return self.__piece

    