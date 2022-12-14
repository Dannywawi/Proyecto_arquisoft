import socket, sys, json
import os
from bdd import connectDb
import hashlib
import pickle 


collection=connectDb()["usuario"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 5002)
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
            safepass = hashlib.sha256(data["clave"].encode('utf-8')).hexdigest()
            post={"tipo_cliente":2,"nombre":data["nombre"],"celular":data["celular"],"clave":safepass,"correo":data["correo"]}
            messs = '2'
            
            # Comprobar si existe correo
            x = collection.find_one({"correo": data["correo"]})
            if x == None:
                collection.insert_one(post)            
                print('Usuario creado: ',post)
            else:
                print('Usuario ya existe.')
                
            if post != None:
                print('sending data back to the client')
                connection.sendall(messs.encode())
                break
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
