from functions import sql

async def is_in_battle(_id):
  if await sql.is_battleowner(_id) or await sql.is_battlereceiver(_id):
    return True
  return False
async def start(_, __):
  if await is_in_battle(_) or await is_in_battle(__):
    return False
  try:
    await sql.startbattle(_, __)
    return True
  except Exception as e:
    print(e)
    return False
async def close(_):
  return await sql.closebattle(_)
