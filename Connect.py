import socket

from Settings import HOST, PORT, PASS, NICK, CHANNEL

def openSocket():
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.send("PASS " + PASS + "\r\n")
	s.send("NICK " + NICK + "\r\n")
	s.send("JOIN #" + CHANNEL + "\r\n")
	return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	
	s.send(messageTemp + "\r\n")
	
	print("Sent: " + messageTemp)
