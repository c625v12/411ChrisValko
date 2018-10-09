# Project: Web service lab with ssl
# Purpose Details: Send data to server with ssl
# Course: IST 411
# Author: Chris Valko
# Date Developed: 10/1/2018
# Last Date Changed: 10/1/2018
# Rev:1
import json, sys, urllib.parse, urllib.request, urllib.error, socket, ssl

url = "https://jsonplaceholder.typicode.com"
param = "/posts/1/comments"

try:
	print("Client connecting on port 8080 using SSL")
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ssl_sock = ssl.wrap_socket(clientsocket,
		ca_certs="server.crt",
		cert_reqs=ssl.CERT_REQUIRED)
	ssl_sock.connect(('localhost', 8080))
	response = urllib.request.urlopen(url+param)
	clientJSON = response.read()
	serverPrint = json.loads(clientJSON.decode('utf-8'))
	ssl_sock.sendall(clientJSON)
except Exception as e:
	print(e)
	print(ssl_sock.cipher())
	ssl_sock.close()
