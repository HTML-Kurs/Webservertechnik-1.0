

from socket import *
from _thread import start_new_thread




SERVER_PORT = 50007
BUFSIZE = 1024
host = "127.0.0.1"

s = socket( AF_INET, SOCK_STREAM)
s.connect( (host, SERVER_PORT) )

def get():
	while True:
		print("Nachricht erhalten: " + s.recv( BUFSIZE ))





def main():

	
	while True:
		msg = input("Nachricht: ")
		s.send( msg.encode("utf-8") )
	
	
	 

	start_new_thread(get)

	s.close()

main()

