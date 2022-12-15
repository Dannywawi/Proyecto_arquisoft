from ctypes import resize
import socket, sys, json, pickle
import os
from bdd import connectDb

collection=connectDb()["comentarios"]

class comentariooo():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 25000)
        self.sock.bind(self.server_address)

        # Listen for incoming connections
        self.sock.listen(1)
        
        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = self.sock.accept()

            try:
                print('connection from', client_address)
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(4096).decode()
                    commands = data.split('|||',2)
                    print('received',commands)

                    if(self.insertar_comentario(commands[0],commands[1],commands[2])):
                        connection.sendall("Se ha publicado el comentario de forma existosa".encode())
                    else:
                        connection.sendall("Hubo un error al publicar el comentario".encode())
                    break
            finally:
                connection.close()

    def insertar_comentario(self, fecha, correo, mensaje):
        try:
            comentario = {"correo":correo, "fecha":fecha, "comentario":mensaje}
            collection.insert_one(comentario)
            return True
        except:
            return False

comentariooo()
