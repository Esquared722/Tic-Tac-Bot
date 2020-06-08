import discord, json

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
    try:
        commands = {'ttt': playGame} # dictionary of bot commands
        await commands[parameters[0][1:]](message.channel, message.author, parameters[1])
    except IndexError:
        await commands[parameters[0][1:]](message.author) # game against a bot
    except KeyError:
        await message.channel.send('Invalid Command!')
        return

async def playGame(channel, p1, p2=''):
    await channel.send('This is a game between {} and {}.'.format(p1, 'a bot' if p2 is '' else p2))
    # TODO implement rest of a standard game, by using previously made code

client.run(token)