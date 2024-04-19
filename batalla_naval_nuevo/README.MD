#BATALLA NAVAL

Este proyecto implementa el juego de Batalla Naval en Python. Consiste en un tablero de 10x10 celdas en el que se colocan barcos de diferentes tamaños y los jugadores intentan adivinar la ubicación de los barcos oponentes para hundirlos.

Descripción del código
El código proporcionado consta de dos archivos principales:

main.py
Este archivo contiene la implementación del juego de Batalla Naval. Aquí se define la clase TableroBatallaNaval, que representa el tablero de juego y contiene métodos para colocar barcos, disparar y verificar el estado del tablero. Además, se definen excepciones personalizadas relacionadas con el juego.

pruebas.py
Este archivo contiene pruebas unitarias para validar el funcionamiento del juego. Se utilizan las bibliotecas unittest y main para realizar las pruebas en la clase TableroBatallaNaval.

Funcionalidades principales
Colocar Naves: El método colocar_naves() de la clase TableroBatallaNaval coloca aleatoriamente barcos de diferentes tamaños en el tablero.
Disparar: El método disparar() permite al jugador disparar a una posición específica del tablero y determina si hubo un impacto en un barco o si fue un disparo al agua.
Imprimir Tablero: El método imprimir_tablero() muestra en la consola el estado actual del tablero.
Validaciones: Se realizan validaciones para verificar que las coordenadas de disparo estén dentro del rango válido y que no se dispare dos veces en la misma posición.
Dependencias
El proyecto depende de las siguientes bibliotecas de Python:

random: Utilizada para la generación de números aleatorios.
colorama: Utilizada para imprimir texto con colores en la consola.
Para instalar las dependencias, puedes utilizar el siguiente comando:

bash
pip install colorama

Ejecución
Para ejecutar el juego de Batalla Naval, simplemente ejecuta el archivo main.py. A continuación, se muestra un ejemplo de cómo se puede usar el código:


# Crear un tablero de Batalla Naval de 10x10
tablero = main.TableroBatallaNaval(10, 10)

# Colocar los barcos en el tablero
tablero.colocar_naves()

# Imprimir el estado inicial del tablero
tablero.imprimir_tablero()

# Disparar a una posición específica
tablero.disparar(3, 2)

# Imprimir el estado del tablero después del disparo
tablero.imprimir_tablero()
