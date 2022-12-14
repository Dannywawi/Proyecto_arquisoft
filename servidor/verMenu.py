import socket, sys, json, pickle
import os
from bdd import connectDb
import hashlib
from bson.json_util import dumps
from ctypes import resize

collectionMenu=connectDb()["menu"]

class menu():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 25009)
        self.sock.bind(self.server_address)
        self.sock.listen(1)
        
        while True:
            print('waiting for a connection')
            connection, client_address = self.sock.accept()

            try:
                print('connection from', client_address)

                data = connection.recv(4096).decode()
                commands = data.split("|||",1)
                print('received',commands)

                messs = self.buscar_menu(commands[0],commands[1])
                connection.sendall(pickle.dumps(messs))
            
                       
            finally:
                connection.close()

    def buscar_menu(self,sucursal,fecha):
        datos = collectionMenu.find_one({"sucursal":str(sucursal),"fecha":str(fecha)},{"menu":1})
        print("datos",datos)
        if datos == None:
            datos = {"menu":"No existe un menu asignado a la sucursal ingresada en la fecha ingresada."}
        return datos

menu()
