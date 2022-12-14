import socket
import sys, json
import pickle

def verComentarios():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('127.0.0.1', 5009)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    #Mesas son para 6 personas max.
    #Bloque1: 9:00 - 14:00
    #Bloque2: 14:00 - 20:00

    post = str({}).replace("'",'"').encode()  
    try: 
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)

        while amount_received < amount_expected:
            data = pickle.loads(sock.recv(4096))
            amount_received += len(data)
            menu = json.dumps(json.loads(data), indent = 4)
            print(menu)
            return data  
    finally:
        print('closing socket')
        sock.close()
        