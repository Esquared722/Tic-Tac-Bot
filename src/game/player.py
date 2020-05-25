
class Player:
    ''' Defines the actions and qualities of a player in a game of Tic-Tac-Toe '''

    __player = 0
    __canMove = False
    __name = ''

    def __init__(self, name):
        self.__player += 1
        self.name = name
    
    def __str__(self):
        return self.name
    
    def move(self, other, board, piece, posX, posY):
        if not self.__canMove:
            return 0
        
        board.placePiece(piece, posX, posY)
        self.__canMove = False;
        other.__canMove = True;
    
    
    def getPlayer(self):
        return self.__player
    
    def getName(self):
        return self.name

    
