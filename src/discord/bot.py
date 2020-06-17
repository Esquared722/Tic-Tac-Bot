import json, sys, discord

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
        await channel.send(":e_mail: <@{0}> {1.name} has invited you to a game of tic-tac-toe! Do you accept the challenge? **(y/n)**".format(opponent.id, initiator))
        
        def check(m):
            return m.author.name == opponent.name

        response = (await client.wait_for("message", check=check)).content
        if response == 'y':
            try:
                await playGame(channel, initiator.name, opponent.name)
            finally:
                pass
        else:
            await channel.send(":x: <@{0}> {1.name} has refused your duel, try again next time!".format(initiator.id, opponent))


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
