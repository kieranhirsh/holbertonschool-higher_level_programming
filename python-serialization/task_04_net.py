#!/usr/bin/python3
''' module documentation '''
import socket
import json

def start_server():
    '''
    function that sets up a server using the socket library
    '''
    HOST = "127.0.0.1"
    PORT = 11235

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            if data:
                print("Received Dictionary from Client:")
                print(json.loads(data))

def send_data(data):
    '''
    function that acts as the client
    '''
    HOST = "localhost"
    PORT = 11235

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(data).encode("utf-8"))
