import socket, sys, json
import os
from bdd import connectDb
import hashlib


collection=connectDb()["usuario"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5001)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(4096).decode()
            data = json.loads(data)
            print('received {!r}',data)
            x = collection.find_one({"correo" : data["usuario"], "clave" : hashlib.sha256(data["password"].encode('utf-8')).hexdigest()})
            print('ESTES ES X: ',x)
            messs = str(x["tipo_cliente"])
            if x != None:
                print('sending data back to the client')
                connection.sendall(messs.encode())
                break
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()