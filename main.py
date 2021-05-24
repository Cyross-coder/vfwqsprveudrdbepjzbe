from discord.ext import commands
from various import colored_terminal as cterm
from various import secs_to_date as nicetime
from time import time as current_time
outages=[]
first_connect=False
client = commands.Bot(command_prefix='e')
@client.event
async def on_connect():
    global outages, first_connect
    if first_connect:
      outages.append(current_time())
      cterm.p.red("Bağlantı kopukluğu oldu ", nicetime.nicetime(outages[-1]))
    else:
      print('--------------------')
      cterm.p.green('Giriş yapıldı')
      print(client.user.name)
      print(client.user.id)
      print(f"{len(client.guilds)} sunucuyla ilgeniyor")
      print('--------------------')
    first_connect=True
client.load_extension("cogs.register")
client.run("ODQzNjQ3ODQxODk2NzU5MzA2.YKG6Rw.P3r35gjMiyLyyWbUGThZ6jyNSfs")