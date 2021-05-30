from discord.ext import commands
from functions import sql
from various import colored_terminal as cterm
from string import ascii_letters
from random import choice
import discord
class Command_Class_Purge(commands.Cog):
    def __init__(self, client):
        self.client = client
       
    @commands.command(pass_context = True)
    async def purge(self, ctx, amount=25):
      ident = ''.join(choice(ascii_letters) for _ in range(8))
      m=await ctx.channel.history(limit=amount).flatten()
      await ctx.send(f"mesaj silimine başlandı, sıra kodu:{ident}")
      for t in m:
        await t.delete()
      await ctx.send(f"görev: {ident} tamamlandı")
    @purge.error
    async def purge_error(self, ctx, error):
      error_identity = ''.join(choice(ascii_letters) for _ in range(5))
      temp = await ctx.send ("Bir sorun oldu, sorun kodu: "+error_identity)
      cterm.p.red(error_identity, " "+str(error))
def setup(bot):
    bot.add_cog(Command_Class_Purge(bot))