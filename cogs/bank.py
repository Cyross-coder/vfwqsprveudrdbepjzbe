from discord.ext import commands
from functions import sql
from various import colored_terminal as cterm
from string import ascii_letters
from random import choice
import discord
class Command_Class_Bank(commands.Cog):
    def __init__(self, client):
        self.client = client
       
    @commands.command(pass_context = True, aliases=['bank', 'para', 'zula'])
    async def money(self, ctx, who: discord.Member = None):
      who = ctx.author if who == None else who
      money = await sql.get_money(who.id)
      if not money == False:
        await ctx.send(f">>> {who.mention} {money}")
      else:
        await ctx.send("Kayıtlı değil")
    @money.error
    async def money_error(self, ctx, error):
      error_identity = ''.join(choice(ascii_letters) for _ in range(5))
      temp = await ctx.send ("Bir sorun oldu, sorun kodu: "+error_identity)
      cterm.p.red(error_identity, " "+str(error))
def setup(bot):
    bot.add_cog(Command_Class_Bank(bot))