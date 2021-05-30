from discord.ext import commands
from functions import sql
from various import colored_terminal as cterm
from string import ascii_letters
from random import choice
import discord
import datetime
import time as mtime
class Command_Class_User(commands.Cog):
    def __init__(self, client):
        self.client = client
       
    @commands.command(pass_context = True)
    async def user(self, ctx, what= None, who: discord.Member = None):
      who= ctx.author if who == None else who
      if what == "pp":
        await ctx.send(who.avatar_url)
      elif what == "profil":
        crdt=who.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
        time = mtime.time()
        c = time-(who.created_at).timestamp()
        years = int(c // 31104000)
        months = int(c // 2592000 % 12)
        days =int(c // 86400 % 30)
        hours =int(c // 3600 % 24)
        minutes = int(c // 60 % 60)
        seconds = int(c % 60)
        once=""
        if years > 0:
         once = once + str(years) + ' yıl '
        if months > 0:
         once = once + str(months) + ' ay '
        if days > 0:
         once = once + str(days) + ' gün '
        if hours > 0:
          once = once + str(hours) + ' saat '
        once = once + str(minutes) + ' dakika '
        once = once + str(seconds) + ' saniye'
        embed = discord.Embed(colour=discord.Color(0xffff00), timestamp=ctx.message.created_at,
                            title=f"User Info - {who}")
        embed.set_thumbnail(url=who.avatar_url)
        embed.set_footer(text=f"{ctx.author}'in isteği üzerine")
        embed.add_field(name="ID:", value=who.id)
        embed.add_field(name="Kullanıcı Adı", value=who.display_name)
        embed.add_field(name="Oluşturulma Tarihi:", value=f"{str(crdt)}\n**{once} önce**")
        await ctx.send(embed=embed)
    @user.error
    async def user_error(self, ctx, error):
      error_identity = ''.join(choice(ascii_letters) for _ in range(5))
      temp = await ctx.send ("Bir sorun oldu, sorun kodu: "+error_identity)
      cterm.p.red(error_identity, " "+str(error))
def setup(bot):
    bot.add_cog(Command_Class_User(bot))