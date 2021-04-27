import random
import os
from colorama import Fore
from colorama import Style

from discord.ext import commands
from dotenv import load_dotenv

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
    print(
        f'🚀 {Fore.CYAN}{bot.user.name}{Style.RESET_ALL} > Quote for {person} requested. . .')
    people = {'fred': ['dude', 'wanna try my dubai tobacco', '*inhales vape*'],
              'crocker': ['Chemistry', 'elliot', 'gog', 'joji'],
              'matt': ['Chemistry', 'drink', 'gogger', 'gog', '🤙🤙'],
              'jude': ['mysterious', 'girl', 'rampager', 'otis'],
              'joel': ['ay']}
    response = ''
    if person in people:
        response = random.choice(people[person])
    else:
        response = f'{person} 🥶'
    print(f'👍 {Fore.CYAN}{bot.user.name}{Style.RESET_ALL} > Replied: {response}')
    await ctx.send(response)


@bot.command(name='fred')
async def fred(ctx):
    fred_quotes = ['dude', 'wanna try my dubai tobacco', '*inhales vape*']
    response = random.choice(fred_quotes)
    await ctx.send(response)


@bot.command(name='crocker')
async def crocker(ctx):
    crocker_quotes = ['Chemistry', 'elliot', 'gog', 'joji']
    response = random.choice(crocker_quotes)
    await ctx.send(response)


@bot.command(name='matt')
async def matt(ctx):
    matt_quotes = ['Chemistry', 'drink', 'gogger', 'gog', '🤙🤙']
    response = random.choice(matt_quotes)
    await ctx.send(response)


@bot.command(name='jude')
async def jude(ctx):
    jude_quotes = ['rampage', 'mysterious', 'girl']
    response = random.choice(jude_quotes)
    await ctx.send(response)


@bot.command(name='joel')
async def joel(ctx):
    joel_quotes = ['ay']
    response = random.choice(joel_quotes)
    await ctx.send(response)


@bot.command(name='gog', help='Pray to Gog and receive his reply.')
async def gog(ctx):
    gog_list = ['gog ', 'gogger ', 'gogging ', 'gogged ',
                'gogs ', 'goggers ', 'goggings ', 'gog ']
    response = ''
    for i in range(1, random.randint(1, 300)):
        response += random.choice(gog_list)
    print(f'🙏 {Fore.CYAN}{bot.user.name}{Style.RESET_ALL} > gog')
    await ctx.send(f'📖 Gog said: {response}')


bot.run(TOKEN)
