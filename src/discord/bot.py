import json
import sys
import discord

sys.path.insert(1, '/Users/eric/projects/DiscordBots/TicTacBot/src/game')

with open("./config.json", "r") as read_file:
    config = json.load(read_file)

token, prefix, cID = config["token"], config["prefix"], config["channel_id"]

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user or not message.content.startswith(prefix):
        return
    parameters = message.content.split(" ")
    print(parameters)
    if parameters[0][1:] == 'ttm':
        return parameters[1]
        # ttt.setMove(parameters[1])
    elif parameters[0][1:] == 'ttt':
        await playGame(message.channel, message.author.name, message.mentions[0].name)


async def playGame(channel, p1, p2=''):
    from player import Player
    from board import Board
    from ttt import Game
    game = Game(Board(), Player(p1), Player(p2))
    if game.getP1() is None and game.getP2() is None:
        await channel.send('Sorry, users can only play one game at a time.')
        return
    await game.play(channel, client)

client.run(token)
