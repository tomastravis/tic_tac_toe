#=============================================================================#
#                                                                             #
#                                Entrega 3                                    # 
#                                                                             #
#=============================================================================#
#%%

import tres_en_raya as TER

#==============
# EJERCICIO 1 |  Comprobar fin de la partida
#==============

TER.dibujaTablero([[' ', 'O', 'O'],
                   ['X', 'O', 'O'],
                   ['O', 'X', 'X']])


def compruebaTablero(L):
    
    if (['X','X','X'] in [L[i] for i in range(0,3)] or                              # Comprueba las filas para 'X'
        ['X','X','X'] in [[L[i][j] for i in range(0,3)] for j in range(0,3)] or     # Comprueba las columnas
        ['X','X','X'] in [[L[i][i] for i in range(0,3)]] or                         # Comprueba la diagonal
        ['X','X','X'] in [[L[0][2], L[1][1], L[2][0]]]):                            # Comprueba la diagonal en sentido contrario
        print('¡Enhorabuena! ¡Has ganado!')
        TER.dibujaTablero(L)
        return 3                                                                    # Si gana el jugador devuelve '3' (arbitrario para luego)
        
    elif (['O','O','O'] in [L[i] for i in range(0,3)] or                            # Igual para las 'O'
          ['O','O','O'] in [[L[i][j] for i in range(0,3)] for j in range(0,3)] or   
          ['O','O','O'] in [[L[i][i] for i in range(0,3)]] or                       
          ['O','O','O'] in [[L[0][2], L[1][1], L[2][0]]]):                            
          print('¡Enhorabuena! Ha ganado la máquina')
          TER.dibujaTablero(L)
          return 2                                                                   # # Si gana la máquina devuelve '2' (arbitrario para luego)
          
    elif (True in [L[i][j] == ' ' for i in range(0,3) for j in range(0,3)]):         # Si ninguno ha ganado todavía y quedan casillas por jugar lo comunica.
          # print('¡Sigue jugando!')
          TER.dibujaTablero(L)
          return 0                                                                   # Si la partida no ha acabado la funcion vale 0
                                                                                     
    else:
          print('La partida ha acabado en empate')                                   # Si no se cumple ninguna de los dos la partida ha acabado en empate
          TER.dibujaTablero(L)
          return 1                                                                   # Si la partida acaba en empate la función devuelve 1 (arbitrario para luego)
             
#%%
#==============
# EJERCICIO 2 | Movimiento del jugador
#==============
        
# Durante los ejercicios estableceremos que el jugador usa el símbolo 'X' para jugar 
# y que la máquina usará el símbolo 'O' 

TER.dibujaTablero([[' ', 'X', 'O'],
                   ['X', 'O', 'O'],
                   ['X', 'O', 'X']])


def mueveJugador(L):   
    
    # Si la partida ha acabado la función se lo comunica al jugador y no se ejecuta la función.
    if compruebaTablero(L) != 0:
        print('No puedes jugar en una partida que ya ha acabado')
        return
    
    while True:
        entrada = input('\nIntroduce la fila (1, 2, ó 3) y la columna (a, b, ó c) donde quieras jugar: ')

        # Comprobamos que la entrada está bien escrita:
        if len(entrada) == 2 and entrada[0] in ['1', '2', '3'] and entrada[1] in ['a', 'b', 'c']:
            fila = int(entrada[0]) - 1
            col_l = entrada[1]
            col = ord(col_l) - 97

            # Si la casilla no está ocupada entonces sale del bucle
            if L[fila][col] == ' ':
                break  
            
            # Pero si ya está ocupada entonces vuelve al principio
            else:
                print('\nLa casilla elegida ya está ocupada. Introduce una casilla vacía.')
        else: 
            print('\nNo has introducido tu movimiento en el formato correcto. Inténtalo de nuevo')


    # If the move is played correctly, save the move on the board and check the game state
    L[fila][col] = 'X' 
    print('\nTu movimiento ha sido guardado con éxito!')
    compruebaTablero(L)

    
    
#%%

import random

#==============
# EJERCICIO 3 | Movimiento de la IA
#==============

TER.dibujaTablero([[' ', 'O', 'O'],
                   [' ', ' ', ' '],
                   [' ', 'O', ' ']])

