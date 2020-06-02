from piece import Piece


class Player:
    ''' Defines the actions and qualities of a player in a game of Tic-Tac-Toe '''

    __player = 0
    __canMove = False
    __name = ''
    __piece = None

    def __init__(self, name):
        Player.__player += 1
        self.name = name
        self.__piece = Piece(self.__player)

    def __int__(self):
        return self.__player

    def move(self, board, piece, posX = None, posY = None):  # check for valid move
        if self.name == 'Randy': # bot Randy move
            from random import randint
            posX, posY = randint(0, 2), randint(0, 2)

        if self.isValidMove(board, posX, posY):
            board.placePiece(piece, posX, posY)
            return True
        return False

    def isValidMove(self, board, posX, posY):
        if posX in range(3) and posY in range(3) and board.getBoard()[posY][posX] == ' ':
            return True

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
    
