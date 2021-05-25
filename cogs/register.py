from discord.ext import commands
from functions import sql
from various import colored_terminal as cterm
from string import ascii_letters
from random import choice
from functions import get_profile
import discord
import asyncio
class Command_Class_Register(commands.Cog):
    def __init__(self, client):
        self.client = client
       
    @commands.command(pass_context = True, aliases=['kaydol', 'kayıt ol', 'register', 'signup', 'sign up'])
    async def kayıt(self, ctx):
      await ctx.send("Karakterin için bir kullanıcı adı oluşturmalısın, 18 karakteri geçmeyen bir kullanıcı adı gir")
      channel=ctx.channel.id
      heroid=ctx.author.id
      def check(message):
          return message.author.id == heroid and message.channel.id == channel
      valid=False
      cancel=False
      count=1
      while not valid:
        if count==3:
          cancel=True
          valid=True
        msg = await self.client.wait_for('message', check=check)
        if len(msg.content) > 18:
          await msg.reply(f"Malesef 18 karakterden uzun kullanıcı adı kullanamazsın ({count}/3)\n> __{msg.content[:18]}__~~{msg.content[19:]}~~")
          count+=1
        else:
          username=msg.content
          valid=True
      if cancel:
        await ctx.send("Kayıt sürecinden çıkıldı")
        return
      reaction_message=await ctx.send('>>> Karakterinin dövüş stilini seçmelisin, ilerleyen zamanlarda bunu farklı bir yöne yönlendirebilirsin,\n`🏹` Uzak dövüş : İsabetli vuruşlarda sakatlama oranı yüksektir, hareket hızını düşürür.\n`⚔️` Yakın dövüş : Kritik hasar oranı daha yüksek hasarlar verir ')
      await reaction_message.add_reaction('🏹')
      await reaction_message.add_reaction('⚔️')
      def check(reaction, user):
          return user.id == heroid and (str(reaction.emoji) == '🏹' or str(reaction.emoji) == '⚔️')
      try:
          reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
      except asyncio.TimeoutError:
          await ctx.send("Zaman aşımından dolayı kayıt işlemi iptal edildi")
      if str(reaction.emoji) == '⚔️':
        tip="yakın"
      if str(reaction.emoji) == '🏹':
        tip="uzak"
      if not await sql.register(ctx.author.id, username, tip):
        await reaction_message.add_reaction('❎')
        await ctx.send("Sunucu taraflı hata meydana geldi")
        return
      await reaction_message.add_reaction('✅')
      spammsg=[]
      spammsg.append(f"{tip} sanatı seçildi")
      spammsg.append("Eternal'a hoşgeldin "+username)
      spammsg.append("Markete erişim `e market`")
      spammsg.append("Envanterini görmek için `e inv`")
      spammsg.append("profil `e profil`")
      spammsg.append("Tam liste için `e help`")
      spammsg.append("Markette item satabilir veya alabilirsin, unutma! alış fiyatı satış fiyatından hep yüksek olur")
      spammsg.append("Markette item satmak için `e  market sell {item} {miktar}` miktar değeri girilmezse 1 adet satılır.")
      spammsg.append("İtemlerin fiyatları gün içinde değişebilir, hemen satmadan önce doğru zamanı beklemek isteyebilirsin.")
      spammsg.append("Güncel satış fiyatlarına`e market stat` ile ulaşabilirsin")
      spammsg.append("Markette satacak eşya bulmak için haritada gezinmelisin detaylı bilgi `e help avcılık`")
      spammsg_log=[]
      wein=0
      maxin=len(spammsg)
      showing=True
      send=True
      delete=False
      while showing:
        action=False
        if send:
          action=True
          try:
            spammsg_log.append(await ctx.send (spammsg[wein]))
            wein+=1
            if not delete and len(spammsg_log)>3:
              delete=True
          except IndexError:
            send=False
        if delete:
          action=True
          try:
            await spammsg_log[0].delete()
            spammsg_log.pop(0)
          except IndexError:
            delete=False
        if not action:
          showing=False
        else:
          await asyncio.sleep(3)
      embed=await get_profile.embed(ctx.author)
      await ctx.send(embed=embed)
    @kayıt.error
    async def kayıt_error(self, ctx, error):
      error_identity = ''.join(choice(ascii_letters) for _ in range(5))
      temp = await ctx.send ("Bir sorun oldu, sorun kodu: "+error_identity)
      cterm.p.red(error_identity, " "+str(error))
def setup(bot):
    bot.add_cog(Command_Class_Register(bot))