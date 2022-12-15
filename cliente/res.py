import socket, pickle
import sys, json
import os

def restaurantes():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((socket.gethostname(),6000))

    while True:
      
        option = 1

        if option == 1:
            sock.send(bytes(str(option),"utf-8"))
            msg = sock.recv(4096)


            for rest in pickle.loads(msg):
                print("restaurant:",rest["nombre"])
  
            restaurant=input('Indique nombre del restaurant: ')
        
        else:
            print("ERROR")

        return restaurant

def ejecucion(restaurant,correo):

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((socket.gethostname(),6000))

    while True:

        option = 2

        if option == 2:
            sock.send(bytes(str(option),"utf-8"))
            
            fecha=input('indique fecha: ')
            horario=input('indique horario: ')
            personas=input('indique numero de personas: ')
            
            post = str({'restaurant': restaurant,'fecha': fecha, 'horario':horario, 'personas':personas, 'correo':correo}).replace("'",'"').encode()

            try: 
                sock.sendall(post)
                amount_received = 0
                amount_expected = len(post)

                while amount_received < amount_expected:
                    res = sock.recv(4096)
                    amount_received += len(res)
                    print('received {!r}'.format(res))
                    return
   
            finally:
                print('closing socket')
                sock.close()


        else:
            print("ERROR")
        

def reservar(c):
    
    r = restaurantes()
    ejecucion(r,c)
    print("Reserva realizada")




