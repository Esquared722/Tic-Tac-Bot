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
    __turn = None
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
        plyPiece = self.__turn.getPiece()

        return b.checkRows(plyPiece) or b.checkCols(plyPiece) or b.checkDiags(plyPiece)

    async def play(self, channel, client):
        ''' Goes through the standard mode of play, with coin flip for first move, move making, and winning '''

        if randint(0, 1):
            self.__turn = self.__p1
        else:
            self.__turn = self.__p2

        p1Name = self.__p1.getName()
        p2Name = self.__p2.getName()

        await self.__board.displayBoard(channel, p1Name, p2Name)
        await channel.send("First turn goes to {} via coin flip!".format(self.__turn.getName()))

        while True:

            if len(self.__board) == 9:
                await channel.send("***Draw!*** Well fought game {} and {}!".format(p1Name, p2Name))
                return

            player = self.__turn
            await channel.send("{} please submit your move. To submit a move type **!ttm x, y**" \
                "\n:1234: Use numbers on the sides as a guide :1234:".format(player.getName()))

            coords = await submitMove(channel, client, player)

            while not self.__turn.move(self.__board, self.__turn.getPiece(), coords[0], coords[1]):
                await channel.send("***Invalid Move!*** <@{}>, please submit a different move **!ttm x, y**" \
                    "\n:1234: Use numbers on the sides as a guide :1234:".format(player.getUID()))
                coords = await submitMove(channel, client, player)

            

            await self.__board.displayBoard(channel, p1Name, p2Name)

            if self.__checkWin():
                break

            self.__turn = self.__p2 if self.__turn.getUID() == self.__p1.getUID() else self.__p1

        
        winner = self.__turn.getName()
        loser = p2Name if self.__turn.getUID() == self.__p1.getUID() else p1Name
        await channel.send("Attention @everyone :bell: ***{}***, has won the match vs. *{}*! :partying_face:".format(winner, loser))
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
        return m.author.name == player.getName() and m.content.startswith("!ttm") and len(m.content.strip(whitespace)) > 4
    move = (await client.wait_for('message', check=moveCheck)).content.split(" ")[1].split(",")
    try:
        move[0] = int(move[0].strip("(){}[]" + whitespace))
        move[1] = int(move[1].strip("(){}[]" + whitespace))
    except ValueError:
        await channel.send(":x: <@{}> ***Invalid coordinates***, " \
            "make sure your coordinates are a pair of integers between [0-2]!".format(player.getUID()))
        move = (await submitMove(channel, client, player))
    return move
