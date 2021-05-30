from functions import sql
from random import randint
async def addxp(_id, min = 10, max= 25):
  try:
    await sql.set_xp(_id, await sql.get_xp(_id)+randint(min, max))
    return True
  except Exception as e:
    print(e)
    return False
async def get_xp(_id):
  return await sql.get_xp(_id)

def stages(xp):
  xp=int(xp)
  xpx=xp
  formin = 1225 # for first level
  level = 0
  while True:
    level+=1
    xpx-=formin
    if xpx <= 0:
      break
    else:
      xp-=formin
      formin+=formin//5
  bpr=0
  x_=formin//15
  while xpx>0:
    bpr+=1
    xpx-=x_
  process_bar=("_"*15).replace("_", "#", bpr)
  Object= {
    'level': level,
    'current_xp': xp,
    'maxxp': formin,
    'bar': process_bar
  }
  return Object

def bolum_xp(xp):
  xp=int(xp)
  formin = 125 #startpoint
  level = 0
  if xp < formin:
    return 0
  while xp > formin:
    xp-=formin
    level+=1
  return level