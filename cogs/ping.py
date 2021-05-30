from discord.ext import commands
import discord

class testcode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command()
    async def ping(self, ctx):
      await ctx.reply("pong")
def setup(bot):
    bot.add_cog(testcode(bot))