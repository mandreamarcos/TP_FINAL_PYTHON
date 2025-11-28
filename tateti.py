#TATETI ENTRE DOS PERSONAS

def mostrar_tablero_guia():
    print()
    print('*********************************************************************************')
    print('********************* BIENVENIDO JUEGO DEL TATETI *******************************')
    print('*********************************************************************************')
    print('INSTRUCCIONES: PARA LA POSICION ELIJA UN NUMERO SEGUN EL SIGUIENTE TABLERO GUIA.')
    print('               Si elije un casillero seleccionado por otro jugador, pierde turno.')
    print()
    print()
    print(f"1|2|3")
    print(f"4|5|6")
    print(f"7|8|9")
    return()

def mostrar_tablero(fila1, fila2, fila3):
    print('')
    print('Tablero:\n')
    print(f"{fila1[0]}|{fila1[1]}|{fila1[2]}")
    print(f"{fila2[0]}|{fila2[1]}|{fila2[2]}")
    print(f"{fila3[0]}|{fila3[1]}|{fila3[2]}")
    return()

def reemplazar_elemento(simbolo,jugada, fila1, fila2, fila3):

    if jugada == 1 or jugada == 2 or jugada == 3:
        if fila1[jugada-1] in ('X','O'):
            print('Ya está lleno ese casillero\n')
        else:
            fila1[jugada-1] = simbolo            
    elif  jugada == 4:
        if fila2[0] in ('X','O'):
            print('Ya esta lleno ese casillero\n')
        else:
            fila2[0] = simbolo
    elif  jugada == 5:
        if fila2[1] in ('X','O'):
            print('Ya esta lleno ese casillero\n')
        else:
            fila2[1] = simbolo
    elif jugada == 6:
        if fila2[2] in ('X','O'):
            print('Ya esta lleno ese casillero\n')
        else:
            fila2[2] = simbolo
    elif jugada == 7:
        if fila3[0] in ('X','O'):
            print('Ya esta lleno ese casillero\n')
        else:
            fila3[0] = simbolo
    elif jugada == 8:
        if fila3[1] in ('X','O'):
            print('Ya esta lleno ese casillero\n')
        else:
            fila3[1] = simbolo
    elif jugada == 9:
        if fila3[2] in ('X','O'):
            print('Ya esta lleno ese casillero\n')
        else:
            fila3[2] = simbolo
    return(fila1,fila2,fila3)

def revisar_jugada(simbolo):
    # Combinaciones ganadoras
    return (
        # veo si coinciden las filas
        (fila1[0] == fila1[1] == fila1[2] == simbolo) or
        (fila2[0] == fila2[1] == fila2[2] == simbolo) or
        (fila3[0] == fila3[1] == fila3[2] == simbolo) or
        # veo si coinciden las Columnas
        (fila1[0] == fila2[0] == fila3[0] == simbolo) or
        (fila1[1] == fila2[1] == fila3[1] == simbolo) or
        (fila1[2] == fila2[2] == fila3[2] == simbolo) or
        # veo si coinciden las Diagonales
        (fila1[0] == fila2[1] == fila3[2] == simbolo) or
        (fila1[2] == fila2[1] == fila3[0] == simbolo)
    )

def revisar_fin_juego(fila1,fila2,fila3):
        
        # veo si el juego terminó y nadie ganó
        i = 0
        fin_juego = 'S'
       
        while i < 3 and fin_juego != 'N':            
            if fila1[i] not in ('X','O'):
                fin_juego = 'N'
                break
            if fila2[i] not in ('X','O'):
                fin_juego = 'N'
                break
            if fila3[i] not in ('X','O'):
                fin_juego = 'N'
                break
            i += 1
       
        return(fin_juego)


# main
import  sys, os
os.system('cls')

sigue_jugando = 'S'

while sigue_jugando == 'S':

    # Inicializamos el tablero
    fila1 = ["_","_","_"]
    fila2 = ["_","_","_"]
    fila3 = ["_","_","_"]

    print('')
    mostrar_tablero_guia()
    print('')
    print('')
    mostrar_tablero(fila1, fila2, fila3)
    print('')
    print('')

    ganador = False
    fin_jugada = 'N'
    """"""

    while not ganador and  fin_jugada == 'N':
        print('')
        # Jugada JUGADOR 1
        valor_correcto = 'N'
        while valor_correcto == 'N':
            jugador_1 = input('JUGADOR 1 JUEGA CON LA ''X'' -  Indicar en que posición según GUIA: ')
            if str(jugador_1)  not in ('1','2','3','4','5','6','7','8','9'):
                print('Error - Ingrese un valor válido de 1 a 9')
                valor_correcto = 'N'
            else:
                valor_correcto = 'S'

        fila1,fila2,fila3 = reemplazar_elemento('X',int(jugador_1),fila1,fila2,fila3)
        mostrar_tablero(fila1, fila2, fila3)
        ganador = revisar_jugada('X')
        if ganador:
            print('')
            print('*******************************')
            print('Ganó el JUGADOR 1 con sus ''X''')
            print('*******************************')
            break
        fin_jugada = revisar_fin_juego(fila1,fila2,fila3)
    
        if fin_jugada == 'S':
            print('*********** Terminó el juego y nadie ganó *********************')
            break

        print('')
        # Jugada JUGADOR 2 (sé que podria hacer una funcion que le pase parametros para no repetir el mismo codigo
        # para ambos jugadores )
        valor_correcto = 'N'
        while valor_correcto == 'N':
            jugador_2 = input('JUGADOR 2 JUEGA CON ''O'' -  Indicar en que posición según GUIA: ').strip()
            if jugador_2 not in ('1','2','3','4','5','6','7','8','9'):
                print('Error - Ingrese un valor válido de 1 a 9')
                valor_correcto = 'N'
            else:
                valor_correcto = 'S'
    
        fila1,fila2,fila3 = reemplazar_elemento('O',int(jugador_2),fila1,fila2,fila3)
        mostrar_tablero(fila1, fila2, fila3)
        ganador = revisar_jugada('O')    
        if ganador:
            print('')
            print('*******************************')
            print('Ganó el JUGADOR 2 con sus ''O''')
            print('*******************************')
            break
        
        fin_jugada = revisar_fin_juego(fila1,fila2,fila3)
    
        if fin_jugada == 'S':
            print('*********** Terminó el juego y nadie ganó *********************')
            break
    
    sigue_jugando = 'X'
    while sigue_jugando not in ('S','N'):
        sigue_jugando = input('¿Desea seguir jugando? (S/N): ')
        if sigue_jugando == 'N':
            break
        elif sigue_jugando != 'S':
            print('Elija opción S/N')
    