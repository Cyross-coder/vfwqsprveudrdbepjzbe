import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, '')
def nicetime(time: float):
  return datetime.fromtimestamp(time).strftime("%A, %B %d, %Y %I:%M:%S")