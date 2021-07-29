import discord
from discord.ext import commands
import platform


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

 

    
    @commands.command(brief = 'Divides two given numbers', description = 'Input = ')
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

def setup(bot):
    bot.add_cog(Math(bot))