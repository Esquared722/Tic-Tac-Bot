# Tic-Tac-Bot

A discord bot that allows users on a server duel in a friendly game of traditional Tic-Tac-Toe. Game history and statistics will be recorded for each user on the server, will be persisted in a database.

## Getting Started

To get this bot, follow this link [here](https://discord.com/api/oauth2/authorize?client_id=714273310208294994&permissions=67584&scope=bot)

## Commands

* !ttt [other user]: Sends an invite to the other user, via mention, to a game of Tic-Tac-Toe, and will commence the game if the invitee accepts. Also, acts as an accept to a game if used by the invitee succeeding the invite.

## Built With

* [Python 3](https://docs.python.org/3/) - Language
* [PyPI](https://pypi.org/) - Dependency Management
* [PostgreSQL](https://www.postgresql.org/) - Database
* [discord.py](https://github.com/Rapptz/discord.py) - API Wrapper
