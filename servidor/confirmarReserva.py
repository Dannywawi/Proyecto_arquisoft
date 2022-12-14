import socket, sys, json
import os
from bdd import connectDb
import hashlib
import pickle
from bson.json_util import dumps
from bson.objectid import ObjectId


collectionReservas=connectDb()["reservas"]
#collectionHorarios=connectDb()["horarios"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 5011)
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
            
            objInstance = ObjectId(data["id"])
 
            resultado = collectionReservas.update_one({"_id": objInstance},{"$set":{"estado":True}})

            if resultado != None:
                print('sending data back to the client')
                msg = "ok"
                connection.sendall(pickle.dumps(msg))
                break
            else:
                print('no data from', client_address)
                msg = "no se pudo confirmar"
                connection.sendall(pickle.dumps(msg))
                break

    finally:
        # Clean up the connection
        connection.close()