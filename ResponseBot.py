# Response Bot
from importlib.util import decode_source
import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv
import platform
from urllib import parse, request
import logging
import sys, traceback

# cogs used
initial_extensions = [
                    'cogs.Math', 
                    'cogs.Misc'
                     ]

bot = commands.Bot(command_prefix='!', case_insensitive=True, activity = discord.Game(name = "!help for commands list!"))
load_dotenv()
TOKEN = os.getenv("TOKEN")
logging.basicConfig(level=logging.INFO)

# loads extensions (cogs)
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

# on_ready message
@bot.event
async def on_ready():
    print(f'\nLogged in as: {bot.user.name} :: {bot.user.id} :: Current prefix: "!"\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n')



bot.run(TOKEN) 
