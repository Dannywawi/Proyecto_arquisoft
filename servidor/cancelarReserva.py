import socket, sys, json
import os
from bdd import connectDb
import hashlib
import pickle


collectionReservas=connectDb()["reservas"]
collectionHorarios=connectDb()["horarios"]
collectionSucursales=connectDb()["sucursales"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 6002)
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

            #Eliminar reserva
            filtro = {"usuario":data["correo"],"sucursal":data["nombre"],"fecha":data["fecha"],"horario":data["horario"]}
                   
            reservas = collectionReservas.find_one(filtro,{"cantidadMesas":1,"_id":1})
            print(reservas)

            post = collectionReservas.delete_one({"_id": reservas["_id"]})

            #Liberar mesas
            filtro2 = {"sucursal":data["nombre"],"fecha":data["fecha"]}
            filtro3 = {"nombre":data["nombre"]}
            maxMesas = collectionSucursales.find_one(filtro3,{"mesas":1,"_id":0})
            horarios = collectionHorarios.find_one(filtro2,{"horarios":1,"_id":0})

            print(horarios)
            print( horarios["horarios"])
            print(horarios["horarios"][data["horario"]])

            maxMes = int(maxMesas["mesas"]) 
            result = horarios["horarios"][data["horario"]]

            if int(result) + int(reservas["cantidadMesas"]) <= maxMes and horarios!=None: 
                horarios["horarios"][data["horario"]] = int(horarios["horarios"][data["horario"]]) + int(reservas["cantidadMesas"])
                collectionHorarios.update_one(filtro2, {"$set":{"horarios":horarios["horarios"]}})
                msg = "liberacion exitosa"
                connection.sendall(pickle.dumps(msg))
                break
            else:
                horarios["horarios"][data["horario"]] = maxMes
                collectionHorarios.update_one(filtro, {"$set":{"horarios":horarios["horarios"]}})
                msg = "liberacion exitosa"
                connection.sendall(pickle.dumps(msg))
                break

    finally:
        # Clean up the connection
        connection.close()