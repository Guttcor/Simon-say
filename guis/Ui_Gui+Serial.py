from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from Ui_ventana_principal import Ui_MainWindow
from Ui_xjugadores import Ui_xjugadores
from Ui_xtremo import Ui_xtremo
from Ui_nomunjugador import Ui_Formulario1ju
from Ui_ventana1jugador import Ui_Unjugador
from configuracion_pines import *
import random
import threading
import time

class Principal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.xjugadores_window = XJugadoresWindow(self)
        self.nomjugador_window = NomJugadorWindow(self)
        
        # Conectar botones a sus métodos respectivos
        self.Xtream.clicked.connect(self.open_xjugadores)
        self.Un_jugador.clicked.connect(self.open_nomjugador)

    def open_xjugadores(self):
        self.xjugadores_window.show()

    def open_nomjugador(self):
        self.nomjugador_window.show()

class XJugadoresWindow(QtWidgets.QWidget, Ui_xjugadores):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.players_labels = [self.Player1, self.Player2, self.Player3, self.Player4, self.Player5, self.Player6]
        self.players_texts = [self.nomPlayer1, self.nomPlayer2, self.nomPlayer3, self.nomPlayer4, self.nomPlayer5, self.nomPlayer6]

        # Ocultar todos los elementos de los jugadores al inicio
        self.hide_all_player_elements()

        self.check.clicked.connect(self.update_player_visibility)
        self.conf.clicked.connect(self.open_xtremo)

    def hide_all_player_elements(self):
        # Función para ocultar todos los elementos relacionados con jugadores
        for label, text in zip(self.players_labels, self.players_texts):
            label.hide()
            text.hide()

    def update_player_visibility(self):
        # Ocultar todos los elementos al inicio
        self.hide_all_player_elements()

        # Muestra solo los elementos necesarios según el número de jugadores seleccionado
        num_players = self.select.value()
        for i in range(num_players):
            self.players_labels[i].show()
            self.players_texts[i].show()

    def open_xtremo(self):
        # Recoger nombres de jugadores desde los campos de texto
        player_names = [text.toPlainText() for text in self.players_texts]
        # Abrir la ventana Xtremo y pasar los nombres de los jugadores
        print("Abriendo XtremoWindow con los siguientes nombres de jugadores:", player_names)  # Confirmación en consola
        self.xtremo_window = XtremoWindow(self.main_window, num_players=self.select.value(), player_names=player_names)
        self.xtremo_window.show()
        self.hide()

    def return_to_main(self):
        # Regresar a la ventana principal
        self.hide()
        self.main_window.show()

class NomJugadorWindow(QtWidgets.QWidget, Ui_Formulario1ju):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.boton1p.clicked.connect(self.open_ventana1jugador)

    def open_ventana1jugador(self):
        # Abrir ventana1jugador con el nombre del jugador
        self.ventana1jugador_window = Ventana1JugadorWindow(self, self.nombre1p.toPlainText())
        self.ventana1jugador_window.show()
        self.hide()

