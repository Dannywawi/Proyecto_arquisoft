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
                print("restaurant:",rest["restaurant"])
  
            restaurant=input('Indique nombre del restaurant: ')

            for rest in pickle.loads(msg):
                if rest["restaurant"] == restaurant:
                    print("restaurant:",rest["restaurant"])
                    print("fecha:",rest["fecha"])

                    fecha=rest["fecha"]

                    cant = 0
                    while cant < 5:
                        print("horario:",rest["Horario"][cant]," numero de mesas:",rest["n_mesas"][cant])
                        cant = cant + 1

        
        else:
            print("ERROR")

        return restaurant, fecha

def ejecucion(restaurant, fecha, correo):

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((socket.gethostname(),6000))

    while True:

        option = 2

        if option == 2:
            sock.send(bytes(str(option),"utf-8"))

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
    
    r, f= restaurantes()
    print(r,f)
    ejecucion(r,f,c)
    print("Reserva realizada")




