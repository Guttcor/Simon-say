
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from Ui_ventana_principal import Ui_MainWindow
from Ui_xjugadores import Ui_xjugadores
from Ui_xtremo import Ui_xtremo
from Ui_nomunjugador import Ui_Formulario1ju
from Ui_ventana1jugador import Ui_Unjugador


class Principal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.xjugadores_window = XJugadoresWindow(self)
        self.nomjugador_window = NomJugadorWindow(self)
        
        # Connect buttons to respective methods
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
        
        # Try to set name and score labels if they exist
        self.name_labels = []
        self.score_labels = []
        for i in range(1, 7):
            try:
                self.name_labels.append(getattr(self, f'nomp{i}'))  # Try to get labels named `nomp#`
                self.score_labels.append(getattr(self, f'stp{i}'))  # Try to get labels named `stp#`
            except AttributeError:
                # If not found, add a placeholder (None), which will be ignored when setting text
                self.name_labels.append(None)
                self.score_labels.append(None)

        # Initial visibility for player fields
        for label, text, name_label, score_label in zip(self.players_labels, self.players_texts, self.name_labels, self.score_labels):
            label.hide()
            text.hide()
            if name_label:
                name_label.hide()
            if score_label:
                score_label.hide()

        self.check.clicked.connect(self.update_player_visibility)
        self.conf.clicked.connect(self.open_xtremo)

        # Connect return button if it exists
        try:
            self.returnx.clicked.connect(self.return_to_main)
        except AttributeError:
            pass  # Skip if returnx button is not available

    def update_player_visibility(self):
        num_players = self.select.value()
        # Hide all labels and text edits
        for label, text, name_label, score_label in zip(self.players_labels, self.players_texts, self.name_labels, self.score_labels):
            label.hide()
            text.hide()
            if name_label:
                name_label.hide()
            if score_label:
                score_label.hide()
        # Show the necessary labels and text edits based on selected number of players
        for i in range(num_players):
            self.players_labels[i].show()
            self.players_texts[i].show()
            if self.name_labels[i]:
                self.name_labels[i].show()
            if self.score_labels[i]:
                self.score_labels[i].show()

    def open_xtremo(self):
        # Gather player names from text edits
        player_names = [text.toPlainText() for text in self.players_texts]
        # Open xtremo window and pass player names to display
        self.xtremo_window = XtremoWindow(self.main_window, num_players=self.select.value(), player_names=player_names)
        self.xtremo_window.show()
        self.hide()

    def return_to_main(self):
        # Return to the main window
        self.hide()
        self.main_window.show()

class NomJugadorWindow(QtWidgets.QWidget, Ui_Formulario1ju):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.boton1p.clicked.connect(self.open_ventana1jugador)

    def open_ventana1jugador(self):
        # Open ventana1jugador window with player name
        self.ventana1jugador_window = Ventana1JugadorWindow(self, self.nombre1p.toPlainText())
        self.ventana1jugador_window.show()
        self.hide()

class Ventana1JugadorWindow(QtWidgets.QWidget, Ui_Unjugador):
    def __init__(self, main_window, player_name):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.nom1p.setText(player_name)  # Display player name
        # Add functionality to buttons if required
        self.return1p_2.clicked.connect(self.close)  # Close the window

class XtremoWindow(QtWidgets.QWidget, Ui_xtremo):
    def __init__(self, main_window, num_players=1, player_names=None):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        player_names = player_names if player_names else [""] * num_players
        # Set player names in labels
        for i in range(num_players):
            try:
                getattr(self, f'nomp{i+1}').setText(player_names[i])  # Set player name in `nomp#` labels
            except AttributeError:
                pass  # Ignore if label is missing
        # Show the number of players selected
        for i in range(1, num_players + 1):
            try:
                getattr(self, f'stp{i}').show()  # Show score labels up to num_players
            except AttributeError:
                pass  # Ignore if label is missing
        for i in range(num_players + 1, 7):
            try:
                getattr(self, f'stp{i}').hide()  # Hide remaining score labels
            except AttributeError:
                pass  # Ignore if label is missing
        try:
            self.returnx.clicked.connect(self.return_to_main)
        except AttributeError:
            pass  # Skip if returnx button is not available

    def return_to_main(self):
        # Close this window and return to the main window
        self.hide()
        self.main_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Principal()
    main_window.show()
    sys.exit(app.exec())
