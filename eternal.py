# eternal
token=os.getenv("token")
import discord
import asyncio
import json
import time
from inc import sorular

client = commands.Bot("-")
@client.event
async def on_connect():
  print(f"logged in as {client.user}")
  
await client.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name="-help"))