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
        print("restaurant:",par["id_sucursal"])
        print("fecha:",par["fecha"])
        print("hora:",par["horario"])
        print("numero de personas:",par["n_personas"])
        print("estado:",par["estado"])
        print("***************************")
        print(" ")


    x=input("Presionar boton para salir")



