import socket, sys, json
import os
from bdd import connectDb
import hashlib
import pickle
from bson.json_util import dumps


collectionComentarios=connectDb()["comentarios"]
#collectionHorarios=connectDb()["horarios"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 5009)
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
            
            comentarios = collectionComentarios.find({},{"_id":0})
            json_data = dumps(list(comentarios))

            if comentarios != None:
                print('sending data back to the client')
                connection.sendall(pickle.dumps(json_data))
                break
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()