from discord.ext import commands
from random import choice

cevaplar=[
  "olumlu bakmıyorum",
  "çok umutlu olma",
  "ayrı dünyalardansınız",
  "neden olmasın",
  "olur gibi",
  "hadi yine iyisin"]

class Kahin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command()
    async def kahin(self, ctx):
      await ctx.reply(choice(cevaplar))
def setup(bot):
    bot.add_cog(Kahin(bot))
