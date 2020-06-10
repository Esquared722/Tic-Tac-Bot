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
    if len(parameters) > 2:
        await message.channel.send('Invalid Command! Can only verse one player at a time.')
        return
    commands = {'ttt': playGame}  # dictionary of bot commands
    try:
        await commands[parameters[0][1:]](message.channel, message.author.name, message.mentions[0].name)
    except IndexError:
        # game against a bot
        await commands[parameters[0][1:]](message.channel, message.author.nick)
    except KeyError:
        await message.channel.send('Invalid Command!')
        return


async def playGame(channel, p1, p2=''):
    from ttt import Game
    from player import Player
    from board import Board
    await channel.send('This is a game between {} and {}.'.format(p1, 'a bot' if p2 is '' else p2))
    game = Game(Board(), Player(p1), Player(p2))
    await game.play(channel)


client.run(token)
