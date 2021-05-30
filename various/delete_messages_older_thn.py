import discord, time, datetime, asyncio
async def main(Client, x, i):
  await Client.wait_until_ready()
  channel=Client.get_channel(i)
  m= await channel.history(limit=1000).flatten()
  for t in m:
     y =time.time() - t.created_at.timestamp()
     x=x+10800
     if y > x:
       await t.delete()
  await asyncio.sleep(10)