# Project: Web service lab with ssl
# Purpose Details: Send data to server with ssl
# Course: IST 411
# Author: Chris Valko
# Date Developed: 10/1/2018
# Last Date Changed:10/1/2018
# Rev:1
# serverssl.py SSL uses port 443 by default but for this example I used 8080
import socket, ssl
try:
	print("create an INET, STREAMing socket using SSL")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ssl_sock = ssl.wrap_socket(s,
		server_side=True,
		certfile="server.crt",
		keyfile="server.key")
	print("bind the socket to a public host, and a well-known port 8080")
	ssl_sock.bind(('localhost', 8080))
	ssl_sock.listen(8080)
	print("ciphers: " + str(ssl_sock.cipher()))
	while True:
		print("accept connections from outside")
		(clientsocket, address) = ssl_sock.accept()
		serverAcceptedData = clientsocket.recv(8080).decode()
		print(serverAcceptedData)
except Exception as e:
	print(e)
	ssl_sock.close()
