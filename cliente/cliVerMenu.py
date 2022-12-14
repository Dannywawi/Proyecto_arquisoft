import socket
import sys, json
import pickle

def VerMenu():

    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Mesas son para 6 personas max.
        #Bloque1: 9:00 - 14:00
        #Bloque2: 14:00 - 20:00

        mensaje = ''
        print("Que desea hacer?")
        print("1. Ver el menu de una sucursal\n2. Volver al menu principal")

        try:
            selec = int(input("Seleccione: "))
            if(selec == 1):
                sucursal = input("Ingrese el nombre de la sucursal: ")
                fecha = input("Ingrese fecha: ")
                mensaje = sucursal+"|||"+fecha
            elif(selec == 2):
                return
            else:
                print("Opcion no disponible.")
                continue

            server_address = ('127.0.0.1', 25009)
            #print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)

            if (mensaje != ''):
                try: 
                    message = mensaje.encode()
                    #print('sending {!r}'.format(message))
                    sock.sendall(message)

                    data = pickle.loads(sock.recv(4096))
                    print("El menu es: ", data["menu"])

 
                finally:
                    print('closing socket')
                    sock.close()
        except:
            print("Opcion invalida")
 
