import asyncio
import resource
import asyncio
l=0

def wtf():
  global l
  l+=1 if l < 10 else 0
  return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if l > 2 else 0
async def main(max_mem):
  x=True
  while x:
    loop = asyncio.get_event_loop()
    lol = await loop.run_in_executor(None, wtf)
    part = max_mem // 15 # parts
    lol = lol // 1000
    if lol >= max_mem:
      exit(200)
    lol2 = str(lol) + ' MB'
    c = 0 #output
    while lol > 0:
      lol-=part
      c+=1
    i=0
    i_r=""
    i_part=part//7
    lol+=part
    lol=lol//part
    percdict={
      0: 'ඞ',
      1: "▏",
      2: "▎",
      3: "▍",
      4: "▌",
      5: "▋",
      6: "▊",
      7: "▉",
      8: "█" #idk, why not .-.
    }
    i_r = percdict[int(lol)]
    i = 1 if int(lol) > 0 else 0
    rbar = "["+("░"*15)+"]"
    rbar = rbar.replace("░", "█", c).replace("░", i_r, i)
    print(" ᴿᴬᴹ: ", rbar, lol2+"/"+str(max_mem)+" MB" "                ", end="\r")
    await asyncio.sleep(1)