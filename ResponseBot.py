# ResponseBot0.2
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


bot = commands.Bot(command_prefix='!', case_insensitive=True, activity = discord.Game(name = "!help for commands list!"))
load_dotenv()
TOKEN = os.getenv("TOKEN")
logging.basicConfig(level=logging.INFO)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def get_dish(): 
    response = requests.get("https://random-data-api.com/api/food/random_food")
    dish = response.json()["dish"] 
    return(dish) 

@bot.event
async def on_ready():
    print(f'\nLogged in as: {bot.user.name} :: {bot.user.id} :: Current prefix: "!"\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n')
       
@bot.command(aliases = ['hi'], brief = 'Says hello!', description = 'Says hello!')
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command(brief = 'Displays some bot stats')
async def stats(ctx):
    py_version = platform.python_version()
    discord_py_version = discord.__version__
    server_count = len(bot.guilds)
    member_count = len(set(bot.get_all_members()))
    await ctx.send(f"I am in {server_count} guilds with a total of {member_count} members. \nPython version: {py_version} \nDiscord.py version: {discord_py_version}")

@bot.command(brief = "Deletes your command and sends the text provided.", description = "Makes it appear as if the bot sent the text you provided without a prompt. ")
async def echo(ctx, *, message=None):
    message = message or "Please provide the message to be repeated."
    await ctx.message.delete()
    await ctx.send(message)


@bot.command(brief = 'Says a random dish', description = 'Replies with a random dish from https://random-data-api.com/api/food/random_food')
async def dish(ctx):
    dish = get_dish()
    await ctx.send(dish)

@bot.command(brief = 'Provides an inspiring quote', description = 'Replies with a random quote from https://zenquotes.io/api/random')
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)

@bot.command(brief = 'Divides two given numbers', description = 'Input = ')
async def div(ctx, num1, num2):
    try:
        num1 = float(num1)
    except:
        await ctx.send(f"Can't convert to float: '{num1}'")
        return

    try:
        num2 = float(num2)
    except:
        await ctx.send(f"Can't convert to float: '{num2}'")
        return
    
    if num2 == 0:
        await ctx.send("Can't divide by zero")
        return
        
    answer = num1 / num2

    ans_em = discord.Embed(title = 'Division', description = f'Question: {num1} / {num2}\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(252, 0, 252))
  
    await ctx.send(embed=ans_em)

@div.error
async def div_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('It needs two values')

@bot.command(brief = 'Adds two given numbers', description = 'Input: ')
async def add(ctx, num1, num2):
    try: 
        num1 = float(num1)
    except:
        await ctx.send(f"Can't convert to float: '{num1}'")    
        return
    
    try: 
        num2 = float(num2)
    except:
        await ctx.send(f"Can't convert to float: '{num2}'")    
        return
    
    answer = num1 + num2

    ans_em = discord.Embed(title='Addition', description = f'Question: {num1} + {num2}\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(252, 252, 0))
    
    await ctx.send(embed=ans_em)

@bot.command(brief = 'Subtracts two given numbers', description = 'Input: ')
async def sub(ctx, num1, num2):
    try: 
        num1 = float(num1)
    except:
        await ctx.send(f"Can't convert to float: '{num1}'")    
        return
    
    try: 
        num2 = float(num2)
    except:
        await ctx.send(f"Can't convert to float: '{num2}'")    
        return
    
    answer = num1 - num2

    ans_em = discord.Embed(title='Subtraction', description = f'Question: {num1} - {num2}\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(0, 252, 252))
    
    await ctx.send(embed=ans_em)

@bot.command(brief = 'Multiplies two given numbers', description = 'Input: ')
async def mul(ctx, num1, num2):
    try: 
        num1 = float(num1)
    except:
        await ctx.send(f"Can't convert to float: '{num1}'")    
        return
    
    try: 
        num2 = float(num2)
    except:
        await ctx.send(f"Can't convert to float: '{num2}'")    
        return
    
    answer = num1 * num2

    ans_em = discord.Embed(title='Multiplication', description = f'Question: {num1} x {num2}\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(60, 220, 28))
    
    await ctx.send(embed=ans_em)

@bot.command(brief = 'Finds the square root of a number', description = 'Input: ')
async def root(ctx, num):
    try: 
        num = float(num)
    except: 
        await ctx.send(f"Can't convert to float: '{num}'")
        return
    
    if num < 0: 
        await ctx.send(f"Number is not above zero: '{num}'")
        return

    answer = math.sqrt(num)

    ans_em = discord.Embed(title='Square Root', description = f'Question: sqrt({num})\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(255, 149, 9))

    await ctx.send(embed=ans_em)

@bot.command(brief = 'Squares a number', description = 'Input: ')
async def squ(ctx, num):
    try: 
        num = float(num)
    except: 
        await ctx.send(f"Can't convert to float: '{num}'")
        return

    answer = num * num

    ans_em = discord.Embed(title='Square', description = f'Question: {num}^2\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(153, 0, 76))

    await ctx.send(embed=ans_em)

@bot.command(brief = 'Finds the factorial of a number', description = 'Input: ')
async def fact(ctx, num):
    try: 
        num = float(num)
    except: 
        await ctx.send(f"Can't convert to float: '{num}'")
        return
    
    if num < 0:
        await ctx.send(f"Number is not greater than zero: '{num}'")
        return
    
    try: 
        math.factorial(num)
    except: 
        await ctx.send(f"Number is not an integer: '{num}'")
        return

    answer = math.factorial(num)

    ans_em = discord.Embed(title='Factorial', description = f'Question: {num}!\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(252, 252, 252))

    await ctx.send(embed=ans_em)

@bot.command(brief = 'Exponentiates a number', description = 'Input: ')
async def expo(ctx, num1, num2): 
    try:
        num1 = float(num1)
    except: 
        await ctx.send(f"Can't convert to float: '{num1}'")    
        return

    try:
        num2 = float(num2)
    except: 
        await ctx.send(f"Can't convert to float: '{num2}'")    
        return 

    try: 
        pow(num1, num2)
    except: 
        await ctx.send(f"Result too large (overflow error): '{num1}^{num2}'")
        return

    answer = pow(num1, num2)

    ans_em = discord.Embed(title='Exponent', description = f'Question: {num1}^{num2}\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(100, 100, 100))

    await ctx.send(embed=ans_em)

bot.run(TOKEN) 



