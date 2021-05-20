# eternal
import os
token=os.getenv("token")
import discord
import random
import asyncio
import json
from datetime import datetime
import time as mtime
from discord.ext import commands
from inc import soru as sorular
intents = discord.Intents.default()  
intents.members = True
client = commands.Bot("-", intents=intents)
@client.event
async def on_connect():
  print(f"logged in as {client.user}")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="-help"))

@client.command()
async def soru(ctx, num = "random"):
  soru = sorular.soru18(num)
  await ctx.send(soru)
@soru.error
async def soru(ctx, devami):
        print(f'Hassikome! {ctx.author} | {devami}')
@client.command()
async def server(ctx, what = None):
  if what == None:
    await ctx.send("serverin neyi?")
    return
  elif what == "pp" or what == "icon":
    await ctx.send(ctx.guild.icon_url)
    return
  else:
    await ctx.send("ben o kadar zeki değilim")
@server.error
async def server(ctx, devami):
        print(f'Hassikome! {ctx.author} | {devami}')
@client.command()
async def user(ctx, who: discord.Member, what = None):
  if what == None:
    await ctx.send("Kullanıcının neyi?")
    return
  elif what == "pp" or what == "avatar":
    await ctx.send(who.avatar_url)
    return
  else:
    await ctx.send("ben o kadar zeki değilim")
@user.error
async def user(ctx, devami):
        print(f'Hassikome! {ctx.author} | {devami}')
@client.command()
async def whois(ctx, member: discord.Member = None):
    dateTimeObj = datetime.now()
    hourtimestamp = dateTimeObj.hour, ':', dateTimeObj.minute
    if not member:
        member = ctx.message.author
    crdt=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
    time = mtime.time()
    c = time-(member.created_at).timestamp()
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
                        title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"{ctx.author}'in isteği üzerine")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Kullanıcı Adı", value=member.display_name)
    embed.add_field(name="Oluşturulma Tarihi:", value=f"{str(crdt)}\n**{once} önce**")
    await ctx.send(embed=embed)
@whois.error
async def whois_error(ctx, error):
    await ctx.reply("sorun oldu ://")
    print(error)
class rpgame:
  class things:
    class items:
      weapons={}
      weapons['Basit yay']={}
      weapons['Basit yay']["class"]="Sokak Eşyaları"
      weapons['Basit yay']["description"]="Eldeki eşyalarla yapılmış her an kırılacakmış gibi duran bir yay, en azından, ok atıyor.."
      weapons['Basit yay']['type']='bow'
      weapons['Basit yay']['range']={}
      weapons['Basit yay']['range']['max']=30
      weapons['Basit yay']['range']['nice']=10
      weapons['Basit yay']['atk']=5
      weapons['Basit yay']['req_slot_inv']=2
      weapons['Basit yay']['req_lvl']=0
      weapons['Basit yay']['rarity']=40
      weapons['Basit yay']['sellprice']=10
      
      weapons['Sarman yayı']={}
      weapons['Sarman yayı']["class"]="Sokak Eşyaları"
      weapons['Sarman yayı']["description"]="Kölelere yaptırılmış bu yay el işçiliği, malzemeden kaçılmış, ve, idare eder."
      weapons['Sarman yayı']['type']='bow'
      weapons['Sarman yayı']['range']={}
      weapons['Sarman yayı']['range']['max']=50
      weapons['Sarman yayı']['range']['nice']=15
      weapons['Sarman yayı']['atk']=9
      weapons['Sarman yayı']['req_slot_inv']=2
      weapons['Sarman yayı']['req_lvl']=0
      weapons['Sarman yayı']['rarity']=30
      weapons['Sarman yayı']['sellprice']=15
      
      weapons['Filkon yayı']={}
      weapons['Filkon yayı']["class"]="Muhafız"
      weapons['Filkon yayı']["description"]="Çok kullanımdan eskimiş bu yay muhafız eğitimlerinde kullanılır"
      weapons['Filkon yayı']['type']='bow'
      weapons['Filkon yayı']['range']={}
      weapons['Filkon yayı']['range']['max']=50
      weapons['Filkon yayı']['range']['nice']=15
      weapons['Filkon yayı']['atk']=11
      weapons['Filkon yayı']['req_slot_inv']=3
      weapons['Filkon yayı']['req_lvl']=0
      weapons['Filkon yayı']['rarity']=28
      weapons['Filkon yayı']['sellprice']=19
      
      weapons['Lirik yay']={}
      weapons['Lirik yay']["class"]="Mühendis"
      weapons['Lirik yay']["description"]="Karmaşık yapıya sahip bu yay klonlanamaz"
      weapons['Lirik yay']['type']='bow'
      weapons['Lirik yay']['range']={}
      weapons['Lirik yay']['range']['max']=40
      weapons['Lirik yay']['range']['nice']=25
      weapons['Lirik yay']['atk']=20
      weapons['Lirik yay']['req_slot_inv']=3
      weapons['Lirik yay']['req_lvl']=5
      weapons['Lirik yay']['rarity']=10
      weapons['Lirik yay']['sellprice']=25
      
      weapons['Eden kılıcı']={}
      weapons['Eden kılıcı']["class"]="Sokak Eşyaları"
      weapons['Eden kılıcı']["description"]="Çeşitli isyanlarda, isyancılar tarafından üretilip kullanılmış basit bir kılıç.. biraz, kör.."
      weapons['Eden kılıcı']['type']='sword'
      weapons['Eden kılıcı']['range']={}
      weapons['Eden kılıcı']['range']['max']=1
      weapons['Eden kılıcı']['range']['nice']=1
      weapons['Eden kılıcı']['atk']=7
      weapons['Eden kılıcı']['req_slot_inv']=3
      weapons['Eden kılıcı']['req_lvl']=0
      weapons['Eden kılıcı']['rarity']=70
      weapons['Eden kılıcı']['sellprice']=5
      
    class maps:
      mapdict=[
        "Terkedilmiş Vadi",
        "Korumasız Dağlar",
        "Binaiçi"
        ]
      maps={}
      maps["Terkedilmiş Vadi"]={}
      maps["Terkedilmiş Vadi"]['description']="Bir zamanlar yerleşimin olduğu bu düzlükte şimdi kimse yaşamıyor, savaşı doğanın kazandığı bu yerde hareket etmek güç"
      maps["Terkedilmiş Vadi"]["specs"]={}
      maps["Terkedilmiş Vadi"]["specs"]["sp"]=0.7
      maps["Terkedilmiş Vadi"]["specs"]["m_speed"]=1.2
      maps["Terkedilmiş Vadi"]["specs"]["items_og"]={}
  @client.command()
  async def start(ctx, _with: discord.Member = None, _map='random', difficulty='normal'):
    if _map=='random':
      pmap=rpgame.things.maps.maps[random.randint(0, len(rpgame.things.maps.mapdict))]
    await ctx.reply(pmap)
client.run(token)