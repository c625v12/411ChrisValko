# Project: app1 implementation
# Purpose Details:
#       app1 will send the secure payload to app2 using TLS.
#       All workflow actions pass or fail will be logged into
#       the activity MongoDB NoSQL database with a timestamp.
#       Unit tests will confirm all methods are functional.
# Course: IST 411
# Author: Chris Valko <cjv5110@psu.edu>
# Date Developed: 10/3/2018
# Last Date Changed: 10/3/2018
# Rev:
# ----------------------------
import json, sys, urllib.parse, urllib.request, urllib.error, socket, ssl, Logger


class App1:
	__logger = Logger.Logger()
	def client_ssl(self):

		url = "https://jsonplaceholder.typicode.com"
		param = "/posts/1/comments"

		try:
			self.__logger.log("Client connecting on port 8080 using SSL")
			clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			ssl_sock = ssl.wrap_socket(clientsocket,
				ca_certs="server.crt",
				cert_reqs=ssl.CERT_REQUIRED)
			self.__logger.log("Connected to host using SSL")
			ssl_sock.connect(('localhost', 8080))
			self.__logger.log("Opening URL")
			response = urllib.request.urlopen(url+param)
			self.__logger.log("Reading URL")
			clientJSON = response.read()
			serverPrint = json.loads(clientJSON.decode('utf-8'))
			self.__logger.log("Sending JSON")
			ssl_sock.sendall(clientJSON)
			self.__logger.log("Saving JSON text file")
			with open('serverSentInfo.json', 'w') as outFile:
				jsonPayload = outFile.write(json.dumps(serverPrint))

		except Exception as e:
			self.__logger.log("Exception in SSL client")
			print(e)
			print(ssl_sock.cipher())
			ssl_sock.close()


if __name__ == '__main__':
	app1 = App1()
app1.client_ssl()
