import sys
sys.path.insert(0, 'Bot_Chat_Interact')
sys.path.insert(0, 'Configurations')
sys.path.insert(0, 'Socket_Setup')

import time
import string
import threading

from Initialize import joinRoom
from Connect import openSocket, sendMessage

from Timed import oftheDay
from Read import getUser, getMessage
from Response import  customRespond, ohHey

def main():
     
     s = openSocket()
     joinRoom(s)
     readbuffer     = ""

     Reloading = True

     while (Reloading):
          
          readbuffer     = readbuffer + s.recv(1024)
          temp           = string.split(readbuffer, "\n")
          readbuffer     = temp.pop()
          
          for line in temp:
               print("LINE =====> %s" % line)
                    
               if "PING" in line:
                    oftheDay(s)
                    break
                    
               if "PING" in line:
                    s.send(line.replace("PING", "PONG"))
                    break
                    
               else:
                    ohHey(line, s)
                    customRespond(line, s)
                    
                    break

if __name__ == "__main__":
    main()
