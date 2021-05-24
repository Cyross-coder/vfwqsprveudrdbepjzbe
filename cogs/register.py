from discord.ext import commands
#from functions import sql
from various import colored_terminal as cterm
from string import ascii_letters
from random import choice

class Command_Class_Register(commands.Cog):
    def __init__(self, client):
        self.client = client
       
    @commands.command(name="kayıt")
    async def command_1(self, ctx):
      channel=ctx.channel.id
      heroid=ctx.author.id
      print("somehow, im here")
      def check(message):
          return message.author.id == heroid and message.channel.id == channel
      valid=False
      cancel=False
      count=0
      while not valid:
        if count==3:
          cancel=True
          valid=True
        msg = await client.wait_for('message', check=check)
        if msg.content > 18:
          msg.reply(f"Malesef 18 karakterden uzun kullanıcı adı kullanamazsın ({count}/3)\n__{msg.content[:18]}__{msg.content[19:]}")
          count+=1
        else:
          username=msg.content
          valid=True
      if cancel:
        ctx.send("Kayıt sürecinden çıkıldı")
        return
      await channel.send('>>> Karakterinin dövüş stilini seçmelisin, ilerleyen zamanlarda bunu farklı bir yöne yönlendirebilirsin,\n`🏹` Uzak dövüş : İsabetli vuruşlarda sakatlama oranı yüksektir, hareket hızını düşürür.\n`⚔️` Yakın dövüş : Kritik hasar oranı daha yüksek hasarlar verir ')
      def check(reaction, user):
          return user == message.author and (str(reaction.emoji) == '🏹' or str(reaction.emoji) == '⚔️')
      try:
          reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
      except asyncio.TimeoutError:
          await ctx.send("Zaman aşımından dolayı kayıt işlemi iptal edildi")
      if str(reaction.emoji) == '⚔️':
        tip="yakındövüş"
      if str(reaction.emoji) == '🏹':
        tip="uzakdövüş"
        
    @command_1.error
    async def kayıt_error(self, ctx, error):
      error_identity = ''.join(choice(ascii_letters) for _ in range(5))
      temp = await ctx.send ("Bir sorun oldu, sorun kodu: "+error_identity)
      cterm.p.red(error_identity, " "+error)
def setup(bot):
    bot.add_cog(Command_Class_Register(bot))