import socket, sys, json
import os
from bdd import connectDb
import hashlib
import pickle


collectionMenu=connectDb()["menu"]
#collectionHorarios=connectDb()["horarios"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 5006)
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
            
            post = {"sucursal":data["sucursal"],"fecha":data["fecha"],"menu":data["menu"]}
            collectionMenu.insert_one(post)     

            if post != None: 
                #horarios["horarios"][data["horario"]] = int(horarios["horarios"][data["horario"]]) - int(data["mesas"])
                #collectionHorarios.update_one(filtro, {"$set":{"horarios":horarios["horarios"]}})
                msg = {"msg":"ok"}
                connection.sendall(pickle.dumps(msg))
                break
            else:
                msg = {"error":"error"}
                connection.sendall(pickle.dumps(msg))
                break

    finally:
        # Clean up the connection
        connection.close()