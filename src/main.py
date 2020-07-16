import json
import sys
import discord
import logging

logging.basicConfig(level=logging.INFO)

with open("./config.json", "r") as read_file:
    config = json.load(read_file)

token, prefix = config["token"], config["prefix"]
requests = set()
boardOccupied = False
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user or not message.content.startswith(prefix):
        return
    parameters = message.content.split(" ")
    command = parameters[0][1:]
    channel = message.channel
    initiator = message.author
    if command == 'ttm':
        return parameters[1]
    elif command == 'ttt':
        try:
            if initiator in requests:
                await channel.send(":x: <@{0.id}> You are already in a game and can not make/accept requests".format(initiator))
                return
            opponent = message.mentions[0]
            if opponent in requests:
                await channel.send(":x: <@{0.id}> **{1.name}** has already been sent a request by another user".format(initiator, opponent))
                return
        except IndexError:
            await channel.send(':x: To request a game with someone you must mention them **(Ex. "!ttm @User")**')
            return

        await channel.send(":e_mail: <@{0.id}> **{1.name}** has invited you to a game of "
                           "tic-tac-toe! Do you accept the challenge? **(y/n)**".format(opponent, initiator))

        requests.add(opponent)
        response = await gameRequest(channel, initiator, opponent)

        if response not in ['y', 'n', 'yes', 'no']:
            await channel.send(":exclamation: <@{0.id}> ***INVALID INPUT*** please respond "
                               "with **(y/n)** to {1.name}'s request. One more try.".format(opponent, initiator))
            response = await gameRequest(channel, initiator, opponent)

        if response in ['y', 'yes']:
            await playGame(channel, initiator, opponent)
        elif response in ['n', 'no']:
            await channel.send(":x: <@{0.id}> **{1.name}** has refused your duel,"
                               " try again next time!".format(initiator, opponent))
        else:
            await channel.send(":x: <@{0.id}> **{1.name}** failed to accept your request "
                               "with valid input. Please, resend the request!".format(initiator, opponent))
    elif command == 'tthelp':
        embed = discord.Embed(title="Commands")
        embed.add_field(name="!ttt <@[other-user.id]>",
                        value="Sends an invite to the other user, via mention, to a game of Tic-Tac-Toe, and will commence the game if the invitee accepts.", inline=False)
        embed.add_field(
            name="!ttm x, y", value="It allows a player to move their piece to a (col[x], row[y]) position on the board on their turn.", inline=False)
        embed.add_field(
            name="!tthelp", value="Gives information on all commands and a link to where the source code can be examined.")
        embed.add_field(name="Full Information",
                        value="Look at the [github](https://github.com/Esquared722/Tic-Tac-Bot)")
        await channel.send(embed=embed)
    else:
        return None


async def gameRequest(channel, initiator, opponent):
    from asyncio import TimeoutError
    from string import whitespace
    response = None

    def check(m):
        return m.author.name == opponent.name

    try:
        response = (await client.wait_for("message", check=check, timeout=60)).content.strip(whitespace).lower()
    except TimeoutError:
        await channel.send(":x: <@{0.id}> request for game with **{1.name}** has timed out. "
                           "Please, resend the request!".format(initiator, opponent))

    return response


async def playGame(channel, p1, p2):
    from game.player import Player
    from game.board import Board
    from game.ttt import Game
    game = Game(Board(), Player(p1), Player(p2))
    global boardOccupied
    if boardOccupied:
        await channel.send(':x: Only one pair of players can occupy the board at a time.')
    else:
        boardOccupied = True
        requests.add(p1)
        await game.play(channel, client)
        boardOccupied = False
        requests.remove(p1)
        requests.remove(p2)

client.run(token)
