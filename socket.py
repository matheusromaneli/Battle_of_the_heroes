import socket
from _thread import *
import sys

server = "192.168.1.71"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)

print("Wating connection...")

def threadead_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)
            
            conn.sendall(str.encode(reply))
        except:
            break
    
    conn.close()

while True:
    conn,addr = s.accept()
    print('conected to: ', addr)

    start_new_thread(threadead_client, (conn,))