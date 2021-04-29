import os
import random
from dotenv import load_dotenv

from colorama import Fore
from colorama import Style

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='$')

GOGBOT = f'{Fore.CYAN}GogBot{Style.RESET_ALL}'


@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(
            f'🚀 {GOGBOT} has connected to {Fore.CYAN}{guild.name}{Style.RESET_ALL}')


@bot.command(name='quote', help='funny')
async def quote(ctx, person: str):
    print(
        f'🚀 {GOGBOT} > Quote for {person} requested')
    people = {'fred': ['dude', '*vapes*'],
              'crocker': ['Chemistry', 'elliot', 'gog', 'joji'],
              'matt': ['Chemistry', 'gogger', 'gog', '🤙🤙'],
              'jude': ['mysterious', 'girl', 'rampage'],
              'joel': ['🍆']}
    response = ''
    if person in people:
        response = random.choice(people[person])
    else:
        response = f'{person} 🥶'
    print(f'👍 {GOGBOT} > Replied: {response}')
    await ctx.send(response)


@bot.command(name='gog', help='Pray to Gog and receive his reply.')
async def gog(ctx):
    gog_list = ['gog ', 'gogger ', 'gogging ', 'gogged ',
                'gogs ', 'goggers ', 'goggings ', 'gog ']
    response = ''
    for _ in range(1, random.randint(1, 300)):
        response += random.choice(gog_list)
    print(f'🙏 {GOGBOT} > gog')
    await ctx.send(f'📖 Gog said: {response}')


bot.run(TOKEN)
