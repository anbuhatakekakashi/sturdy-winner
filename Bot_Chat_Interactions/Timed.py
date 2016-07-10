import time
import random
import threading

from datetime import datetime

from Connect import openSocket, sendMessage
from Read import getUser, getMessage
from Library import PICOFTHEDAY, ANIMEOFTHEDAY, SONGOFTHEDAY
from Library import AD1, AD2, AD3

def oftheDay(s):
     #threading.Timer(10.0, oftheDay).start() #trying some threading not working
     
     redaily     = [("%s" % PICOFTHEDAY),
                    ("%s" % ANIMEOFTHEDAY),
                    ("%s" % SONGOFTHEDAY), 
                    ("%s" % AD1 + AD2 + AD3)
                    ]
     
     sendMessage(s, random.choice(redaily))
     
