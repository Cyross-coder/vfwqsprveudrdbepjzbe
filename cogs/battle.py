from discord.ext import commands
from functions import battle_fundamentals as kavga
from functions import get_profile, sql
from various import colored_terminal as cterm
from string import ascii_letters
from random import choice
import discord
async def run_battle(ctx, dumbs):
  #dumb 0 : battleowner
  #dumb 1 : other dumb
  #just so i can remember
  ctx.send("savaş başladı ama kod yok yayyam")
  return # i have to write the rest
  sql.block(dumbs[0], "Savaşta")
  sql.block(dumbs[1], "Savaşta")
  #blocked them to use commands
  
class Command_Class_Battle(commands.Cog):
    def __init__(self, client):
        self.client = client
       
    @commands.command(pass_context = True, aliases=['saldır', 'meydan oku'])
    async def battle(self, ctx, who: discord.Member = None):
      if who == None:
        await ctx.send('bu özellik henüz eklenmedi')
        #do stuff
      if await kavga.is_in_battle(ctx.author.id): 
        await ctx.send("meydan okuma başarısız, bekleyen meydan okuman var. `e kabul`/ `e reddet`")
        return
      if await kavga.is_in_battle(who.id):
        await ctx.send(f"meydan okuma başarısız, {who.mention}, bekleyen karşılaşman var, `e kabul`/ `e reddet`")
        return
      await kavga.start(ctx.author.id, who.id)
      embed=[get_profile.embed(ctx.author.id), get_profile.embed(who.id)]
      await ctx.send("Yeni meydan okuma", embed=embed)
    
    @commands.command(pass_context = True, aliases =['kabul'])
    async def accept(self, ctx):
      if not sql.is_battlereceiver(ctx.author.id):
        await ctx.reply(f"{ctx.mention}, bekleyen müsabakan yok")
      participants = await kavga.start(ctx.author.id)
      await kavga.close(ctx.author.id)
      await run_battle(participants)
    @accept.error
    async def accept_error(self, ctx, error):
      error_identity = ''.join(choice(ascii_letters) for _ in range(5))
      temp = await ctx.send ("Bir sorun oldu, sorun kodu: "+error_identity)
      cterm.p.red(error_identity, " "+str(error))
    @commands.command(pass_context=True, aliases=['Reddet'])
    async def decline(self, ctx):
      if not sql.is_battlereceiver(ctx.author.id):
         if await kavga.close(ctx.author.id):
           await ctx.reply("Atışma reddedildi")
         else:
           await ctx.send("bir sorun oldu")
      else:
       await ctx.reply("Kaçacak bir savaşın yok, 🐔")
    @decline.error
    async def decline_error(self, ctx, error):
      error_identity = ''.join(choice(ascii_letters) for _ in range(5))
      temp = await ctx.send ("Bir sorun oldu, sorun kodu: "+error_identity)
def setup(bot):
    bot.add_cog(Command_Class_Battle(bot))