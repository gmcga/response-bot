# Response Bot
from importlib.util import decode_source
import discord 
from discord.ext import commands
import requests
import json
import os
from dotenv import load_dotenv
import platform
from urllib import parse, request
import math
import logging
import sys, traceback

# cogs used
initial_extensions = ['cogs.Math']

bot = commands.Bot(command_prefix='!', case_insensitive=True, activity = discord.Game(name = "!help for commands list!"))
load_dotenv()
TOKEN = os.getenv("TOKEN")
logging.basicConfig(level=logging.INFO)

# get random quote function
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

# get random dish function
def get_dish(): 
    response = requests.get("https://random-data-api.com/api/food/random_food")
    dish = response.json()["dish"] 
    return(dish) 

# hello command 
@bot.command(aliases = ['hi'], brief = 'Says hello!', description = 'Says hello!')
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

# basic stats command
@bot.command(brief = 'Displays some bot stats')
async def stats(ctx):
    py_version = platform.python_version()
    discord_py_version = discord.__version__
    server_count = len(bot.guilds)
    member_count = len(set(bot.get_all_members()))
    await ctx.send(f"I am in {server_count} guilds with a total of {member_count} members. \nPython version: {py_version} \nDiscord.py version: {discord_py_version}")

# deletes user's command and sends the text provided
@bot.command(brief = "Deletes your command and sends the text provided.", description = "Makes it appear as if the bot sent the text you provided without a prompt. ")
async def echo(ctx, *, message=None):
    message = message or "Please provide the message to be repeated."
    await ctx.message.delete()
    await ctx.send(message)

# says random dish command
@bot.command(brief = 'Says a random dish', description = 'Replies with a random dish from https://random-data-api.com/api/food/random_food')
async def dish(ctx):
    dish = get_dish()
    await ctx.send(dish)

# provides random inspirational quote
@bot.command(brief = 'Provides an inspiring quote', description = 'Replies with a random quote from https://zenquotes.io/api/random')
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)

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



