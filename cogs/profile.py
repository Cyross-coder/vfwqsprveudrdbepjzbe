from discord.ext import commands
from functions import get_profile
from string import ascii_letters
from random import choice
from various import colored_terminal as cterm
import discord
import traceback
class Command_Class_Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command()
    async def profil(self, ctx, who:discord.Member = None):
      who = ctx.author if who == None else who
      embed=await get_profile.embed(who)
      await ctx.send(embed=embed)
    @profil.error
    async def profil_error(self, ctx, error):
      error_identity = ''.join(choice(ascii_letters) for _ in range(5))
      temp = await ctx.send ("Bir sorun oldu, sorun kodu: "+error_identity)
      cterm.p.red(error_identity, " "+str(error))
      traceback.print_exc()
def setup(bot):
    bot.add_cog(Command_Class_Profile(bot))