import random
from colorama import Fore, Style


class TableroBatallaNaval:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [['O' for _ in range(self.columnas)] for _ in range(self.filas)]  # 'O' representa una celda vacía
        self.naves = {} 
    
    def nave_de_3_casillas(self):
        verificacion = False
        contador = 0
        barco1 = []
        barco2 = []        
        while not verificacion:
            orientacion_barcos = random.choice(["horizontal", "vertical"])
            direccion_horizontal= random.choice(["derecha", "izquierda"])
            direccion_vertical= random.choice(["arriba", "abajo"])
            numero_fila=random.randint(0,9)
            numero_columna=random.randint(0,9)
            if orientacion_barcos == "horizontal" and direccion_horizontal== "derecha":
                if numero_columna + 2 < 10:
                    casilla_vacia= True                    
                    for x  in range(3):                    
                        if self.tablero[numero_fila][numero_columna+x] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False
                            break                                    
                    if casilla_vacia == True:                    
                        for x in range(3):
                            self.tablero[numero_fila][numero_columna+x]= Fore.YELLOW + 'B' + Style.RESET_ALL
                        contador += 1
                        if contador == 1:
                            for direccion_barco in range(3):
                                barco1.append((numero_fila,numero_columna+ direccion_barco))
                                self.naves["barco numero 1"] = barco1
                        else:
                            for direccion_barco in range(3):
                                barco2.append((numero_fila,numero_columna+ direccion_barco))
                                self.naves["barco numero 2"] = barco2
                    else:
                        continue
                else:
                    continue
            if orientacion_barcos == "horizontal" and direccion_horizontal== "izquierda":
                if numero_columna - 2 > 0:
                    casilla_vacia= True                    
                    for x  in range(3):                    
                        if self.tablero[numero_fila][numero_columna-x] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False
                            break                                   
                    if casilla_vacia == True:                    
                        for x in range(3):
                            self.tablero[numero_fila][numero_columna-x]= Fore.YELLOW + 'B' + Style.RESET_ALL
                        contador += 1
                        if contador == 1:
                            for direccion_barco in range(3):
                                barco1.append((numero_fila,numero_columna- direccion_barco))
                                self.naves["barco numero 1"] = barco1
                        else:
                            for direccion_barco in range(3):
                                barco2.append((numero_fila,numero_columna- direccion_barco))
                                self.naves["barco numero 2"] = barco2
                    else:
                        continue
                else:
                    continue
            if orientacion_barcos == "vertical" and direccion_vertical == "arriba":
                if numero_fila - 2 > 0:
                    casilla_vacia= True                    
                    for x  in range(3):                    
                        if self.tablero[numero_fila-x][numero_columna] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False
                            break                                    
                    if casilla_vacia == True:
                        for x in range(3):
                            self.tablero[numero_fila-x][numero_columna]= Fore.YELLOW + 'B' + Style.RESET_ALL
                        contador += 1
                        if contador == 1:
                            for direccion_barco in range(3):
                                barco1.append((numero_fila- direccion_barco,numero_columna))
                                self.naves["barco numero 1"] = barco1
                        else:
                            for direccion_barco in range(3):
                                barco2.append((numero_fila- direccion_barco,numero_columna))
                                self.naves["barco numero 2"] = barco2
                    else:
                        continue
                else:
                    continue
            if orientacion_barcos == "vertical" and direccion_vertical == "abajo":
                if numero_fila + 2 < 10:
                    casilla_vacia= True                    
                    for x  in range(3):                    
                        if self.tablero[numero_fila+x][numero_columna] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False                                    
                    if casilla_vacia == True:
                        for x in range(3):
                            self.tablero[numero_fila+x][numero_columna]= Fore.YELLOW + 'B' + Style.RESET_ALL
                        contador += 1
                        if contador == 1:
                            for direccion_barco in range(3):
                                barco1.append((numero_fila+ direccion_barco,numero_columna))
                                self.naves["barco numero 1"] = barco1
                        else:
                            for direccion_barco in range(3):
                                barco2.append((numero_fila+ direccion_barco,numero_columna))
                                self.naves["barco numero 2"] = barco2
                    else:
                        continue
                else:
                    continue
            if contador == 2:
                verificacion = True
    def nave_de_2_casillas(self):
        verificacion = False
        contador = 0
        barco3 = []
        barco4 = []
        barco5 = []
        barco6= []
        while not verificacion:
            orientacion_barcos = random.choice(["horizontal", "vertical"])
            direccion_horizontal= random.choice(["derecha", "izquierda"])
            direccion_vertical= random.choice(["arriba", "abajo"])
            numero_fila=random.randint(0,9)
            numero_columna=random.randint(0,9)
            if orientacion_barcos == "horizontal" and direccion_horizontal== "derecha":
                if numero_columna + 1 < 10:
                    casilla_vacia= True                    
                    for x  in range(2):                    
                        if self.tablero[numero_fila][numero_columna+x] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False
                            break                                   
                    if casilla_vacia == True:                                                              
                        for x in range(2):
                            self.tablero[numero_fila][numero_columna+x]= Fore.GREEN + 'B' + Style.RESET_ALL
                        contador += 1
                        if contador == 1:
                            for direccion_barco in range(2):
                                barco3.append((numero_fila,numero_columna+ direccion_barco))
                                self.naves["barco numero 3"] = barco3
                        elif contador == 2:
                            for direccion_barco in range(2):
                                barco4.append((numero_fila,numero_columna+ direccion_barco))
                                self.naves["barco numero 4"] = barco4
                        elif contador == 3:
                            for direccion_barco in range(2):
                                barco5.append((numero_fila,numero_columna+ direccion_barco))
                                self.naves["barco numero 5"] = barco5
                        elif contador == 4:
                            for direccion_barco in range(2):
                                barco6.append((numero_fila,numero_columna+ direccion_barco))
                                self.naves["barco numero 6"] = barco6
                        
                    else:
                        continue
                else:
                    continue
            if orientacion_barcos == "horizontal" and direccion_horizontal== "izquierda":
                if numero_columna - 1 > 0:
                    casilla_vacia= True                    
                    for x  in range(2):                    
                        if self.tablero[numero_fila][numero_columna-x] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False
                            break                                   
                    if casilla_vacia == True:
                        for x in range(2):
                            self.tablero[numero_fila][numero_columna-x]= Fore.GREEN + 'B' + Style.RESET_ALL
                        contador += 1
                        if contador == 1:
                            for direccion_barco in range(2):
                                barco3.append((numero_fila,numero_columna-direccion_barco))
                                self.naves["barco numero 3"] = barco3
                        elif contador == 2:
                            for direccion_barco in range(2):
                                barco4.append((numero_fila,numero_columna- direccion_barco))
                                self.naves["barco numero 4"] = barco4
                        elif contador == 3:
                            for direccion_barco in range(2):
                                barco5.append((numero_fila,numero_columna- direccion_barco))
                                self.naves["barco numero 5"] = barco5
                        elif contador == 4:
                            for direccion_barco in range(2):
                                barco6.append((numero_fila,numero_columna- direccion_barco))
                                self.naves["barco numero 6"] = barco6
                    else:
                        continue                    
                else:
                    continue
            if orientacion_barcos == "vertical" and direccion_vertical == "arriba":
                if numero_fila - 1 > 0:
                    casilla_vacia= True                    
                    for x  in range(2):                    
                        if self.tablero[numero_fila-x][numero_columna] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False 
                            break                                   
                    if casilla_vacia == True:                                                                           
                            for x in range(2):
                                self.tablero[numero_fila-x][numero_columna]= Fore.GREEN + 'B' + Style.RESET_ALL
                            contador += 1
                            if contador == 1:
                                for direccion_barco in range(2):
                                    barco3.append((numero_fila- direccion_barco,numero_columna))
                                    self.naves["barco numero 3"] = barco3
                            elif contador == 2:
                                for direccion_barco in range(2):
                                    barco4.append((numero_fila- direccion_barco,numero_columna))
                                    self.naves["barco numero 4"] = barco4
                            elif contador == 3:
                                for direccion_barco in range(2):
                                    barco5.append((numero_fila- direccion_barco,numero_columna))
                                    self.naves["barco numero 5"] = barco5
                            elif contador == 4:
                                for direccion_barco in range(2):
                                    barco6.append((numero_fila- direccion_barco,numero_columna))
                                    self.naves["barco numero 6"] = barco6
                    else:
                        continue
                else:
                    continue
            if orientacion_barcos == "vertical" and direccion_vertical == "abajo":
                if numero_fila + 1 < 10:
                    casilla_vacia= True                    
                    for x  in range(2):                    
                        if self.tablero[numero_fila+x][numero_columna] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False
                            break                                    
                    if casilla_vacia == True:                                                         
                        for x in range(2):
                            self.tablero[numero_fila+x][numero_columna]= Fore.GREEN + 'B' + Style.RESET_ALL
                        contador += 1
                        if contador == 1:
                                for direccion_barco in range(2):
                                    barco3.append((numero_fila+direccion_barco,numero_columna))
                                    self.naves["barco numero 3"] = barco3
                        elif contador == 2:
                            for direccion_barco in range(2):
                                barco4.append((numero_fila+direccion_barco,numero_columna))
                                self.naves["barco numero 4"] = barco4
                        elif contador == 3:
                            for direccion_barco in range(2):
                                barco5.append((numero_fila+direccion_barco,numero_columna))
                                self.naves["barco numero 5"] = barco5
                        elif contador == 4:
                            for direccion_barco in range(2):
                                barco6.append((numero_fila+direccion_barco,numero_columna))
                                self.naves["barco numero 6"] = barco6
                    else:
                        continue 
                else:
                    continue
            if contador == 4:
                verificacion = True
    def nave_de_5_casillas(self):
        verificacion = False
        contador = 0
        barco7 = []
        while not verificacion:
            orientacion_barcos = random.choice(["horizontal", "vertical"])
            direccion_horizontal= random.choice(["derecha", "izquierda"])
            direccion_vertical= random.choice(["arriba", "abajo"])
            numero_fila=random.randint(0,9)
            numero_columna=random.randint(0,9)
            if orientacion_barcos == "horizontal" and direccion_horizontal== "derecha":
                if numero_columna + 4 < 10:
                    casilla_vacia= True                    
                    for x  in range(5):                    
                        if self.tablero[numero_fila][numero_columna+x] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False
                            break                                   
                    if casilla_vacia == True:                                                              
                        for x in range(5):
                            self.tablero[numero_fila][numero_columna+x]= Fore.RED + 'B' + Style.RESET_ALL
                        contador += 1
                        if contador == 1:
                            for direccion_barco in range(5):
                                barco7.append((numero_fila,numero_columna+ direccion_barco))
                                self.naves["barco numero 7"] = barco7
                        
                    else:
                        continue
                else:
                    continue
            elif orientacion_barcos == "horizontal" and direccion_horizontal== "izquierda":
                if numero_columna - 4 > 0:
                    casilla_vacia= True                    
                    for x  in range(5):                    
                        if self.tablero[numero_fila][numero_columna-x] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False
                            break                                   
                    if casilla_vacia == True:
                        for x in range(5):
                            self.tablero[numero_fila][numero_columna-x]= Fore.RED + 'B' + Style.RESET_ALL
                        contador += 1
                        if contador == 1:
                            for direccion_barco in range(5):
                                barco7.append((numero_fila,numero_columna- direccion_barco))
                                self.naves["barco numero 7"] = barco7
                    else:
                        continue                    
                else:
                    continue
            elif orientacion_barcos == "vertical" and direccion_vertical == "arriba":
                if numero_fila - 4 > 0:
                    casilla_vacia= True                    
                    for x  in range(5):                    
                        if self.tablero[numero_fila-x][numero_columna] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False 
                            break                                   
                    if casilla_vacia == True:                                                                           
                            for x in range(5):
                                self.tablero[numero_fila-x][numero_columna]= Fore.RED + 'B' + Style.RESET_ALL
                            contador += 1
                            if contador == 1:
                                for direccion_barco in range(5):
                                    barco7.append((numero_fila- direccion_barco,numero_columna))
                                    self.naves["barco numero 7"] = barco7
                    else:
                        continue
                else:
                    continue
            elif orientacion_barcos == "vertical" and direccion_vertical == "abajo":
                if numero_fila + 4 < 10:
                    casilla_vacia= True                    
                    for x  in range(5):                    
                        if self.tablero[numero_fila+x][numero_columna] == 'O':
                            casilla_vacia = True
                        else:
                            casilla_vacia = False
                            break                                    
                    if casilla_vacia == True:                                                         
                        for x in range(5):
                            self.tablero[numero_fila+x][numero_columna]= Fore.RED + 'B' + Style.RESET_ALL
                        contador += 1
                        if contador == 1:
                            for direccion_barco in range(5):
                                barco7.append((numero_fila+ direccion_barco,numero_columna))
                                self.naves["barco numero 7"] = barco7
                    else:
                        continue 
                else:
                    continue
            if contador == 1:
                verificacion = True                 

    def colocar_naves(self):
        claves = list(self.naves.keys())  
                 
        self.nave_de_3_casillas()
        self.nave_de_2_casillas()
        self.nave_de_5_casillas()        



         
    def imprimir_tablero(self):
        for fila in self.tablero:
            print(' '.join(fila))
    
    def contador_filas_columnas(self):
        cont_columnas= 0
        for fila in self.tablero:
            for columnas in self.tablero:
                cont_columnas += 1
        return cont_columnas
    
    def disparar(self,pos_fila, pos_columna, tablero):
        if tablero[pos_fila-1][pos_columna-1] == Fore.BLACK  + 'X' + Style.RESET_ALL or tablero[pos_fila-1][pos_columna-1] == Fore.BLUE + 'N' + Style.RESET_ALL:
            print("Ya disparaste en esta posicion")
        elif tablero[pos_fila-1][pos_columna-1] == Fore.RED + 'B' + Style.RESET_ALL or tablero[pos_fila-1][pos_columna-1] == Fore.YELLOW + 'B' + Style.RESET_ALL or tablero[pos_fila-1][pos_columna-1] == Fore.GREEN + 'B' + Style.RESET_ALL :
            print("¡Impacto!")
            tablero[pos_fila-1][pos_columna-1] = Fore.BLACK + 'X' + Style.RESET_ALL  # 'X' representa un impacto en un barco
            return 'X'
        else:
            print("¡Agua!")
            tablero[pos_fila-1][pos_columna-1] = Fore.BLUE + 'N' + Style.RESET_ALL  # 'M' representa un disparo al agua
            return "N"

        

    def barco_hundido(self):
        barco_hundido = False
        barcos_a_eliminar = []

        for nombre_barco, coordenadas in self.naves.items():
            barco_intacto = True
            for fila, columna in coordenadas:
                if self.tablero[fila][columna] != Fore.BLACK + 'X' + Style.RESET_ALL:
                    barco_intacto = False                    
                    break

            if barco_intacto:
                print("¡El barco", nombre_barco, "está hundido!")
                barcos_a_eliminar.append(nombre_barco)
                barco_hundido = True

        # Eliminar barcos hundidos del diccionario
        for nombre_barco in barcos_a_eliminar:
            del self.naves[nombre_barco]

        return barco_hundido
    def buscar_barco(self):
        for fila in self.tablero:
            for celda in fila:
                if celda == Fore.YELLOW + 'B' + Style.RESET_ALL or celda == Fore.GREEN + 'B' + Style.RESET_ALL or celda == Fore.RED + 'B' + Style.RESET_ALL:
                    return False  # Se encontró un barco
        return True  # No se encontró ningún barco
    
def ejecutarjuego():
        
    jugador1= TableroBatallaNaval(10, 10)
    jugador1.colocar_naves()
    jugador2= TableroBatallaNaval(10, 10)
    jugador2.colocar_naves()
    juego_acabado= False
    while not juego_acabado:
        jugador1.imprimir_tablero()
        fila = int(input("ingrese posicion de fila\n"))
        columna = int(input("ingrese posicion de columna\n"))
        jugador1.disparar(fila,columna, jugador2.tablero)
        jugador2.barco_hundido()
        juego_acabado= jugador2.buscar_barco()
        jugador2.imprimir_tablero()
        fila = int(input("ingrese posicion de fila\n"))
        columna = int(input("ingrese posicion de columna\n"))
        jugador2.disparar(fila,columna, jugador1.tablero)
        juego_acabado= jugador1.barco_hundido()
        jugador1.buscar_barco()


if __name__ == '__main__':
    ejecutarjuego()

