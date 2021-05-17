# eternal
import os
token=os.getenv("token")
import discord
import asyncio
import json
import time
from discord.ext import commands
from inc import soru as sorular

client = commands.Bot("-")
@client.event
async def on_connect():
  print(f"logged in as {client.user}")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="-help"))

@client.command()
async def soru(ctx):
  soru = sorular.soru18()
  await ctx.send(soru)
@soru.error
async def soru(ctx, devami):
        print(f'Hassikome! {ctx.author} | {devami}')

client.run(token)