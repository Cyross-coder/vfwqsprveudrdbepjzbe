#proudly stolen from https://github.com/Willy-JL/Animate-My-Emojis/
from discord.ext import commands
import discord
from various import colored_terminal as cterm
from string import ascii_letters
from random import choice
class Command_Class_Spam(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def spam(self, ctx, x, *icerik):
      if not int(x):
        return await ctx.send("e spam 5 spam mesajı")
      if int(x) > 20:
        return await ctx.send("ebenin amı")
      webhook=await ctx.channel.create_webhook(name="duck")
      for _ in range(int(x)):
        await webhook.send(username=ctx.author.display_name,
                       avatar_url=ctx.author.avatar_url,
                       content=" ".join(y for y in icerik)
                       )
      await webhook.delete()
            
    @spam.error
    async def spam_error(self, ctx, error):
      error_identity = ''.join(choice(ascii_letters) for _ in range(5))
      temp = await ctx.send ("Bir sorun oldu, sorun kodu: "+error_identity)
      cterm.p.red(error_identity, " "+str(error))
def setup(bot):
    bot.add_cog(Command_Class_Spam(bot))