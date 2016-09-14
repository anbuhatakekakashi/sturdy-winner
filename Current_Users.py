import sys
sys.path.insert(0, 'Configurations')

import json
import time
import urllib2
from sys import platform as _platform

from Settings import CHANNEL
from Library import levels
from Screen_Clear import clear

def main():
     while True:
          f    = urllib2.urlopen("https://tmi.twitch.tv/group/user/%s/chatters" % (CHANNEL))
          
          data = json.loads(f.read().decode("utf-8"))
          
          clear()
          
          print("Total chatters in %s: %d" % (CHANNEL, data["chatter_count"]))
          
          for user in data["chatters"]["viewers"]:
               print(user)
               
               usrList = open("VIEWED", 'a+')
               
               for line in open("VIEWED", 'a+'):
               usrList.seek(0, os.SEEK_SET)
                    if (user != line):
                         print("this")
                         usrList.write("%s\n" % user)
                         print("that")
               usrList.close()
               
          time.sleep(15)


if __name__ == "__main__":
    main()
