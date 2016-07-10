import random

from Read import getUser, getMessage
from Connect import openSocket, sendMessage
from Library import peeps, customre, greetings

def youSuck(line, s):
     user      = getUser(line.lower())
     message   = getMessage(line.lower())
     
     resuck    = [("No, you suck %s!" % user),
                  ("You can suck a  duck %s!" % user)]
                  
     if any(msg in message.split() for msg in suck):
          sendMessage(s, random.choice(resuck))

def ohHey(line, s):
     user      = getUser(line.lower())
     message   = getMessage(line.lower())
     
     rehey     = [("Bruv sup %s!" % user),
                  ("Nice to see you %s!" % user),
                  ("How's are your day been %s?" % user),
                  ("What's up %s?" % user)]
     
     if (any(msg in message.split() for msg in greetings)):
          sendMessage(s, random.choice(rehey))

def customRespond(line, s):
     user      = getUser(line.lower())
     message   = getMessage(line.lower())
     
     reply     = [("%s beat me so bad AhhSooCrazy owes him money!" % user), 
                 ("%s really gave it to AhhSooCrazy. Giggity!!!" % user)]
     
     if (user == "its_chris19"):
          if (any(msg in message for msg in customre)):
               sendMessage(s, random.choice(reply))
     
     if (user == "jwilson3571"):
          if (any(msg in message for msg in customre)):
               sendMessage(s, random.choice(reply))

