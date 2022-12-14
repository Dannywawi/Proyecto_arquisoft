import socket, sys, json
import os
from bdd import connectDb
import hashlib
import pickle


#collectionSucursales=connectDb()["sucursales"]
collectionHorarios=connectDb()["horarios"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 5004)
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

            filtro = {"sucursal":data["sucursal"],"fecha":data["fecha"]}
            try:
                horarios = collectionHorarios.find_one(filtro,{"horarios":1,"_id":0})
                result = horarios["horarios"][data["horario"]]
                #collection.updateOne({sucursal: "alameda", fecha: "12/07/22"}, {$set:{horarios:{12-13:9}}})

                if int(result) - int(data["mesas"]) >= 0 and horarios!=None: 
                    horarios["horarios"][data["horario"]] = int(horarios["horarios"][data["horario"]]) - int(data["mesas"])
                    collectionHorarios.update_one(filtro, {"$set":{"horarios":horarios["horarios"]}})
                    msg = "asignacion exitosa"
                    connection.sendall(pickle.dumps(msg))
                    break
                else:
                    msg = "no quedan mesas disponibles"
                    connection.sendall(pickle.dumps(msg))
                    break
            except:
                msg = "An exception occurred"
                connection.sendall(pickle.dumps(msg))
    finally:
        # Clean up the connection
        connection.close()