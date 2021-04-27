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

GOGBOT = '{Fore.CYAN}{bot.user.name}{Style.RESET_ALL}'


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(f'🚀 {Fore.CYAN}{bot.user.name}{Style.RESET_ALL} has connected to {Fore.CYAN}{guild.name}{Style.RESET_ALL}')


@bot.command(name='quote', help='funny')
async def quote(ctx, person: str):
<<<<<<< HEAD
    print(
        f'🚀 {Fore.CYAN}{bot.user.name}{Style.RESET_ALL} > Quote for {person} requested. . .')
    people = {'fred': ['dude', 'wanna try my dubai tobacco', '*inhales vape*'],
=======
    print(f'🚀 Quote for {person} requested. . .')
    people = {'fred': ['dude', '*vapes*'],
>>>>>>> e8094245cdb2d38ae0a67c0c6680a83530e550c2
              'crocker': ['Chemistry', 'elliot', 'gog', 'joji'],
              'matt': ['Chemistry', 'gogger', 'gog', '🤙🤙'],
              'jude': ['mysterious', 'girl', 'rampage'],
              'joel': ['🍆']}
    response = ''
    if person in people:
        response = random.choice(people[person])
    else:
        response = f'{person} 🥶'
    print(f'👍 {Fore.CYAN}{bot.user.name}{Style.RESET_ALL} > Replied: {response}')
    await ctx.send(response)


@bot.command(name='gog', help='Pray to Gog and receive his reply.')
async def gog(ctx):
    gog_list = ['gog ', 'gogger ', 'gogging ', 'gogged ',
                'gogs ', 'goggers ', 'goggings ', 'gog ']
    response = ''
    for _ in range(1, random.randint(1, 300)):
        response += random.choice(gog_list)
    print(f'🙏 {Fore.CYAN}{bot.user.name}{Style.RESET_ALL} > gog')
    await ctx.send(f'📖 Gog said: {response}')


bot.run(TOKEN)
