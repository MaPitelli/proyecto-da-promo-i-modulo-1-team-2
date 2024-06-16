import random
import os

os.system("clear")
print("\n*** BIENVENIDO AL 3 EN RAYA ***\n\n")
print("Primero lo primero: quién empieza a jugar?\n")
print('''Elige:
        M - Máquina 🤖 o
        J - Jugador 🙋 x
        S - No quiero elegir, que se haga un sorteo entre Máquina y Jugador 🤷
        ''')

quien_juega = input("Elección: ").upper()


tablero_vacio = '''   |   |  
---+---+---
   |   |  
---+---+---
   |   |   '''

tablero_lleno = ''' 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9 '''

jugadas_permitidas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

indices = [1, 5, 9, 24, 28, 32, 47, 51, 55]


def rellena_casilla(casilla, quien_juega):
    global tablero_vacio, tablero_lleno
    for i in range(1, 10):
        if casilla == i:
            indice = indices[i-1]
            tablero_vacio = tablero_vacio[:indice] + quien_juega + tablero_vacio[indice+1:]
            tablero_lleno = tablero_lleno[:indice] + " " + tablero_lleno[indice+1:]
            print()
            os.system("clear")
            print("\n\n")
            print(tablero_vacio, "\n")


def ganar():
    if (tablero_vacio[1] == tablero_vacio[5] == tablero_vacio[9]) and tablero_vacio[1] != " ":
        return True
    elif (tablero_vacio[24] == tablero_vacio[28] == tablero_vacio[32]) and tablero_vacio[24] != " ": 
        return True
    elif (tablero_vacio[47] == tablero_vacio[51] == tablero_vacio[55]) and tablero_vacio[47] != " ":
        return True
    elif (tablero_vacio[1] == tablero_vacio[24] == tablero_vacio[47]) and tablero_vacio[1] != " ":
        return True
    elif (tablero_vacio[5] == tablero_vacio[28] == tablero_vacio[51]) and tablero_vacio[5] != " ":
        return True
    elif (tablero_vacio[9] == tablero_vacio[32] == tablero_vacio[55]) and tablero_vacio[9] != " ":
        return True
    elif (tablero_vacio[1] == tablero_vacio[28] == tablero_vacio[55]) and tablero_vacio[1] != " ":
        return True
    elif (tablero_vacio[9] == tablero_vacio[28] == tablero_vacio[47]) and tablero_vacio[9] != " ":
        return True
        

def eleccion_maquina():
    pass


if quien_juega == "S":
    jugadores = ["J", "M"]
    quien_juega = random.choice(jugadores)

while True:
    if quien_juega == "x":
        quien_juega = "M"
    if quien_juega == "o":
        quien_juega = "J"

    if quien_juega == "J":
        quien_juega = "x"
        print("\n\tEres la 'x'. Dime en qué casilla quieres hacer tu jugada?\n\n\tElige uno de los números que ves en el tablero:\n\n")
        print(tablero_lleno)
       
        while True:
            jugada_jugador = int(input("\n\nCasilla: "))
            
            if jugada_jugador in jugadas_permitidas:
                jugadas_permitidas.remove(jugada_jugador)
                break
            
            else:
                print("\nJugada no permitida ❌ debes elegir el número correspondiente a una casilla que esté vacía.\n")
                print(tablero_lleno)
                print()
                print(tablero_vacio)
        
        rellena_casilla(jugada_jugador, quien_juega)
        if ganar() == True:
            print(f"\n\n!Enhorabuena! Has ganado 🥳\n\n")
            break
        elif len(jugadas_permitidas) == 0:
            print(f"\n\nNadie ha ganado este juego, ha sido empate, inténtalo otra vez.\n\n")
            break

    elif quien_juega == "M":
        quien_juega = "o"
        jugada_maquina = int(random.choice(jugadas_permitidas))
        jugadas_permitidas.remove(jugada_maquina)
        rellena_casilla(jugada_maquina, quien_juega)
        if ganar() == True:
            print("\n\nLa máquina ha ganado 🤖 Inténtalo de nuevo!\n\n")
            break
        elif len(jugadas_permitidas) == 0:
            print(f"\n\nNadie ha ganado este juego, ha sido empate, inténtalo otra vez.\n\n")
            break
        print("\nLa máquina es la 'o' e hizo su jugada, ahora es tu turno.")
    
    else:
        print("Opción no válida 👎 inténtalo de nuevo.")
        break


# Falta implementar la función que deje la máquina mas competitiva: In progress.