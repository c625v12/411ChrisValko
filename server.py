import socket
# Project: Web service lab
# Purpose Details: Send data to server
# Course: IST 411
# Author: Chris Valko
# Date Developed: 9/19/2018
# Last Date Changed:9/21/2018
# Rev:1
try:
	print("create an INET, STREAMing socket")
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("bing the socket to a public host, and a well-known port 8080")
	serversocket.bind((socket.gethostname(), 8080))
	print("become a server socket")
	serversocket.listen(8080)
	while True:
		print("accept connections from outside")
		(clientsocket, address) = serversocket.accept()
		serverAcceptedData = clientsocket.recv(8080).decode() #decode to format it correctly
		print(serverAcceptedData)
except Exception as e:
	print(e)
