import os
import random
import json

from dotenv import load_dotenv

from colorama import Fore
from colorama import Style

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='$')
json_file = 'quotes.json'

GOGBOT = f'{Fore.CYAN}GogBot{Style.RESET_ALL}'


@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(
            f'🚀 {GOGBOT} has connected to {Fore.CYAN}{guild.name}{Style.RESET_ALL}'
        )


@bot.command(name='quote', help='funny')
async def quote(ctx, person: str):
    """Echoes a random quote chosen from the person's quote list and prints
    it into the chat.

    Args:
        person (str): the person who's random quote we want to generate.
    """
    print(f'🚀 {GOGBOT} > Quote for {person} requested')

    with open(json_file, 'r') as f:
        people = json.load(f)

    response = ''
    if person in people:
        response = random.choice(people[person])
    else:
        response = f'{person} 🥶'

    print(f'👍 {GOGBOT} > Replied: {response}')
    await ctx.send(response)


@bot.command(name='add_quote')
async def add_quote(ctx, person: str, quote: str):
    """Takes a quote as an input and adds it to the person's quote list in the
    json file.

    Args:
        person (str): the person to add the quote to.
        quote (str): the quote to add to the person's list of quotes.
    """
    print(f'🚀 {GOGBOT} > Adding quote requested')
    quotes: dict = {}
    response = ''

    with open(json_file, 'r') as f:
        quotes = json.load(f)

    if person in quotes:
        quotes[person].append(quote)
        response = f'added quote: {quote} to {person}\'s quotes'
    else:
        quotes[person] = [quote]
        response = f'added {person} and added quote: {quote}'

    with open(json_file, 'w') as f:
        json.dump(quotes, f)

    print(
        f'👍 {GOGBOT} > {Fore.CYAN}{quote}{Style.RESET_ALL} added to {Fore.CYAN}{person}\'s{Style.RESET_ALL} quotes'
    )
    await ctx.send(response)


@bot.command(name='gog', help='Pray to Gog and receive his reply.')
async def gog(ctx):
    """Echoes a string composed of different variations of `gog`
    """
    gog_list = [
        'gog ', 'gogger ', 'gogging ', 'gogged ', 'gogs ', 'goggers ',
        'goggings ', 'gog '
    ]
    response = ''
    for _ in range(1, random.randint(1, 300)):
        response += random.choice(gog_list)

    print(f'🙏 {GOGBOT} > gog')
    await ctx.send(f'📖 Gog said: {response}')


bot.run(TOKEN)
