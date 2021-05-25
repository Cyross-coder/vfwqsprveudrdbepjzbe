from discord.ext import commands
import aiohttp
import re
import discord

class ClassName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command()
    async def command(self, ctx):
      
    @command.error
      
def setup(bot):
    bot.add_cog(ClassName(bot))