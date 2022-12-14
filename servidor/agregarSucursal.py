import socket, sys, json
import os
from bdd import connectDb
import hashlib
import pickle


collection=connectDb()["sucursales"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 5007)
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
            post={"nombre":data["nombre"],"mesas":data["mesas"],"horario":data["horario"]}
            collection.insert_one(post)
            messs = '2'
            if post != None:
                print('sending data back to the client')
                msg = "se agrego correctamente"
                connection.sendall(pickle.dumps(msg))
                break
            else:
                print('no data from', client_address)
                msg = "ocurrio un problema"
                connection.sendall(pickle.dumps(msg))
                break

    finally:
        # Clean up the connection
        connection.close()