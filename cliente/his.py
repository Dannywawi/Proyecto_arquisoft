import socket, pickle
import sys, json
import os

def mostrarhistorial(correo):
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((socket.gethostname(),6001))

    post = str({'correo':correo}).replace("'",'"').encode()

    sock.sendall(post)
    msg = sock.recv(4096)
    print (" ")

    for par in pickle.loads(msg):
        print("restaurant: ",par["sucursal"])
        print("fecha: ",par["fecha"])
        print("horario: ",par["horario"])
        print("Mesas: ", par["cantidadMesas"])

        if par["estado"] == True:
            print("estado: Reservado")
        
        else:
            print("estado: Reserva terminada")
        print("***************************")
        print(" ")


    x=input("Presionar boton para salir")



