from discord.ext import commands
from various import colored_terminal as cterm
from various import secs_to_date as nicetime
from various import delete_messages_older_thn
from time import time as current_time
from various import resource_usage
import discord
import os
import signal
import multiprocessing
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-hr", "--heroku", help="if running on heroku",
                    action="store_true")
args = parser.parse_args()
fspc = lambda text, t=2: ('\t'*t)+text[1:] if text.startswith(' ') else ('\t'*t)+text
short = lambda text, max=15: text if not len(text) >= max else text[:max-5]+'...'+text[-2:]
if args.heroku:
  discord_token=os.environ['token']
else:
  with open("token", "r") as tokenfile:
    discord_token=tokenfile.readlines()[0]
    
outages=[]
first_connect=False
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='e ', intents=intents)
@bot.event
async def on_connect():
    global outages, first_connect
    if first_connect:
      outages.append(current_time())
      cterm.p.red("Bağlantı kopukluğu oldu ", nicetime.nicetime(outages[-1]))
    else:
      print('--------------------')
      cterm.p.green('Giriş yapıldı', fspc(bot.user.name, 3))
      first_connect=True
      for cog in os.listdir('./cogs'):
        if cog.endswith('.py') and not cog.startswith('_'):
          try:
            bot.load_extension("cogs."+cog.split('.')[0])
            cterm.p.green(short('./cogs/'+cog), fspc('Sınıfı başarıyla yüklendi ve aktif'))
          except Exception as e:
            cterm.p.red('./cogs/'+cog, fspc(str(e).split(':')[-1]))
      def handler(signum, frame):
        print('')
      signal.signal(signal.SIGINT, handler)
      try:
        await resource_usage.main(60)
      except KeyboardInterrupt:
        print('')


#bot.loop.create_task(delete_messages_older_thn.main(bot, 500, 839836362232430596))
print('Giriş yapılıyor...')
try:
   bot.run(discord_token)
except Exception as e:
   cterm.p.red('çalışma hatası', fspc(str(e)))