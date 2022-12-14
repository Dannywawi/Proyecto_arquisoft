import socket
import sys, json
import pickle


def asignarMesa():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('127.0.0.1', 5004)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    #Mesas son para 6 personas max.
    #Bloque1: 9:00 - 14:00
    #Bloque2: 14:00 - 20:00
    print("Ingrese el nombre de la sucursal")
    sucursal=input()
    print("Ingrese fecha")
    fecha=input()
    print("Ingrese horario")
    horario=input()
    print("Ingrese la cantidad de mesas")
    mesas=input()


    post = str({'sucursal': sucursal,'fecha': fecha,'horario': horario, 'mesas':mesas}).replace("'",'"').encode()  
    try: 
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)

        while amount_received < amount_expected:
            data = pickle.loads(sock.recv(4096))
            amount_received += len(data)
            print(data)
            return data 
    finally:
        print('closing socket')
        sock.close()
        