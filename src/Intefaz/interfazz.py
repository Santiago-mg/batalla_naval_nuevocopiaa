from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")

from Batalla.Juego_principal import TableroBatallaNaval
class MyPopup_jugador1(Popup):
    def __init__(self, **kwargs):
        super(MyPopup_jugador1, self).__init__(**kwargs)
        self.title = 'Alerta'
        self.size_hint = (None, None)
        self.size = (300, 200)
        
        content_layout = BoxLayout(orientation='vertical')
        
        message_label = Label(text='El jugador 1 ha ganado')
        content_layout.add_widget(message_label)
        self.content = content_layout
class MyPopup_jugador2(Popup):
    def __init__(self, **kwargs):
        super(MyPopup_jugador2, self).__init__(**kwargs)
        self.title = 'Alerta'
        self.size_hint = (None, None)
        self.size = (300, 200)
        
        content_layout = BoxLayout(orientation='vertical')
        
        message_label = Label(text='El jugador 2 ha ganado')
        content_layout.add_widget(message_label)
        self.content = content_layout
class MyPopup_impacto(Popup):
    def __init__(self, **kwargs):
        super(MyPopup_impacto, self).__init__(**kwargs)
        self.title = 'Alerta'
        self.size_hint = (None, None)
        self.size = (300, 200)
        
        content_layout = BoxLayout(orientation='vertical')
        
        message_label = Label(text='Barco destruido')
        content_layout.add_widget(message_label)
        self.content = content_layout         

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        
        # Initialize the game boards for both players
        self.player1_board = TableroBatallaNaval(10, 10)
        self.player1_board.colocar_naves()
        self.player2_board = TableroBatallaNaval(10, 10)
        self.player2_board.colocar_naves()


        ContenedorA= BoxLayout(orientation= "vertical")
        # Create labels to display whose turn it is
        self.Jugador_En_Turno = Label(text="El turno de disparar es para el Jugador 1", font_size="30sp", size_hint_y=0.2)
        ContenedorA.add_widget(self.Jugador_En_Turno)

        Contenedor1 = BoxLayout(orientation='vertical')

        # Create buttons for player 1's board
        for numero_fila in range(10):
            fila = BoxLayout(orientation="horizontal")
            for numero_columna in range(10):
                casilla = Button(text='O', font_size=20,
                                 disabled=False
                                 )
                casilla.fila = numero_fila
                casilla.columna = numero_columna
                casilla.bind(on_press=self.player1_fire)
                if self.player2_board.buscar_barco():
                    casilla.bind(on_press=self.show_popup)
                fila.add_widget(casilla)
            Contenedor1.add_widget(fila)

        ContenedorA.add_widget(Contenedor1)
        self.add_widget(ContenedorA)
    def show_popup2(self):
        popup = MyPopup_impacto()
        popup.open()
    
    def player1_fire(self, instance):
        # Fire shot on player 2's board
        result = self.player2_board.disparar(instance.fila, instance.columna, self.player2_board.tablero)

        # Update button text to reflect the shot result
        if result == 'X':
            instance.text = 'X'
            instance.background_color= (255, 0, 0, 1)
            instance.disabled= True
        elif result == 'N':
            instance.text = ' '
            instance.background_color=(0, 255, 255, 0.5) 
            instance.disabled= True

        # Check for sunk ships
        barco_hundido = self.player2_board.barco_hundido()
        if barco_hundido :
            self.show_popup2()

        self.manager.current = 'CambioDePantalla'
    def show_popup(self, instance):
        popup = MyPopup_jugador1()
        popup.open() 


class CambioDePantalla(Screen):
    def __init__(self, player1_board, **kwargs):
        super(CambioDePantalla, self).__init__(**kwargs)
        self.player1_board = player1_board

        ContenedorB= BoxLayout(orientation="vertical")
       
        self.Jugador_En_Turno = Label(text="El turno de disparar es para el Jugador 2", font_size="30sp", size_hint_y=0.2)
        ContenedorB.add_widget(self.Jugador_En_Turno)

        Contenedor2 = BoxLayout(orientation='vertical')

        for numero_fila in range(10):
            fila = BoxLayout(orientation="horizontal")
            for numero_columna in range(10):
                casilla = Button(text='O', font_size=20, 
                                 disabled=False
                                 )
                casilla.fila = numero_fila
                casilla.columna = numero_columna
                casilla.bind(on_press=self.player2_fire)
                if self.player1_board.buscar_barco():
                    casilla.bind(on_press=self.show_popup)
                fila.add_widget(casilla)
            Contenedor2.add_widget(fila)

        ContenedorB.add_widget(Contenedor2)
        self.add_widget(ContenedorB)
    def show_popup2(self):
        popup = MyPopup_impacto()
        popup.open()

    def player2_fire(self, instance):

        result = self.player1_board.disparar(instance.fila, instance.columna, self.player1_board.tablero)

 
        if result == 'X':
            instance.text = 'X'
            instance.background_color= (255, 0, 0, 1)
            instance.disabled= True
        elif result == 'N':
            instance.text = ' '
            instance.background_color=(0, 255, 255, 0.5) 
            instance.disabled= True
        barco_hundido =self.player1_board.barco_hundido()
        if barco_hundido:
            self.show_popup2()

        self.manager.current = 'Turno_Jugador1'
  
    def show_popup(self, instance):
        popup = MyPopup_jugador2()
        popup.open()

class BattleshipApp(App):
    def build(self):
        sm = ScreenManager()

        # Create instances of screens
        Pantalla1 = GameScreen(name='Turno_Jugador1')
        Pantalla2 = CambioDePantalla(name='CambioDePantalla', player1_board=Pantalla1.player1_board)

        sm.add_widget(Pantalla1)
        sm.add_widget(Pantalla2)

        return sm

if __name__ == '__main__':
    BattleshipApp().run()
