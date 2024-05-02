import machine
import time

# Definir los pines GPIO de la Raspberry Pi Pico
clk_pin = machine.Pin(19, machine.Pin.OUT)
data_pin = machine.Pin(18, machine.Pin.OUT)
button_pin = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)  # Configurar el pin del botón como entrada

# Función para enviar datos al SN74LS164N
def shift_out(data_pin, clk_pin, data):
    for i in range(8):
        # Establecer el valor de datos
        data_pin.value((data >> (7 - i)) & 1)
        # Pulsar el pin de reloj (clk) para enviar el dato
        clk_pin.value(1)
        clk_pin.value(0)

# Bucle principal
button_state = 0  # Estado inicial del botón
debounce_time = 0.05  # Tiempo de debounce en segundos
last_toggle_time = 0  # Último tiempo en que se cambió el estado del botón

while True:
    # Leer el estado del botón
    current_time = time.time()
    if current_time - last_toggle_time > debounce_time:
        new_button_state = button_pin.value()

        # Si el estado del botón cambia, actualizar el tiempo del último cambio
        if new_button_state != button_state:
            button_state = new_button_state
            last_toggle_time = current_time

    # Si se presiona el botón (estado alto), encender la LED
    if button_state == 1:
        shift_out(data_pin, clk_pin, 0b00000001)  # Enviar datos al SN74LS164N para encender la LED
        #print("LED encendida")
    else:
        shift_out(data_pin, clk_pin, 0b00000000)  # Enviar datos al SN74LS164N para apagar la LED
        #print("LED apagada")

    time.sleep(0.01)  # Pequeña pausa para liberar el procesador
