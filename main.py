from discord.ext import commands
from various import colored_terminal as cterm
from various import secs_to_date as nicetime
from time import time as current_time
with open("token", "r") as tokenfile:
  discord_token=tokenfile.readlines()[0]
outages=[]
first_connect=False
bot = commands.Bot(command_prefix='e ')
@bot.event
async def on_connect():
    global outages, first_connect
    if first_connect:
      outages.append(current_time())
      cterm.p.red("Bağlantı kopukluğu oldu ", nicetime.nicetime(outages[-1]))
    else:
      print('--------------------')
      cterm.p.green('Giriş yapıldı')
      print(bot.user.name)
      print(bot.user.id)
      print(f"{len(bot.guilds)} sunucuyla ilgeniyor")
      print('--------------------')
    first_connect=True
bot.load_extension("cogs.register")
bot.load_extension("cogs.ping")
bot.load_extension("cogs.profile")
bot.run(discord_token)