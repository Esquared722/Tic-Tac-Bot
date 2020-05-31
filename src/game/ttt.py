from random import randint
from player import Player
import board

class Game:
    ''' Engine for a standard game of Tic-Tac-Toe '''
    __board = None
    __p1 = None
    __p2 = None
    __turn = ''

    def __init__(self, board, p1, p2):
        self.__board = board
        self.__p1 = p1
        self.__p2 = p2
    
    @classmethod
    def onePlayer(cls, board, p1):
        return cls(board, p1)
    
    def __checkWin(self):
        ''' Checks to see a winning board has been made '''
        b = self.__board
        ply = self.__p1 if self.__turn == 'p2' else self.__p2
        plyPiece = ply.getPiece()

        return b.checkRows(plyPiece) or b.checkCols(plyPiece) or b.checkDiags(plyPiece)

    
    def play(self):
        ''' Goes through the standard mode of play, with coin flip for first move, move making, and winning '''

        firstmove = ''
        if randint(0, 1):
            self.__turn = 'p1'
        else: 
            self.__turn = 'p2'

        p1Name = self.__p1.getName()
        p2Name = self.__p2.getName()
        player = p1Name if self.__turn == 'p1' else p2Name

        self.__board.displayBoard()
        print("First turn goes to {} via coin flip!".format(player))
        
        
        while True:
            
            if len(self.__board) == 9:
                print("Draw! Well fought game {} and {}!".format(p1Name, p2Name))
                return;
            
            player = p1Name if self.__turn == 'p1' else p2Name
            coords = input("{}, please submit your move (col, row): ".format(player)).split(", ") # check for bad input
            
            if self.__turn == 'p1':
                while not self.__p1.move(self.__board, self.__p1.getPiece(), int(coords[0]), int(coords[1])):
                    coords = input("Another piece occupies that space. {}, please submit a different move (col, row): ".format(player)).split(", ")
                self.__turn = 'p2'
            else:
                while not self.__p2.move(self.__board, self.__p2.getPiece(), int(coords[0]), int(coords[1])):
                    coords = input("Another piece occupies that space. {}, please submit a different move (col, row): ".format(player)).split(", ")
                self.__turn = 'p1'
            
            self.__board.displayBoard()
            
            if self.__checkWin():
                break
            
             
        winner = p1Name if self.__turn == 'p2' else p2Name
        print("Congratulations {}, you have won the match!".format(winner))

    
