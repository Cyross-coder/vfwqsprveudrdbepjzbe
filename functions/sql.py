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
  