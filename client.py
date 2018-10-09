import json, sys, urllib.parse, urllib.request, urllib.error, socket
# Project: Web service lab
# Purpose Details: Send data to server
# Course: IST 411
# Author: Chris Valko
# Date Developed: 9/19/2018
# Last Date Changed:9/21/2018
# Rev:1
url = "https://jsonplaceholder.typicode.com"
param = "/posts/1/comments"

try:
	print("Client connecting on port 8080")
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect((socket.gethostname(), 8080))
	response = urllib.request.urlopen(url+param)
	clientJSON = response.read()
	serverPrint = json.loads(clientJSON.decode('utf-8'))
	#print(serverPrint)
	clientsocket.sendall(clientJSON)
except Exception as e:
	print(e)
