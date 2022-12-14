import socket
import sys, json
import pickle

def agregarSucursal():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('127.0.0.1', 5007)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    #Mesas son para 6 personas max.
    #Bloque1: 9:00 - 14:00
    #Bloque2: 14:00 - 20:00
    print("Ingrese el nombre de la sucursal")
    nombre=input()
    print("Ingrese la cantidad de mesas")
    mesas=input()
    print("Ingrese el horario de la sucursal")
    print("1. Bloque 1: 9:00 - 14:00")
    print("2. Bloque 2: 14:00 - 20:00")
    print("3. Bloque 1 y 2")
    
    while(1):
        horario = input()
        h = int(horario)
        if h == 1 or h == 2 or h == 3:
            break
        else:
            print("opcion invalida, intente nuevamente")

    post = str({'nombre': nombre,'mesas': mesas, 'horario':horario}).replace("'",'"').encode()  
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
        