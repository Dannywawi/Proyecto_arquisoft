import socket, sys, json
import os
from bdd import connectDb
import hashlib
import pickle
from bson.json_util import dumps


collectionSucursales = connectDb()["sucursales"]
collectionHorarios = connectDb()["horarios"]
collectionMenu = connectDb()["menu"]
collectionReservas = connectDb()["reservas"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 5008)
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
            #post={"nombre":data["nombre"],"mesas":data["mesas"],"horario":data["horario"]}
            #messs = collection.find_one({"nombre": data["nombre"]})
            #messs = collection.find({},{"nombre":1,"_id":0})
            try:
                post = collectionSucursales.delete_one({"nombre": data["nombre"]})
                myquery = { "sucursal": data["nombre"]}

                
                #try:
                #    x = collectionHorarios.delete_many(myquery)
                #try:
                #    y = collectionMenu.delete_many(myquery)
                #try:
                #    z = collectionReservas.delete_many(myquery)
                

                print(post)

                if post != None:
                    print('sending data back to the client')
                    msg = "se elimino correctamente"
                    connection.sendall(pickle.dumps(msg))
                    break
                else:
                    print('no data from', client_address)
                    msg = "ocurrio un problema"
                    connection.sendall(pickle.dumps(msg))
                    break
            except:
                msg = "ocurrio un problema"
                connection.sendall(pickle.dumps(msg))

    finally:
        # Clean up the connection
        connection.close()