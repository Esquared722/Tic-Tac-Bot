from enum import Enum


class Type(Enum):
    ''' An enum that defines which piece type, X or O, the current piece is '''
    X = 0
    O = 1


class Piece:
    ''' Represents a tic-tac-toe piece '''

    def __init__(self, player):
        self.type = Type.X if player == 1 else Type.O

    def __str__(self):
        if self.type == Type.O:
            return 'O'
        return 'X'

    def __int__(self):
        if self.type == Type.O:
            return 'O'
        return 'X'

    def getType(self):
        return self.type
