from random import randint
from player import Player
from board import Board
from string import whitespace
import discord


class Game:
    ''' Engine for a standard game of Tic-Tac-Toe '''
    __board = None
    __p1 = None
    __p2 = None
    __turn = ''
    __bots = ['Randy']
    __players = set()

    def __init__(self, board, p1, p2):
        self.__board = board
        if p1.getName() in Game.__players or p2.getName() in Game.__players:
            self.__p1 = None
            self.__p2 = None
            return
        Game.__players.add(p1.getName())
        Game.__players.add(p2.getName())
        self.__p1 = p1
        self.__p2 = p2

    def __checkWin(self):
        ''' Checks to see a winning board has been made '''
        b = self.__board
        ply = self.__p1 if self.__turn == 'p2' else self.__p2
        plyPiece = ply.getPiece()

        return b.checkRows(plyPiece) or b.checkCols(plyPiece) or b.checkDiags(plyPiece)

    async def play(self, channel, client):
        ''' Goes through the standard mode of play, with coin flip for first move, move making, and winning '''

        if randint(0, 1):
            self.__turn = 'p1'
        else:
            self.__turn = 'p2'

        p1Name = self.__p1.getName()
        p2Name = self.__p2.getName()
        player = p1Name if self.__turn == 'p1' else p2Name

        await self.__board.displayBoard(channel, p1Name, p2Name)
        await channel.send("First turn goes to {} via coin flip!".format(player))

        while True:

            if len(self.__board) == 9:
                await channel.send("Draw! Well fought game {} and {}!".format(p1Name, p2Name))
                return

            player = p1Name if self.__turn == 'p1' else p2Name

            await channel.send("{} please submit your move. To submit a move type **!ttm x, y** where x and y are positions on the board.".format(player))
            coords = await submitMove(channel, client, player)

            if self.__turn == 'p1':
                while not self.__p1.move(self.__board, self.__p1.getPiece(), coords[0], coords[1]):
                    await channel.send("Invalid Move! {}, please submit a different move **!ttm x, y**: ".format(player))
                    coords = await submitMove(channel, client, player)
                self.__turn = 'p2'
            else:
                while not self.__p2.move(self.__board, self.__p2.getPiece(), coords[0], coords[1]):
                    await channel.send("Invalid Move! {}, please submit a different move **!ttm x, y**: ".format(player))
                    coords = await submitMove(channel, client, player)
                self.__turn = 'p1'

            await self.__board.displayBoard(channel, p1Name, p2Name)

            if self.__checkWin():
                break

        winner = p1Name if self.__turn == 'p2' else p2Name
        await channel.send("Congratulations {}, you have won the match!".format(winner))
        Game.__players.remove(p1Name)
        Game.__players.remove(p2Name)

    def getPlayers(self):
        return Game.__players

    def getP1(self):
        return self.__p1

    def getP2(self):
        return self.__p2


async def submitMove(channel, client, player):
    def moveCheck(m):
        return m.author.name == player
    coords = (await client.wait_for('message', check=moveCheck)).content.split(" ")[1]
    try:
        move = coords.split(',')
        move[0] = int(move[0].strip("(){}[]" + whitespace))
        move[1] = int(move[1].strip("(){}[]" + whitespace))
    except ValueError:
        return
    return move