class Ventana1JugadorWindow(QtWidgets.QWidget, Ui_Unjugador):
    def __init__(self, main_window, player_name):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.nom1p.setText(player_name)  # Mostrar nombre del jugador

        # Crear una instancia de Jugador para el jugador actual y mostrar el puntaje en la interfaz
        self.jugador = self.Jugador(player_name)
        self.score1p.setText(str(self.jugador.puntaje))

        # Variables de control del juego
        self.paused = False
        self.running = False

        # Conectar los botones de inicio y pausa
        self.star1p.clicked.connect(self.iniciar_juego)
        self.pause1p.clicked.connect(self.toggle_pause)
        self.return1p_2.clicked.connect(self.close)

    class Jugador:
        def __init__(self, usuario, puntaje=0):
            self.usuario = usuario
            self.puntaje = puntaje

        def incrementar_puntaje(self, puntos):
            self.puntaje += puntos

        def __str__(self):
            return f"Jugador: {self.usuario}, Puntaje: {self.puntaje}"

    def iniciar_juego(self):
        """Inicia el juego en un hilo separado para no bloquear la GUI."""
        if not self.running:  # Iniciar el juego solo si no está ya en ejecución
            self.running = True
            self.juego_thread = threading.Thread(target=self.juego_principal)
            self.juego_thread.start()

    def toggle_pause(self):
        """Activa o desactiva el estado de pausa."""
        if self.running:
            self.paused = not self.paused  # Cambia el estado de pausa
            if self.paused:
                print("Juego en pausa")
                self.pause1p.setText("Resume")  # Cambia el texto a "Resume" cuando está en pausa
            else:
                print("Juego reanudado")
                self.pause1p.setText("Pause")  # Cambia el texto a "Pause" cuando está activo

    def juego_principal(self):
        pasos = 4
        delay = 1.0
        nivel = 1
        puntos_por_nivel = 1000
        self.jugador.puntaje = 0

        while nivel <= 10:
            # Pausa el juego si el estado de pausa está activado
            while self.paused:
                time.sleep(0.1)  # Espera hasta que se quite la pausa

            time.sleep(2)
            self.secuencia(pasos, delay)
            print('TE TOCA')
            self.turn_off_all_leds()
            self.juego(pasos)
            print(self.button_sequence)
            print(self.sequence)

            # Verifica si el juego está pausado después de cada intento
            if self.paused:
                continue

            if self.button_sequence == self.sequence:
                print("¡Correcto!")
                self.jugador.incrementar_puntaje(puntos_por_nivel)
                self.actualizar_puntaje()
                nivel += 1
                pasos += 1
                delay = max(0.2, delay - 0.05)
                self.turn_off_all_leds()
            else:
                print("Secuencia incorrecta. Has perdido.")
                self.turn_off_all_leds()
                print(self.jugador)
                break

        if nivel > 10:
            print('¡FELICIDADES, GANASTE!')

        # Indica que el juego ha terminado
        self.running = False

    def secuencia(self, pasos, delay):
        """Genera y muestra una secuencia de colores."""
        self.sequence = [random.choice(['yellow', 'red', 'green', 'blue']) for _ in range(pasos)]
        self.show_sequence(self.sequence, delay)
        time.sleep(1)
        self.turn_off_all_leds()

    def juego(self, pasos):
        """Lee la secuencia del jugador."""
        self.button_sequence = []
        print("Reproduce la secuencia...")

        while len(self.button_sequence) < pasos:
            # Pausa el juego si el estado de pausa está activado
            if self.paused:
                time.sleep(0.1)
                continue

            for button_name, pin in button_pins.items():
                if self.read_button(pin):
                    self.button_sequence.append(button_name)
                    print(f"{button_name} presionado")
                    self.toggle_led(led_pins[button_name], True)
                    time.sleep(0.5)
                    self.toggle_led(led_pins[button_name], False)
                    self.turn_off_all_leds()
                    time.sleep(0.3)

    def actualizar_puntaje(self):
        """Actualiza el puntaje mostrado en la GUI."""
        self.score1p.setText(str(self.jugador.puntaje))

    # Métodos auxiliares
    def read_button(self, pin):
        """Lee el estado de un botón en un pin específico."""
        return pin.read() == 1

    def toggle_led(self, pin, state):
        """Activa o desactiva un LED."""
        pin.write(1 if state else 0)

    def turn_off_all_leds(self):
        """Apaga todos los LEDs."""
        for pin in led_pins.values():
            pin.write(0)

    def show_sequence(self, sequence, delay):
        """Muestra la secuencia de LEDs para la memoria del jugador."""
        for color in sequence:
            self.toggle_led(led_pins[color], True)
            time.sleep(delay)
            self.toggle_led(led_pins[color], False)
            time.sleep(0.2)

class XtremoWindow(QtWidgets.QWidget, Ui_xtremo):
    def __init__(self, main_window, num_players=1, player_names=None):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        player_names = player_names if player_names else [""] * num_players

        # Configurar los labels `scp#` con '000000' para los jugadores seleccionados
        print("Configurando labels en XtremoWindow...")  # Confirmación en consola
        for i in range(1, 7):
            scp_label = getattr(self, f'scp{i}', None)
            if scp_label:
                if i <= num_players:
                    scp_label.setText("000000")
                    scp_label.show()
                    print(f"scp{i} configurado como '000000' y visible")  # Confirmación en consola
                else:
                    scp_label.setText("")  # Dejar vacío si no se usa
                    scp_label.hide()
                    print(f"scp{i} ocultado")  # Confirmación en consola
            else:
                print(f"scp{i} no encontrado en la interfaz.")  # Mensaje si el label no existe

        try:
            self.returnx.clicked.connect(self.return_to_main)
        except AttributeError:
            print("El botón returnx no existe en la interfaz.")  # Confirmación en consola

    def return_to_main(self):
        # Cerrar esta ventana y regresar a la ventana principal
        self.hide()
        self.main_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Principal()
    main_window.show()
    sys.exit(app.exec())

