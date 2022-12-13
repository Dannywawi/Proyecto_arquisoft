import socket, sys, json
import os
from bdd import connectDb
import pickle

collection=connectDb()["sucursal"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
sock.bind((socket.gethostname(),6000))

# Listen for incoming connections
sock.listen(5)

while True:
    while True:
        print('waiting for a connection')

        while True:
            datos=[]
            clientsocket, address = sock.accept()
            print(f"La conexion con {address} fue establecida")

            option = int(clientsocket.recv(4096).decode("utf-8"))

            if option == 1:

                for data in collection.find({},{"_id":0}):
                    datos.append(data)
                clientsocket.sendall(pickle.dumps(datos))
                break

            else:
                print('Opcion invalida, por favor elija numero entre 1 y 3.')