import time
import random

from datetime import datetime

from Connect import openSocket, sendMessage
from Read import getUser, getMessage
from Settings import PICOFTHEDAY, ANIMEOFTHEDAY
from Settings import SONGOFTHEDAY, JOKEOFTHEDAY
from Settings import AD1, AD2, AD3, AD4, AD5

def oftheDay(s):
     redaily     = [("Picture of the day: %s" % PICOFTHEDAY),
                    ("Anime of the day: %s" % ANIMEOFTHEDAY),
                    ("Song of the day: %s" % SONGOFTHEDAY),
                    ("Joke of the day: %s" % JOKEOFTHEDAY)]
                    
     sendMessage(s, random.choice(redaily))

def ADS(s):
     readvertise = [("%s" % AD1 + AD2 +AD3),
                    ("%s" % AD4 + AD5)]
                    
     sendMessage(s, random.choice(readvertise))

