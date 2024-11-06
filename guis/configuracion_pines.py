import pyfirmata
import time
import inspect

# Verificar compatibilidad con versiones antiguas de inspect
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

# Configuración de la placa (ajusta el puerto según tu configuración)
board = pyfirmata.Arduino('COM6')  # Cambia el puerto según corresponda
it = pyfirmata.util.Iterator(board)
it.start()

# Declaración de pines con la sintaxis de get_pin
button_pins = {
    'yellow': board.get_pin('d:5:i'),  
    'green': board.get_pin('d:2:i'),   
    'red': board.get_pin('d:3:i'),    
    'blue': board.get_pin('d:4:i')     
}
led_pins = {
    'yellow': board.get_pin('d:9:o'),
    'red': board.get_pin('d:7:o'),
    'green': board.get_pin('d:6:o'),
    'blue': board.get_pin('d:8:o')
}

# Frecuencias para cada color
frequencies = {
    'yellow': 440,       
    'red': 523,
    'green': 659,
    'blue': 784
}

# Configuración del pin del zumbador como PWM
buzzer_pin = board.get_pin('d:11:p')  # PWM en el pin 14

# Variable de estado de los botones
button_states = {
    'yellow': False,
    'green': False,
    'red': False,
    'blue': False
}

# Función para leer el estado de cada botón
def read_buttons():
    """Actualiza el estado de cada botón."""
    for color, pin in button_pins.items():
        button_state = pin.read()
        if button_state is not None:
            button_states[color] = button_state  # Actualiza el estado del botón

# Función para encender o apagar un LED
def toggle_led(led, state):
    """Controla el LED encendiéndolo o apagándolo."""
    led.write(1 if state else 0)  # Escribe 1 para encender o 0 para apagar

# Función para apagar todos los LEDs
def turn_off_all_leds():
    """Apaga todos los LEDs."""
    for led in led_pins.values():
        led.write(0)  # Apaga el LED

# Función para reproducir un tono en el buzzer usando PWM
def play_buzzer(frequency, duration):
    buzzer_pin.write(frequency / 1000)  # Ajusta el PWM a la frecuencia deseada
    time.sleep(duration)
    buzzer_pin.write(0)  # Apaga el buzzer

# Función para mostrar una secuencia de luces y sonidos
def show_sequence(sequence, delay):
    for color in sequence:
        toggle_led(led_pins[color], True)  # Enciende el LED
        play_buzzer(frequencies[color], delay)  # Activa el zumbador
        toggle_led(led_pins[color], False)  # Apaga el LED
        time.sleep(0.2)


