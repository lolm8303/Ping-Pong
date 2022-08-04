import socket 
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 5555


try:
    ServerSocket.bind((host, port))
    print('The server is online!')

except socket.error as e:
    print(e)

ServerSocket.listen(2)

def thread_client(connection):
    while True:
        data = connection.recv(2048)
        # reply = f"Client said: {data.decode('utf-8')}"
        # print(reply)
        print(data.decode('utf-8'))
        
        if not data:
            break

    connection.close()

while True:
    Client, adresss = ServerSocket.accept()
    start_new_thread(thread_client, (Client,))

