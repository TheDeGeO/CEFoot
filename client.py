import socket

# Crear un socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Especificar la dirección IP y el puerto del host
server_address = ('192.168.123.100', 12345)

# Conectar al host
client_socket.connect(server_address)

print(f"Conexión establecida con {server_address[0]}:{server_address[1]}")

# Recibir el mensaje del host
data = client_socket.recv(1024)
print(f"Mensaje recibido: {data.decode()}")

# Cerrar la conexión
client_socket.close()