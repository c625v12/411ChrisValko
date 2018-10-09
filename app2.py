import socket
import ssl

import Logger


class App2:
    __logger = Logger.Logger()

    def server_ssl(self):
        """
        Initiate TLS connection and receive data
        """
        try:
            self.__logger.log("Initiate the socket connection")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__logger.log("SSL connection")
            ssl_sock = ssl.wrap_socket(s,
                                       server_side=True,
                                       certfile="server.crt",
                                       keyfile="server.key")

            self.__logger.log("Set the localhost and port")
            ssl_sock.bind(('localhost', 8080))
            ssl_sock.listen(5)

            while True:
                self.__logger.log("While loop: accept clients")
                (client_socket, address) = ssl_sock.accept()
                data = client_socket.recv(1024)

                if not data: break

                self.__logger.log("Data receiving")
                print("Data Received:")
                print("==============")
                print(data.decode('utf-8'))

        except Exception as e:
            self.__logger.log("Exception in SSL server")
            print(e)


if __name__ == '__main__':
    app2 = App2()
app2.server_ssl()
