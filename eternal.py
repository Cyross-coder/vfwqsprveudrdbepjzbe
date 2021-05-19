# eternal
import os
token=os.getenv("token")
import discord
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
    await ctx.send(ctx.message.guild.icon_url)
    return
  else:
    await ctx.send("ben o kadar zeki değilim")
@soru.error
async def server(ctx, devami):
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

client.run(token)