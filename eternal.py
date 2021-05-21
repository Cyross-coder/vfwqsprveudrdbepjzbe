# eternal
with open("token", 'r') as x:
  token=x.readlines()[0]
import discord
import random
import asyncio
import json
import urllib.parse
import time as mtime
import sqlite3 as ssql
from datetime import datetime
from discord.ext import commands
from inc import soru as sorular
class sql:
    veritabanı=ssql.connect("veri.sql")
    im=veritabanı.cursor()
    im.execute("CREATE TABLE IF NOT EXISTS users (id INT(18) PRIMARY KEY, xp INT(30) NOT NULL DEFAULT '0', equips VARCHAR(50) NOT NULL DEFAULT '[]', inventory VARCHAR(255) NOT NULL DEFAULT '[]', charracter VARCHAR(255), datejoin TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    im.execute("CREATE TABLE IF NOT EXISTS battles (ilk INT(18), iki INT(18))")
    class defs:
      async def register(userid, charracter):
        sql.im.execute(f"INSERT INTO `table_name`(id,equips,charracter) VALUES ({userid},, 'yumruk', '{charracter}')")
        veritabanı.commit()
      async def is_registered(user_id):
        r=sql.im.execute(f"SELECT * FROM users WHERE id='{user_id}'")
        if len(r.fetchall()) > 0:
          return True
        else:
          return False
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
  class text:
    register = [
      "kayıt",
      "kayit",
      "kaydol",
      "register",
      ]
  class funcs:
    async def registered(_id):
      return await sql.defs.is_registered(_id)
    async def register_direct(userid, username):
      sql.defs.register(userid, username)
    async def register(ctx):
      channel=ctx.channel.id
      heroid=ctx.author.id
      registered=False
      while not registered:
        #embed
        await ctx.send(embed=embed)
        def check(message):
          return m.author.id == heroid and m.channel.id == channel
        valid=False
        while not valid:
          msg = await client.wait_for('message', check=check)
          if rpgame.defs.check_username_validity(msg.content):
             valid=True
             username=msg.content
          else:
            endstr="\n"
            if any(not c.isalnum() for c in msg.content):
              reason+="•Geçersiz karakter içeriyor "+c+endstr
            if len(msg.content) > rpgame.conf.username['max_lenght']:
              reason+="•İzin verilen uzunluk "+str(rpgame.conf.username['max_lenght'])+" karakter"+endstr
            ctx.send('**Hata**: Geçersiz kullancı adı, '+msg.content+'\n'+reason)
        await rpgame.defs.register_direct(ctx.author.id, username)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        spam1 = await ctx.send("Eternal'a hoşgeldin "+username)
        await asyncio.sleep(2)
        spam2 = await ctx.send("Komut listesi için -rpg help")
        await asyncio.sleep(2)
        spam3 = await ctx.send("Markete erişim -rpg market")
        await asyncio.sleep(1)
        await message.delete(spam2)
        spam4 = await ctx.send("Markette item satabilir veya alabilirsin, unutma! alış fiyatı satış fiyatından hep yüksek olur")
        await asyncio.sleep(3)
        await message.delete(spam3)
        spam5 = await ctx.send("Markette item satmak için `-rpg sell {item} {miktar}` miktar değeri girilmezse 1 adet satılır")
        await asyncio.sleep(2)
        await message.delete(spam4)
        spam6 = await ctx.send("Markette item satmak için `-rpg sell {item} {miktar}` miktar değeri girilmezse 1 adet satılır")
        await asyncio.sleep(2)
        await message.delete(spam6)
        spam7= await ctx.send("Güncel satış fifiyatlarına`rpg market stat` ile ulaşabilirsin")
        await asyncio.sleep(2)
        await message.delete(spam7)
        spam8= await ctx.send("Markette satacak eşya bulmak için haritaMarkette, detaylı bilgi `-rpg help avcılık`")
        await asyncio.sleep(3)
        await message.delete(spam8)
        await ctx.send('buraya profili resim olarak gösterticem 0xp fln klan yok fln fln')
    async def battlereq(who, _with):
      return False
    async def weapon(userid):
     # name=await mysql.equip(userid)
      name="yumruk"
      if not name == 'yumruk':
        return weapons[name]
      else:
        return 'yumruk'
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
      maps["Korumasız Dağlar"]={}
      maps["Korumasız Dağlar"]['description']="Olumsuz, burdan çıkış yok gibi. muhafızların pes edip burayı canavarlara bıraktığı kesin."
      maps["Korumasız Dağlar"]["specs"]={}
      maps["Korumasız Dağlar"]["specs"]["sp"]=0.7
      maps["Korumasız Dağlar"]["specs"]["m_speed"]=1.2
      maps["Korumasız Dağlar"]["specs"]["items_og"]={}
      maps["Binaiçi"]={}
      maps["Binaiçi"]['description']="Kapalı ortmda düşük item bulma olasılığı, ama güvenli, sakin."
      maps["Binaiçi"]["specs"]={}
      maps["Binaiçi"]["specs"]["sp"]=0.7
      maps["Binaiçi"]["specs"]["m_speed"]=1.2
      maps["Binaiçi"]["specs"]["items_og"]={}
  @client.command
  async def rpg(ctx, *all):
    if any(all[0] == c.lower() for c in rpgame.text.register):
      await rpgame.defs.register(ctx)
  @client.command()
  async def battle(ctx, _with: discord.Member = None, _map='random', difficulty='normal'):
    if not await rpgame.funcs.registered(ctx.author.id):
      embed=discord.Embed(title="Meydan okuma başarısız", description="Henüz bir karakter oluşturmadın?!\n`-rpg kayıt` kayıt ol", color=0xff0000)
      await ctx.send(embed=embed)
      return
    if not await rpgame.funcs.registered(_with.id):
      embed=discord.Embed(title="Meydan okuma başarısız", description="Hedefin bu dünyada yok .-.", color=0xff0000)
      await ctx.send(embed=embed)
      return
    if ctx.author.id==_with.id:
      embed=discord.Embed(title="Meydan okuma başarısız", description="Kendine saldıramazsın, baka!", color=0xff0000)
      await ctx.send(embed=embed)
      return
    if await rpgame.funcs.battlereq(ctx.author.id, _with.id):
      if _map=='random':
        _map=random.choice(rpgame.things.maps.mapdict)
        pmap=rpgame.things.maps.maps[_map]
      else:
        try:
          pmap=rpgame.things.maps.maps[_map]
        except:
          _map=random.choice(rpgame.things.maps.mapdict)
          pmap=rpgame.things.maps.maps[_map]
      embed=discord.Embed(title="Meydan okuma", description=f"{ctx.author.name}, {_with.name} meydan okuyor", color=0xde7a37)
      embed.add_field(name="Harita", value=f"{_map}\n*{pmap['description']}*", inline=False)
      embed.add_field(name=ctx.author.name, value=await rpgame.funcs.weapon(ctx.author.id), inline=True)
      embed.add_field(name=_with.name, value=await rpgame.funcs.weapon(_with.name), inline=True)
      await ctx.send(embed=embed)
    else:
      embed=discord.Embed(title="Meydan okuma başarısız", description="Senin veya karşı tarafın bekleyen meydan okuması var\n`-battle kb`: bekleyen meydan okumayı kabul et\n`-battle rb`: bekleyen meydan okumayı reddet", color=0xff0000)
      await ctx.send(embed=embed)
    
client.run(token)