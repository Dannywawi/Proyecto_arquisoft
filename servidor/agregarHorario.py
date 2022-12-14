import socket, sys, json
import os
from bdd import connectDb
import hashlib
import pickle


collectionSucursales=connectDb()["sucursales"]
collectionHorarios=connectDb()["horarios"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 5003)
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
            filtro1={"nombre":data["sucursal"]}
            mesas = collectionSucursales.find_one(filtro1,{"mesas":1,"_id":0})
            cantidadMesas = int(mesas["mesas"])

            mesasHorario = {"12-13":cantidadMesas,"13-14":cantidadMesas,"14-15":cantidadMesas,"15-16":cantidadMesas,"16-17":cantidadMesas}
            post = {"sucursal":data["sucursal"],"fecha":data["fecha"],"horarios":mesasHorario}
            collectionHorarios.insert_one(post)          
            print('Horarios agregados para el dia y la sucursal indicada',post)

            if post != None:
                print('sending data back to the client')
                msg = "se agrego correctamente"
                connection.sendall(pickle.dumps(msg))
                break
            else:
                print('no data from', client_address)
                msg = "Ocurrio un problema"
                connection.sendall(pickle.dumps(msg))
                break

    finally:
        # Clean up the connection
        connection.close()