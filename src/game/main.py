from ttt import Game
from player import Player
from board import Board


if __name__ == "__main__":
    while True:
        print("Welcome to Tic-Tac-Toe!")
        p1Name = input("What is your name? ")
        secondPlayer = input("Two-player game?(y/n) ").lower()

        p1 = Player(p1Name)

        if secondPlayer == 'y':
            p2Name = input("Player-two, what is your name? ")
            p2 = Player(p2Name)
        
        game = Game(Board(), p1, p2)

        game.play()

        playAgain = input("Would you like to play again?(y/n) ").lower()

        if playAgain == 'n':
            break
    
    print("Thanks for playing! Hope to see you soon :D")