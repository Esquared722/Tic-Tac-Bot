from random import randint
from math import floor
from player import Player

class Game:
    __board = []
    __p1 = Player()
    __p2 = Player()
    __turn = ''

    def __init__(self, board, p1, p2):
        self.__board = board
        self.__p1 = p1
        self.__p2 = p2
    
    def play(self):
        if randint(0, 1):
            self.__turn = 'p1'
        else: 
            self.__turn = 'p2'
        
        while checkWin():
            p1Name = self.__p1.getName()
            p2Name = self.__p2.getName()

            if len(self.__board) == 9:
                print("Draw! Well fought game {} and {}".format(p1Name, p2Name))
                return;

            coords = input(p1Name if self.__turn == 'p1' else p2Name + ", please submit your move (col, row): ").split(", ")

            if self.__turn == 'p1':
                self.__p1.move(self.__board, self.__p1.getPiece(), coords[0], coords[1])
                self.__turn = 'p2'
            else:
                self.__p2.move(self.__board, self.__p2.getPiece(), coords[0], coords[1])
                self.__turn = 'p1'
            
             
        
        winner = p1Name if self.__turn == 'p2' else p2Name
        print("Congratulations {}, you have won the match!".format(winner))

    def checkWin(self):
        # TODO
        return;
