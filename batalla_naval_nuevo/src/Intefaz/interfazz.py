from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import sys
sys.path.append("src")

from Batalla.Juego_principal import TableroBatallaNaval

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        
        # Initialize the game boards for both players
        self.player1_board = TableroBatallaNaval(10, 10)
        self.player1_board.colocar_naves()
        self.player2_board = TableroBatallaNaval(10, 10)
        self.player2_board.colocar_naves()

        # Create labels to display whose turn it is
        self.turn_label = Label(text="Player 1's Turn")
        self.add_widget(self.turn_label)

        # Create buttons for player 1's board
        Contenedor1 = BoxLayout(orientation='vertical')
        for numero_fila in range(10):
            fila = BoxLayout(orientation="horizontal")
            Contenedor1.add_widget(fila)
            for numero_columna in range(10):
                casilla = Button(text='O', font_size=60)
                casilla.fila = numero_fila
                casilla.columna = numero_columna
                casilla.bind(on_press=self.player1_fire)
                fila.add_widget(casilla)
            

        return Contenedor1
        
    
    def player1_fire(self, instance):
        # Fire shot on player 2's board
        result = self.player2_board.disparar(instance.fila, instance.columna, self.player2_board.tablero)

        # Update button text to reflect the shot result
        if result == 'X':
            instance.text = 'X'
        elif result == 'N':
            instance.text = ' '

        # Check for sunk ships
        self.player2_board.barco_hundido()

        # Update turn label
        self.turn_label.text = "Player 2's Turn"

        self.manager.current =  'Turno_Jugador2'


class CambioDePantalla(Screen):
    def __init__(self, **kwargs):
        super(CambioDePantalla, self).__init__(**kwargs)

        # Create labels to display whose turn it is
        self.turn_label = Label(text="Player 2's Turn")
        self.add_widget(self.turn_label)
        Contenedor2 = BoxLayout(orientation='vertical')
        # Create buttons for player 2's board
        for numero_fila in range(10):
            fila = BoxLayout(orientation="horizontal")
            Contenedor2.add_widget(fila)
            for numero_columna in range(10):
                casilla = Button(text='O', font_size=60)
                casilla.fila = numero_fila
                casilla.columna = numero_columna
                casilla.bind(on_press=self.player2_fire)
                fila.add_widget(casilla)
            
        return Contenedor2

    def player2_fire(self, instance):
        # Fire shot on player 1's board
        result = self.player1_board.disparar(instance.fila, instance.columna, self.player1_board.tablero)

        # Update button text to reflect the shot result
        if result == 'X':
            instance.text = 'X'
        elif result == 'N':
            instance.text = ' '

        # Check for sunk ships
        self.player1_board.barco_hundido()

        # Update turn label
        self.turn_label.text = "Player 1's Turn"

        # Change to player 1's turn screen
        self.manager.current = 'TurnoJugador1'

class BattleshipApp(App):
    def build(self):
        sm = ScreenManager()
        Pantalla_Jugador1= GameScreen(name='Turno_Jugador1')
        Pantalla_Jugador2= CambioDePantalla(name='Turno_Jugador2')

        sm.add_widget(GameScreen(name='Turno_Jugador1'))

        Turno_Jugador2=Pantalla_Jugador2.__init__()
        Pantalla_Jugador2.add_widget(Turno_Jugador2)
        sm.add_widget(CambioDePantalla(name='Pantalla_Jugador2'))
        return sm

if __name__ == '__main__':
    BattleshipApp().run()