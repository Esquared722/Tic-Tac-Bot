from asyncio import TimeoutError
from game.board import Board
from game.player import Player
from random import randint, choice
from string import whitespace
import discord
import json
import pip._vendor.requests as requests

with open("game/giphyKey.json", "r") as read_file:
    giphyKey = json.load(read_file)

GIPHY_API_KEY = giphyKey["giphy_api_key"]


class Game:
    ''' Engine for a standard game of Tic-Tac-Toe '''
    __board = None
    __p1 = None
    __p2 = None
    __turn = None

    def __init__(self, board, p1, p2):
        self.__board = board
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
        await channel.send("First turn goes to <@{}> via coin flip!".format(self.__turn.getUID()))

        while True:

            if len(self.__board) == 9:
                await channel.send("***Draw!*** Well fought game {} and {}!".format(p1Name, p2Name))
                return

            player = self.__turn
            await channel.send("<@{}> please submit your move. To submit a move type **!ttm x, y**"
                               "\n:1234: Use numbers on the sides as a guide :1234:"
                               "\n:alarm_clock: You have **5 minutes** to make your move.".format(player.getUID()))

            coords = await self.__submitMove(channel, client, player)
            if coords is None:
                return

            while not self.__turn.move(self.__board, self.__turn.getPiece(), coords[0], coords[1]):
                await channel.send("***Invalid Move!*** <@{}>, please submit a different move **!ttm x, y**"
                                   "\n:1234: Use numbers on the sides as a guide :1234:".format(player.getUID()))
                coords = await self.__submitMove(channel, client, player)
                if coords is None:
                    return

            await self.__board.displayBoard(channel, p1Name, p2Name)

            if self.__checkWin():
                break

            self.__turn = self.__p2 if self.__turn.getUID() == self.__p1.getUID() else self.__p1

        winner = self.__turn.getName()
        loser = p2Name if self.__turn.getUID() == self.__p1.getUID() else p1Name
        await winMessage(channel, winner, loser)

    def getPlayers(self):
        return Game.__players

    def getP1(self):
        return self.__p1

    def getP2(self):
        return self.__p2

    async def __submitMove(self, channel, client, player):
        def moveCheck(m):
            return m.author.name == player.getName() and m.content.startswith("!ttm") and len(m.content.strip(whitespace)) > 4
        try:
            move = (await client.wait_for('message', check=moveCheck, timeout=300)).content[4:].split(",")
        except TimeoutError:
            winner = self.__p2.getName() if self.__turn.getUID(
            ) == self.__p1.getUID() else self.__p1.getName()
            await channel.send(":alarm_clock: <@{}> ***TIMEOUT*** for turn, you have been ***automatically forfeited*** from the match! **{}** wins by default.".format(player.getUID(), winner))
            await winMessage(channel, winner, player.getName())
            return None
        try:
            move[0] = int(move[0].strip("(){}[]" + whitespace))
            move[1] = int(move[1].strip("(){}[]" + whitespace))
        except ValueError:
            await channel.send(":x: <@{}> ***Invalid coordinates***, "
                               "make sure your coordinates are a pair of integers between [0-2] and that they are separated by a comma!".format(player.getUID()))
            move = (await self.__submitMove(channel, client, player))
        return move


# TODO upload the gif instead of using url, for cleaner look
def getVictoryGif():
    ''' Returns a gif from a pool of gifs requested from Giphy via API '''
    payload = {'api_key': GIPHY_API_KEY, 'q': choice(
        ['victory', 'champion', 'winner', 'congratulations', 'celebration']), 'lang': 'en'}
    response = requests.get(
        'https://api.giphy.com/v1/gifs/search', params=payload)
    return choice(response.json()['data'])


async def winMessage(channel, winner, loser):
    gifSlug = getVictoryGif()['slug']
    await channel.send("Attention @here :bell: ***{}***, has won the match vs. *{}*! :partying_face:"
                       "\nhttps://giphy.com/gifs/{}".format(winner, loser, gifSlug))
