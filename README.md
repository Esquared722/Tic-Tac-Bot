# Tic-Tac-Bot

A discord bot that allows users on a server duel in a friendly game of traditional Tic-Tac-Toe. Game history and statistics will be recorded for each user on the server, will be persisted in a database.

## Getting Started

To use this bot on your own discord server, you must follow this link [here](https://discord.com/api/oauth2/authorize?client_id=714273310208294994&permissions=67584&scope=bot)

## Commands [WIP] (Finished Commands in BOLD)

* !ttt [other user]: Sends an invite to the other user, via mention, to a game of Tic-Tac-Toe, and will commence the game if the invitee accepts. Also, acts as an accept to a game if used by the invitee succeeding the invite.
* !tthelp: Triggers the bot to send a link to the git page for the list of commands available for the bot, and a brief description of its capabilites.
* !tthist [other user] [date]: Triggers the bot to retrieve a paginated record of the user's match history with the other user. If date provided, only history from that date onward will be retrieved.
* !ttprof: Triggers the bot to retrieve game related data to the user, e.g. Wins-Ties-Losses (All), Win Rate %, Easiest Opponent, Toughest Opponent, Best First Move, Best Piece.

## Built With

* [Python 3](https://docs.python.org/3/) - Language
* [PyPI](https://pypi.org/) - Dependency Management
* [PostgreSQL](https://www.postgresql.org/) - Database
* [discord.py](https://github.com/Rapptz/discord.py) - API Wrapper
