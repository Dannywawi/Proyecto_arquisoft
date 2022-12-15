import socket
import sys, json
import pickle 

def cancelar(correo):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('127.0.0.1', 6002)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    print("Ingrese el nombre de la sucursal")
    nombre=input()
    print("Ingrese fecha de la reserva")
    fecha=input()
    print("Ingrese horario de la reserva")
    horario=input()



    post = str({'nombre': nombre,'fecha':fecha,'horario':horario,'correo':correo}).replace("'",'"').encode()  
    try: 
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)
        #data = pickle.loads(sock.recv(4096))
        #print(data)

        while amount_received < amount_expected:
            data = pickle.loads(sock.recv(4096))
            amount_received += len(data)
            print(data)
            return data
    finally:
        print('closing socket')
        sock.close()