def mueveIA(L): 
    
    # Si la partida ha acabado no debería pdoer mover así que finalizaríamos la función:
    if compruebaTablero(L) != 0:
        print('No puedes jugar en una partida que ya ha acabado')
        return
    
    # Creamos una lista de índices donde no se haya jugado todavía.
    I = [(i,j) for i in range(0,3) for j in range(0,3) if L[i][j] == ' '] 
    
    # Elegimos uno al azar y marcamos la jugada de la máquina.
    ii = random.choice(I)    
    L[ii[0]][ii[1]] = 'O'
    
    print('\nLa máquina ha jugado')
    #compruebaTablero(L)
    
    
#%%
#==============
# EJERCICIO 4 | Jugar partida
#==============


def nuevoJuego():
    
    # Predefinimos un tablero vacío para la partida
    ganador = 0
    L = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
    print('\n¡Comienza una nueva partida! Primero jugará la máquina')
    
    # Mientras la partida no haya acabado sigue jugando
    while ganador == 0:
        mueveIA(L)
        mueveJugador(L)
        ganador = compruebaTablero(L)
        
    # Para poder gestionar el torneo, vamos a hacer que la funcion devuelva un número según quién haya ganado:
    return compruebaTablero(L)
    


#%%
#==============
# EJERCICIO 5 | Jugar torneo
#==============

def nuevoTorneo():
    
    # Definimos variables auxiliares para hacer las comprobaciones durante el torneo:
    n_partidas = 0
    n_IA = 0
    n_jugador = 0

    # Mientras ninguno de los dos haya ganado 2 partidas (porque el torneo es al mejor de 3)
    # sigue generando partidas:
    while n_IA < 2 and n_jugador < 2:
        
          # El ganador de cada partida se registrará en 'resultado_juego':
          resultado_juego = nuevoJuego()

          # Y dependiendo que quien gana se le añadirá a la cuenta uno más. 
          # También se registran el número de partidas por cada victoria y no por cada empate.
          if resultado_juego == 2:
             n_IA += 1
             n_partidas += 1
             print('Te ha ganado la máquina... ¡Espabila!')

          elif resultado_juego == 3:
               n_jugador += 1
               n_partidas += 1
               print('¡HAS GANADO LA PARTIDA! SIGUE ASÍ')
          elif resultado_juego == 1:
               print('Habéis empatado...Suerte a la próxima')
               
          print('-'*50)
          print('PARTIDAS GANADAS POR LA MÁQUINA: ', n_IA)
          print('PARTIDAS QUE HAS GANADO: ', n_jugador)
          print('-'*50)
          input('\nPulsa enter para seguir')

    if n_IA == 2:
        print('\nEl ganador del torneo es........ la máquina!!!!!')

    elif n_jugador == 2:
        print('\n¡¡¡HAS GANADO EL TORNEO!!!!!')
        
        

#%%
#==============
# EJERCICIO 6 | IA avanzada
#==============

import random

def mueveIA2(L, dificultad):
    if dificultad == 'facil':
        mueveIA(L)
    elif dificultad == 'dificil':
        
        # Comprobamos movimientos ganadores
        for i in range(3):
            # Comprueba filas
            if L[i].count('O') == 2 and ' ' in L[i]:
                j = L[i].index(' ')
                L[i][j] = 'O'
                return

            # Comprueba columnas
            if [L[fila][i] for fila in range(3)].count('O') == 2 and ' ' in [L[fila][i] for fila in range(3)]:
                fila = [L[fila][i] for fila in range(3)].index(' ')
                L[fila][i] = 'O'
                return

        # Check diagonals
        if [L[i][i] for i in range(3)].count('O') == 2 and ' ' in [L[i][i] for i in range(3)]:
            j = [L[i][i] for i in range(3)].index(' ')
            L[j][j] = 'O'
            return

        if [L[i][2 - i] for i in range(3)].count('O') == 2 and ' ' in [L[i][2 - i] for i in range(3)]:
            j = [L[i][2 - i] for i in range(3)].index(' ')
            L[j][2 - j] = 'O'
            return

        # Si no hay movimientos ganadores, elegirá una casilla vacía aleatoria
        I = [(i, j) for i in range(3) for j in range(3) if L[i][j] == ' ']
        if I:
            i, j = random.choice(I)
            L[i][j] = 'O'

    compruebaTablero(L)
    
    


nuevoTorneo()








