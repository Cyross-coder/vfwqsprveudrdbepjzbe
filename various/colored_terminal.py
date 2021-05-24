import sys
class p:
  if sys.platform != "win32":
    def red(colored, uncolored=""):
       print(f"\033[1;31;40m{colored}\033[1;37;40m{uncolored}")
    def green(colored, uncolored=""):
       print(f"\033[1;32;40m{colored}\033[1;37;40m{uncolored}")
  else:
    def red(colored, uncolored=""):
       print(colored+uncolored)
    def green(colored, uncolored=""):
       print(colored+uncolored)
       