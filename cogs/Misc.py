# Cog for misc commands
import discord
from discord.ext import commands
import requests
import json
import platform

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

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # hello command 
    @commands.command(aliases = ['hi'], brief = 'Says hello!', description = 'Says hello!')
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")

    # deletes user's command and sends the text provided
    @commands.command(brief = "Deletes your command and sends the text provided.", description = "Makes it appear as if the bot sent the text you provided without a prompt. ")
    async def echo(self, ctx, *, message=None):
        message = message or "Please provide the message to be repeated."
        await ctx.message.delete()
        await ctx.send(message)

    # says random dish command
    @commands.command(brief = 'Says a random dish', description = 'Replies with a random dish from https://random-data-api.com/api/food/random_food')
    async def dish(self, ctx):
        dish = get_dish()
        await ctx.send(dish)

    # provides random inspirational quote
    @commands.command(brief = 'Provides an inspiring quote', description = 'Replies with a random quote from https://zenquotes.io/api/random')
    async def inspire(self, ctx):
        quote = get_quote()
        await ctx.send(quote)

    # basic stats command
    @commands.command(brief = 'Displays some bot stats')
    async def stats(self, ctx):
        py_version = platform.python_version()
        discord_py_version = discord.__version__
        server_count = len(self.bot.guilds)
        member_count = len(set(self.bot.get_all_members()))
        await ctx.send(f"I am in {server_count} guilds with a total of {member_count} members. \nPython version: {py_version} \nDiscord.py version: {discord_py_version}")

def setup(bot):
    bot.add_cog(Misc(bot))
