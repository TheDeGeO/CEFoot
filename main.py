import machine
import time
import socket
import network

pins = [0, 1, 2, 3, 4, 6, 27, 26]

for pin_num in pins:
    pin = machine.Pin(pin_num, machine.Pin.OUT)
    pin.off()

anfitrion = machine.Pin(27, machine.Pin.OUT)
visitante = machine.Pin(26, machine.Pin.OUT)

anfitrion.on()

botonJugador = machine.Pin(5, machine.Pin.IN)

paleta1 = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)
paleta2 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)
paleta3 = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)
paleta4 = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
paleta5 = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
paleta6 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)

ledPaleta1 = machine.Pin(0, machine.Pin.OUT)
ledPaleta2 = machine.Pin(1, machine.Pin.OUT)
ledPaleta3 = machine.Pin(2, machine.Pin.OUT)
ledPaleta4 = machine.Pin(3, machine.Pin.OUT)
ledPaleta5 = machine.Pin(4, machine.Pin.OUT)
ledPaleta6 = machine.Pin(6, machine.Pin.OUT)

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Vega', '123456789')

while wlan.isconnected() == False:
    pass

print('Connected to WiFi network')

# Get the IP address
ip_address = wlan.ifconfig()[0]

print(f"Device IP address: {ip_address}")


#Create socket
server_address = (ip_address, 12345)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

print(f"Host esperando conexiones en {server_address[0]}:{server_address[1]}")



while True:

    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address[0]}:{client_address[1]}")

    if paleta1.value() == 1:
        message = 'a'
    elif paleta2.value() == 1:
        message = 'b'
    elif paleta3.value() == 1:
        message = 'c'
    elif paleta4.value() == 1:
        message = 'd'
    elif paleta5.value() == 1:
        message = 'e'
    elif paleta6.value() == 1:
        message = 'f'
    elif botonJugador.value() == 1:
        message = 'g'
    else:
        message = 'h'

    client_socket.sendall(message.encode())

    client_socket.close()




