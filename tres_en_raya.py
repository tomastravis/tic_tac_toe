"""
Descripción del modulo aquí
"""

def dibujaTablero(tablero):
    '''
    Dibuja en la consola el tablero actual, indicando filas (1, 2, 3) y
    columnas (a, b, c).
    
            Parámetros:
                    tablero (list): una lista de listas definiendo el estado
                    del tablero de 3x3. Cada casilla puede contener uno de los
                    tres caracteres siguientes ' ', 'X', 'O'
    
            Devuelve:
                    none
    '''
    
    barra = '     +---+---+---+'
    
    # Encabezado
    print('\n')
    print('       a   b   c  ')

    # Filas
    print(barra)
    for i, c in enumerate(tablero):   
        print('   {0} | {1[0]} | {1[1]} | {1[2]} |'.format(1+i,c))
        print(barra)

    print('\n')
    
