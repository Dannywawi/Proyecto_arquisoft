import socket, pickle
import sys
import os
from datetime import date

def WriteCom(type_user, mail):
    
    # Accion que desea realizar el usuario en el foro
    while(True):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    

        alo = ''
        print("Que desea hacer?")
        print("1. Publicar comentario\n2. Volver al menu principal")
        
        try:
            selec = int(input("Seleccione: "))
            if(selec == 1):
                pal = input("Ingrese comentario (maximo 200 caracteres): \n")
                while (len(pal) < 1) or (len(pal) > 200):
                    pal = input("Ingrese comentario (maximo 200 caracteres): \n")
                fecha = str(date.today())
                alo = fecha+"|||"+mail+"|||"+pal
            elif(selec == 2):
                return
            else:
                print("Opcion no disponible.")
                continue
            
            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 25000)
            print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)

            if (alo != ''):
                try:
                    os.system('clear')
                    message = alo.encode()
                    #print('sending {!r}'.format(message))
                    sock.sendall(message)

                    data = sock.recv(4096)
                    print(data.decode())
                        
                finally:
                        sock.close()

        except:
            print("Opcion invalida.")
