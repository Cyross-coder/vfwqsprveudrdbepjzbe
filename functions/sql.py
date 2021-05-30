import sqlite3
def login():
  filename="database.sql"
  return sqlite3.connect(filename)
  
"""
Preparr the database for tables,
this will let us easily purge database when necessary
keep this shit up to date
"""
vt=login()
im=vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS 'players'
('id', 'username', 'money', 'xp', 'okcu', 'ydvs')""")
im.execute("""CREATE TABLE IF NOT EXISTS 'battles' ('1', '2')""")
vt.close()
async def register(_id, _username, _stage):
  try:
    default={
      'money': 250,
      'xp': 0,
      'tier_level': 2
    }
    _username=_username.replace('"', '')
    okcu = 250 if _stage == 'uzak' else 0
    yakın = 250 if _stage == 'yakın' else 0
    vt=login()
    im=vt.cursor()
    im.execute(f"""INSERT INTO players (id, username, money, xp, okcu, ydvs) VALUES ("{_id}", "{_username}", "{default['money']}", "{default['xp']}", "{okcu}", "{yakın}")""")
    vt.commit()
    vt.close()
    return True
  except Exception as e:
    print(e)
    return False
async def is_user_registered(_id):
  vt=login()
  im=vt.cursor()
  _ = True if len(im.execute(f"SELECT * FROM players WHERE id='{_id}'").fetchall()) > 0 else False
  vt.close()
  return _
async def get_xp(_id):
  if not await is_user_registered(_id):
    return False
  vt=login()
  im=vt.cursor()
  _ = im.execute(f"SELECT xp FROM players WHERE id='{_id}'").fetchall()[0][0]
  vt.close()
  return str(_)
async def get_username(_id):
  vt=login()
  im=vt.cursor()
  _ = im.execute(f"SELECT username FROM players WHERE id='{_id}'").fetchall()[0][0]
  vt.close()
  return str(_)
async def bolum_xp(_id):
  vt=login()
  im=vt.cursor()
  _ = im.execute(f"SELECT okcu FROM players WHERE id='{_id}'").fetchall()[0][0]
  __ = im.execute(f"SELECT ydvs FROM players WHERE id='{_id}'").fetchall()[0][0]
  Object=[_, __]
  vt.close()
  return Object
async def get_money(_id):
  if not await is_user_registered(_id):
    return False
  vt=login()
  im=vt.cursor()
  _ = im.execute(f"SELECT money FROM players WHERE id='{_id}'").fetchall()[0][0]
  vt.close()
  return str(_)
  
async def is_battleowner(_id):
  if not await is_user_registered(_id):
    return False
  vt=login()
  im=vt.cursor()
  _=im.execute(f"SELECT * FROM 'battles' WHERE 1='{_id}'").fetchall()
  vt.close()
  return True if len(_) > 0 else False
async def is_battlereceiver(_id):
  if not await is_user_registered(_id):
    return False
  vt=login()
  im=vt.cursor()
  _=im.execute(f"SELECT * FROM 'battles' WHERE 2='{_id}'").fetchall()
  vt.close()
  return True if len(_) > 0 else False
async def closebattle(_id):
  if not is_user_registered(_id):
    return "Kayıtlı değil"
  vt=login()
  im=vt.cursor()
  if is_battleowner(_id):
    im.execute(f"DELETE FROM 'battles' WHERE 1='{_id}'")
  elif is_battlereceiver(_id):
    im.execute(f"DELETE FROM 'battles' WHERE 2='{_id}'")
  else:
    return False
async def startbattle(_, __):
  print (" f")