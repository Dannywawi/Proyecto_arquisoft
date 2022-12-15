import socket, sys, json
import os
from bdd import connectDb
import pickle
import hashlib
import bson
import numpy as np

collection1=connectDb()["reservas"]
collection2=connectDb()["historial"]
collection3=connectDb()["usuario"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
sock.bind((socket.gethostname(),6001))

sock.listen(5)


while True:
    while True:
        print('waiting for a connection')

        while True:
            reservas=[]
            datos=[]
            clientsocket, address = sock.accept()
            print(f"La conexion con {address} fue establecida")

            reserv=clientsocket.recv(4096).decode("utf-8")
            reserv = json.loads(reserv)
            print('received {!r}',reserv)

            #obtener id usuario
            for data in collection3.find({},{}):
                if data['correo'] == reserv["correo"]:
                    id_usuario = data['_id']

            #obtener reservas realizada por el usuario
            for data in collection2.find({},{}):
                if data['id_usuario'] == id_usuario:
                    reservas.append(data['id_reserva'])
            
            orden = 0

            #Mostrar historial de reservas
            for data in collection1.find({},{}):
                for res in reservas:
                    if res == data['_id']:
                        datos.append(data)
            
            clientsocket.sendall(pickle.dumps(datos))
            

                    

            

            

            

            
