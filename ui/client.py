import socket
import time

# Crear un socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Especificar la dirección IP y el puerto del host
server_address = ('192.168.100.99', 12345)

client_socket.connect(server_address)


# Recibir el mensaje del host
while True:
    # Receive data from the server
    data = client_socket.recv(1024)
    if data:
        print(data.decode())
    time.sleep(1)