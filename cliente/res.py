import socket, pickle
import sys, json
import os

orden = 0


def reservar():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((socket.gethostname(),6000))

    while True:
        option = 1
        sock.send(bytes(str(option),"utf-8"))
        msg = sock.recv(4096)

        for rest in pickle.loads(msg):
            print("restaurant:",rest["restaurant"])
  
        restaurant=input('Indique nombre del restaurant: ')

        for rest in pickle.loads(msg):
            if rest["restaurant"] == restaurant:
                print("restaurant:",rest["restaurant"])
                print("fecha:",rest["fecha"])
                print("horario:",rest["Horario"])
                print("numero de mesas:",rest["n_mesas"])

        horario=input('indique horario: ')
        mesas=input('indique numero de mesas: ')

        #AUN EN PROCESO

        break



