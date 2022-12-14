import socket, sys, json
import os
from bdd import connectDb
import pickle
import hashlib
import bson

collection1=connectDb()["sucursal"]
collection2=connectDb()["reserva"]
collection3=connectDb()["historial"]
collection4=connectDb()["usuario"]

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

                for data in collection1.find({},{"_id":0}):
                    datos.append(data)
                print(data)
                clientsocket.sendall(pickle.dumps(datos))
                break

            elif option == 2:
                print('Esperando datos...')
                reserv=clientsocket.recv(4096).decode("utf-8")
                reserv = json.loads(reserv)
                print('received {!r}',reserv)

                #Almacenando reserva

                resto = int(reserv["personas"])%6

                if resto == 0:
                    mesas = int(int(reserv["personas"])/6)
                
                else:
                    mesas = int(int(reserv["personas"])/6 + 1)


                for data in collection1.find({},{}):
                    if data['restaurant'] == reserv["restaurant"]:
                        id_rest = data['_id']
                
                id_reserva = bson.ObjectId()
                    
                post1={"_id":id_reserva,"id_sucursal": id_rest,"n_personas":reserv["personas"],"n_mesas":mesas,"fecha":reserv["fecha"],"horario":reserv["horario"],"estado":"reservada"}
                collection2.insert_one(post1)            
                print('reserva creada: ',post1)

                #Almacenando historial

                for data in collection4.find({},{}):
                    if data['correo'] == reserv["correo"]:
                        id_usuario = data['_id']   
                
                post2={"id_usuario":id_usuario,"id_reserva": id_reserva}
                collection3.insert_one(post2)            
                print('historial nuevo creado: ',post2)

                response = '1'

                if post1 != None:
                    print('sending data back to the client')
                    clientsocket.sendall(response.encode())
                    break
                else:
                    print('no data from', address)
                    break
                



            else:
                print('Opcion invalida, por favor elija numero entre 1 y 3.')
                