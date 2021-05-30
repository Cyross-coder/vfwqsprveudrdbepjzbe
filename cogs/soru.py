from discord.ext import commands
from various import colored_terminal as cterm
from string import ascii_letters
import discord
from various import sorular
import asyncio
from random import choice
import traceback
async def oyun(client, ctx, oyuncular):
  print(len(oyuncular))
  if len(oyuncular) < 2:
    return await ctx.send("yetersiz katılımcı")
  mevcut_oyuncu=0
  kaldık=0
  hazne =[]
  for i in range(sorular.max()):
    hazne.append(i)
  condition = True
  sorukodu=choice(hazne)
  hazne.pop(hazne.index(sorukodu))
  while condition:
    kaldık+=1
    soru=sorular.soru18(sorukodu)
    __=await ctx.send(f"soru **{kaldık}**, {oyuncular[mevcut_oyuncu].mention} senin sorun şu: ```\n{soru}\n```\n yanıtladıysan ✅, ayrıca soruyu geçebilir veya oyundan çıkabilirsin")
    await __.add_reaction("✅")
    await __.add_reaction("⏭️")
    await __.add_reaction("❌")
    def check(reaction, user):
      return user.id == oyuncular[mevcut_oyuncu].id and (str(reaction.emoji) == "✅" or str(reaction.emoji) ==  "⏭️" or str(reaction.emoji) ==  "❌" )
    reaction, user = await client.wait_for('reaction_add', check=check)
    def owner(message, user):
      return user.id == oyuncular[mevcut_oyuncu].id and message.content.startswith('-')
    if str(reaction.emoji) == "✅":
      sorukodu=choice(hazne)
      try:
        hazne.pop(sorukodu)
      except:
        pass
      if mevcut_oyuncu+1 >= len (oyuncular):
        mevcut_oyuncu =0
      else:
        mevcut_oyuncu=mevcut_oyuncu+1
    elif str(reaction.emoji)== "⏭️":
      await ctx.send("Soru geçildi")
      sorukodu=choice(hazne)
    elif str(reaction.emoji) == "❌" : 
      await ctx.send("bb")
      oyuncular.pop(mevcut_oyuncu)
      if len(oyuncular) == 1:
        break
      if mevcut_oyuncu+1 > len (oyuncular):
        mevcut_oyuncu =0
      else:
        mevcut_oyuncu=mevcut_oyuncu+1
    
class Command_Class_Soru(commands.Cog):
    def __init__(self, client):
        self.client = client
       
    @commands.command(pass_context = True)
    async def soru(self, ctx):
      oyuncu=[]
      _ = await ctx.send("Soru odası kuruldu, katılımcılar 20 saniye içinde lolipopu yalasın")
      await _.add_reaction('🍭')
      await asyncio.sleep(20)
      __= await _.channel.fetch_message(_.id)
      async for user in __.reactions[0].users():
        if not user.id == self.client.user.id:
          oyuncu.append(user)
      print(user)
    #  await ctx.send(str(len(oyuncu))+ "katılımcıyla devam ediliyor, soruyu yanıtmak için yanıtının başına - koy, yanıtın oylamaya açılacak, ayrıca soruyu geçebilirsin ama bu da oynamaya açılacak, oylamasız olarak oyundan çıkabilirsin. oyunda 2 kişiden az kişi kalırsa oyun biter.")
      await oyun(self.client, ctx, oyuncu)
      await ctx.send("oyun bitti")
    @soru.error
    async def purge_error(self, ctx, error):
      error_identity = ''.join(choice(ascii_letters) for _ in range(5))
      temp = await ctx.send ("Bir sorun oldu, sorun kodu: "+error_identity)
      cterm.p.red(error_identity, " "+str(error))
      traceback.print_exc()
def setup(bot):
    bot.add_cog(Command_Class_Soru(bot))