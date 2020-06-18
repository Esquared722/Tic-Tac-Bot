from piece import Piece
from discord import User


class Player:
    ''' Defines the actions and qualities of a player in a game of Tic-Tac-Toe '''

    __player = 0
    __canMove = False
    __name = None
    __userDisc = None
    __piece = None

    def __init__(self, userDisc):
        Player.__player += 1
        self.__userDisc = userDisc
        self.__name = userDisc.name
        self.__piece = Piece(self.__player)

    def __int__(self):
        return self.__player

    def move(self, board, piece, posX = None, posY = None):  # check for valid move
        # if self.__name == 'Randy': # bot Randy move
        #     from random import randint
        #     posX, posY = randint(0, 2), randint(0, 2)
        if posX in range(3) and posY in range(3) and board.getBoard()[posY][posX] == ' ':
            board.placePiece(piece, posX, posY)
            return True
        return False

    def getName(self):
        return self.__name

    def getPiece(self):
        return self.__piece
    
    def getUID(self):
        return self.__userDisc.id
    
