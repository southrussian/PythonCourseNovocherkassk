from socket import *
from threading import *

clients = set()


def client_thread(client_socket, client_address):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(client_address[0] + ":" + str(client_address[1] + " says: " + message))

        for client in clients:
            if client is not client_socket:
                client.send((client_address[0] + ":" + str(client_address[1]) + " says: " + message).encode('utf-8'))

        if not message:
            clients.remove(client_socket)
            print(client_address[0] + ":" + str(client_address[1] + 'disconnected'))
            break

    client_socket.close()


host_socket = socket(AF_INET, SOCK_STREAM)
host_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

host = '127.0.0.1'
port = 9090
host_socket.bind((host, port))
host_socket.listen()

print('Server is waiting...')

while True:
    client_socket, client_address = host_socket.accept()
    clients.add(client_socket)
    print("Connected with: ", client_address[0] + ':' + str(client_address[1]))
    thread = Thread(target=client_thread, args=(client_socket, client_address, ))
    thread.start()
