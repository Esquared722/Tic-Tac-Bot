from game.ttt import Game
from game.player import Player
from game.board import Board

if __name__ == "__main__":

    def ynPrompt(msg):
        ans = input(msg + "(y/n) ").strip().lower()
        while ans not in ['y', 'n']:
            ans = input("Invalid Response!\n" + msg + "(y/n) ").strip().lower()
        return ans

    def namePrompt(msg):
        ans = input(msg).strip()
        while ans == '':
            ans = input("Invalid input!\n" + msg).strip()
        return ans

    while True:
        print("Welcome to Tic-Tac-Toe!")
        p1Name = namePrompt("What is your name? ")
        p1 = Player(p1Name)
        secondPlayer = ynPrompt("Two-player game?")

        if secondPlayer == 'y':
            p2Name = namePrompt("What is your name player-two? ")
            p2 = Player(p2Name)
        else:
            bots = {1:'Randy'}
            while True:
                try:
                    bot = int(input("Which CPU would you like to play against?\n1.\tRandy\n\nEnter # of the CPU you would like to verse: ")) # implement try-catch
                    while bot not in range(1, len(bots) + 1):
                        bot = int(input("Invalid Input!\nWhich CPU would you like to play against?\n1.\tRandy\n\nEnter # of the CPU you would like to verse: "))
                except ValueError:
                    print("Invalid value!")
                    continue
                break
            p2 = Player(bots[bot])

        game = Game(Board(), p1, p2)  # creates a game with two players
        game.play()

        playAgain = ynPrompt("Would you like to play again?")
        if playAgain == 'n':
            break

    print("Thanks for playing! Hope to see you again soon :D")
