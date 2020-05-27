from ttt import Game
from player import Player
from board import Board


if __name__ == "__main__":

    welcome = input("Welcome to Tic-Tac-Toe! Would you like to play?(y/n) ").lower() # check for bad input

    if welcome == 'y':
        p1Name = input("Fantastic!\nWhat is your name player one? ")
        secondPlayer = input("Will you be playing with someone else today?(y/n) ").lower()

        if secondPlayer == 'y':
            p2Name = input("What is player two's name? ")
            p2 = Player(p2Name)
        
        p1 = Player(p1Name)

        game = Game(Board(), p1, p2)

        game.play()
    else:
        print("Aww, too bad! Glad to see you another time!")