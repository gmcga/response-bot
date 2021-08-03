# Response Bot
import discord 
from discord.ext import commands
import os
import json
from dotenv import load_dotenv
import logging
import sys, traceback
from pathlib import Path

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-_-")
# cogs used
initial_extensions = [
                    'cogs.Math', 
                    'cogs.Misc'
                     ]

bot = commands.Bot(command_prefix='!', case_insensitive=True, activity = discord.Game(name = "!help for commands list!", owner_id=282914357048770561))
load_dotenv()
TOKEN = os.getenv("TOKEN")
logging.basicConfig(level=logging.INFO)

bot.blacklisted_users = []

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
    print(f'\nLogged in as: {bot.user.name} :: ID {bot.user.id} :: Current prefix: "!"\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n')
    data = read_json("blacklist")
    bot.blacklisted_users = data["blacklistedUsers"]

# ignores messages sent by bot and blacklisted users
@bot.event
async def on_message(message): 
    if message.author.id == bot.user.id:
        return
    
    if message.author.id in bot.blacklisted_users: 
        return
    
    await bot.process_commands(message)

@bot.command(brief = "Blacklists a user", description = "Blacklists a user. Blacklisted users cannot use the bot.")
@commands.is_owner()
async def blacklist(ctx, user: discord.Member):
    if ctx.message.author.id == user.id:
        await ctx.send("Hey, you cannot blacklist yourself!")
        return

    bot.blacklisted_users.append(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].append(user.id)
    write_json(data, "blacklist")
    await ctx.send(f"Blacklisted {user.name}.")

@bot.command(brief = "Unblacklists a user", description = "Unblacklists a user. Blacklisted users cannot use the bot.")
@commands.is_owner()
async def unblacklist(ctx, user: discord.Member):
    bot.blacklisted_users.remove(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].remove(user.id)
    write_json(data, "blacklist")
    await ctx.send(f"Unblacklisted {user.name}.")

def read_json(filename):
    with open(f"{cwd}/bot_config/{filename}.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"{cwd}/bot_config/{filename}.json", "w") as file:
        json.dump(data, file, indent=4)

bot.run(TOKEN) 
