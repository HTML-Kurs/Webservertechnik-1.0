
from socket import *
from _thread import start_new_thread


ECHO_PORT = 50007
BUFSIZE = 1024
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', ECHO_PORT))
s.listen( 1 )

def get(conn, remotehost, remoteport):
	print ('Verbunden mit %s:%s' % (remotehost, remoteport))
	
	while True:
		data = conn.recv(BUFSIZE).decode("utf-8")
		print ("Echo: %s" % (data))
		if not data:

			break

		conn.send(data.encode("utf-8"))


def main():
	
	
	
	print ("Server gestartet")
	
	# Warte auf eine Verbindung zum Server
	

	
	while True:
		conn, (remotehost, remoteport) = s.accept()
		start_new_thread(get, (conn, remotehost, remoteport,))

	s.close()

main()

