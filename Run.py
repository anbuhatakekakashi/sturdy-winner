import time
import string

from Initialize import joinRoom
from Timed import oftheDay, ADS
from Read import getUser, getMessage
from Response import  youSuck, ohHey
from Connect import openSocket, sendMessage
from Response import ohBryan, ohDerek, ohJae

s = openSocket()
joinRoom(s)
readbuffer = ""

Reloading = True

while (Reloading):

     readbuffer = readbuffer + s.recv(1024)
     temp = string.split(readbuffer, "\n")
     readbuffer = temp.pop()

     for line in temp:
          print("LINE =====> %s" % line)
          
          
               
          if "PING" in line:
               oftheDay(s)
               break
               
          if "PING" in line:
               s.send(line.replace("PING", "PONG"))
               break
               
          else:
               ohBryan(line, s)
               ohDerek(line, s)
               ohJae(line, s)
               
               youSuck(line, s)
               ohHey(line, s)
               break
