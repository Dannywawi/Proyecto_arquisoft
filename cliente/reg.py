import socket
import sys, json


def Register():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5002)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    
    nombre=""
    celular=0
    correo=""
    password=""
    
    print("Ingrese su nombre (maximo 20 caracteres)")
    nombre=input()
    while (len(nombre) < 1) or (len(nombre) > 20):
        print("Ingrese su nombre")
        nombre=input()
    
    while True:
        print("Ingrese su celular (maximo 15 números)")
        try:
            celular=int(input())
            while (celular < 1) or (celular > 999999999999999):
                print("Ingrese su celular (maximo 15 números)")
                try:
                    celular=int(input())
                    break
                except ValueError:
                    print("Error en el valor ingresado")
                    continue
            break
        except ValueError:
            print("Error en el valor ingresado")
            continue
    
    print("Ingrese su correo electronico (maximo 25 caracteres)")
    correo=input()
    while (len(correo) < 1) or (len(correo) > 25):
        print("Ingrese su correo electronico (maximo 25 caracteres)")
        correo=input()
    
    print("Ingrese su contraseña (maximo 20 caracteres)")
    password=input()
    while (len(password) < 1) or (len(password) > 20):
        print("Ingrese su contraseña (maximo 20 caracteres)")
        password=input()
    
    post = str({'nombre': nombre, 'celular':celular, 'clave': password, 'correo':correo}).replace("'",'"').encode()  
    try: 
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)

        while amount_received < amount_expected:
            data = sock.recv(4096)
            amount_received += len(data)
            print('received {!r}'.format(data))
            return data.decode("utf-8") 
    finally:
        print('closing socket')
        sock.close()
        
