#Clone for responsebot math cog
import discord
from discord.ext import commands
import platform
import math



class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(brief = 'Divides two given numbers', description = 'Input: ')
    async def div(self, ctx, num1, num2):
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
    async def div_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('It needs two values')
    
    @commands.command(brief = 'Adds two given numbers', description = 'Input: ')
    async def add(self, ctx, num1, num2):
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

    @commands.command(brief = 'Subtracts two given numbers', description = 'Input: ')
    async def sub(self, ctx, num1, num2):
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

    @commands.command(brief = 'Multiplies two given numbers', description = 'Input: ')
    async def mul(self, ctx, num1, num2):
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

    @commands.command(brief = 'Finds the square root of a number', description = 'Input: ')
    async def root(self, ctx, num):
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

    @commands.command(brief = 'Squares a number', description = 'Input: ')
    async def squ(self, ctx, num):
        try: 
            num = float(num)
        except: 
            await ctx.send(f"Can't convert to float: '{num}'")
            return

        answer = num * num

        ans_em = discord.Embed(title='Square', description = f'Question: {num}^2\n\nAnswer: {answer}', colour = discord.Colour.from_rgb(153, 0, 76))

        await ctx.send(embed=ans_em)

    @commands.command(brief = 'Finds the factorial of a number', description = 'Input: ')
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

    @commands.command(brief = 'Exponentiates a number', description = 'Input: ')
    async def expo(self, ctx, num1, num2): 
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



def setup(bot):
    bot.add_cog(Math(bot))