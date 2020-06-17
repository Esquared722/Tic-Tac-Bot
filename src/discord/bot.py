import json
import sys
import discord
import asyncio
from string import whitespace

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
    if parameters[0][1:] == 'ttm':
        return parameters[1]
    elif parameters[0][1:] == 'ttt':
        channel = message.channel
        initiator = message.author
        opponent = message.mentions[0]

        await channel.send(":e_mail: <@{0.id}> **{1.name}** has invited you to a game of tic-tac-toe! Do you accept the challenge? **(y/n)**".format(opponent, initiator))

        response = await gameRequest(channel, initiator, opponent)

        if response not in ['y', 'n', 'yes', 'no']:
            await channel.send(":exclamation: <@{0.id}> ***INVALID INPUT*** please respond with **(y/n)** to {1.name}'s request. One more try.".format(opponent, initiator))
            response = await gameRequest(channel, initiator, opponent)

        if response in ['y', 'yes']:
            await playGame(channel, initiator.name, opponent.name)
        elif response in ['n', 'no']:
            await channel.send(":x: <@{0.id}> **{1.name}** has refused your duel, try again next time!".format(initiator, opponent))
        else:
            await channel.send(":x: <@{0.id}> **{1.name}** failed to accept your request with valid input. Please, resend the request!".format(initiator, opponent))


async def gameRequest(channel, initiator, opponent):
    response = None

    def check(m):
        return m.author.name == opponent.name

    try:
        response = (await client.wait_for("message", check=check, timeout=60.0)).content.strip(whitespace).lower()
    except asyncio.TimeoutError:
        await channel.send(":x: <@{0.id}> request for game with **{1.name}** has timed out. Please, resend the request!".format(initiator, opponent))

    return response


async def playGame(channel, p1, p2=''):
    from player import Player
    from board import Board
    from ttt import Game
    game = Game(Board(), Player(p1), Player(p2))
    if game.getP1() is None and game.getP2() is None:
        await channel.send(':x: Sorry, users can only play one game at a time.')
        return
    await game.play(channel, client)

client.run(token)
