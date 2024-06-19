import random
import os

class TicTacToe:

    def __init__(self): # Método constructor 
        self.tablero_vacio = '''   |   |  
---+---+---
   |   |  
---+---+---
   |   |   '''

        self.tablero_lleno = ''' 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9 '''
        
        self.jugadas_permitidas = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Lista de jugadas permitidas
        self.indices = [1, 5, 9, 24, 28, 32, 47, 51, 55] # Índices correspondientes a las posiciones en el string del tablero
        self.posiciones_ganadoras = [
            (1, 5, 9), (24, 28, 32), (47, 51, 55),  # Filas
            (1, 24, 47), (5, 28, 51), (9, 32, 55),  # Columnas
            (1, 28, 55), (9, 28, 47)]               # Diagonales
        self.quien_juega = None


    def mensaje_bienvenida(self):
        """Muestra el mensaje de bienvenida y las opciones para elegir quién comienza"""
        os.system("clear")
        print("\n*** BIENVENIDO AL 3 EN RAYA ***\n\n")
        print("Quién empieza a jugar?\n")
        print('''Elige:
                M - Máquina 🤖 o
                J - Jugador 🙋 x
                S - No quiero elegir, que se haga un sorteo entre Máquina y Jugador 🤷
                ''')


    def elegir_quien_empieza(self):
        """Permite al usuario elegir quién comienza el juego o seleccionar aleatoriamente"""
        while True:
            self.quien_juega = input("Elección: ").upper()
            os.system('clear')
            if self.quien_juega == "S":
                jugadores = ["J", "M"]
                self.quien_juega = random.choice(jugadores)
                break
            elif self.quien_juega in "JM":
                break
            else:
                print("Opción no válida 👎 inténtalo de nuevo.")


    def rellena_casilla(self, casilla, quien_juega):
        """Rellena una casilla del tablero con el símbolo del jugador actual"""
        for i in range(1, 10):
            if casilla == i:
                indice = self.indices[i-1]
                self.tablero_vacio = self.tablero_vacio[:indice] + quien_juega + self.tablero_vacio[indice+1:]
                self.tablero_lleno = self.tablero_lleno[:indice] + " " + self.tablero_lleno[indice+1:]
                print()
                os.system("clear")
                print("\n\n")
                print(self.tablero_vacio, "\n")


    def ganar(self):
        """Verifica si hay una combinación ganadora en el tablero"""
        for pos in self.posiciones_ganadoras:
            if self.tablero_vacio[pos[0]] == self.tablero_vacio[pos[1]] == self.tablero_vacio[pos[2]] != " ":
                return True
        return False


    def eleccion_maquina(self):
        """Determina la jugada de la máquina con prioridad en ganar o bloquear al jugador"""
        # Prioridad 1: Verificar si la máquina puede ganar en la siguiente jugada
        for pos in self.posiciones_ganadoras:
            if self.tablero_vacio[pos[0]] == self.tablero_vacio[pos[1]] == "o" and self.tablero_vacio[pos[2]] == " ":
                return self.indices.index(pos[2]) + 1
            if self.tablero_vacio[pos[0]] == self.tablero_vacio[pos[2]] == "o" and self.tablero_vacio[pos[1]] == " ":
                return self.indices.index(pos[1]) + 1
            if self.tablero_vacio[pos[1]] == self.tablero_vacio[pos[2]] == "o" and self.tablero_vacio[pos[0]] == " ":
                return self.indices.index(pos[0]) + 1

        # Prioridad 2: Verificar si el jugador puede ganar en la siguiente jugada y bloquearlo
        for pos in self.posiciones_ganadoras:
            if self.tablero_vacio[pos[0]] == self.tablero_vacio[pos[1]] == "x" and self.tablero_vacio[pos[2]] == " ":
                return self.indices.index(pos[2]) + 1
            if self.tablero_vacio[pos[0]] == self.tablero_vacio[pos[2]] == "x" and self.tablero_vacio[pos[1]] == " ":
                return self.indices.index(pos[1]) + 1
            if self.tablero_vacio[pos[1]] == self.tablero_vacio[pos[2]] == "x" and self.tablero_vacio[pos[0]] == " ":
                return self.indices.index(pos[0]) + 1

        # Prioridad 3: Hacer una jugada aleatoria en una casilla libre
        return random.choice(self.jugadas_permitidas)


    def jugar(self):
        """Controla el flujo del juego alternando entre el jugador y la máquina"""
        while True:
            if self.quien_juega == "x":
                self.quien_juega = "M"
            if self.quien_juega == "o":
                self.quien_juega = "J"

            if self.quien_juega == "J":
                self.quien_juega = "x"
                print("\n\tEres la 'x'. Dime en qué casilla quieres hacer tu jugada?\n\n\tElige uno de los números que ves en el tablero:\n\n")
                print(self.tablero_lleno)

                while True:
                    jugada_jugador = int(input("\n\nCasilla: "))
                    os.system('clear')

                    if jugada_jugador in self.jugadas_permitidas:
                        self.jugadas_permitidas.remove(jugada_jugador)
                        break

                    else:
                        print("\nJugada no permitida ❌ debes elegir el número correspondiente a una casilla que esté vacía.\n")
                        print(self.tablero_lleno)
                        print()
                        print(self.tablero_vacio)

                self.rellena_casilla(jugada_jugador, self.quien_juega)
                if self.ganar():
                    print(f"\n\n!Enhorabuena! Has ganado 🥳\n\n")
                    break
                elif len(self.jugadas_permitidas) == 0:
                    print(f"\n\nNadie ha ganado este juego, ha sido empate, inténtalo otra vez.\n\n")
                    break

            elif self.quien_juega == "M":
                self.quien_juega = "o"
                jugada_maquina = self.eleccion_maquina()
                self.jugadas_permitidas.remove(jugada_maquina)
                self.rellena_casilla(jugada_maquina, self.quien_juega)
                if self.ganar():
                    print("\n\nLa máquina ha ganado 🤖 Inténtalo de nuevo!\n\n")
                    break
                elif len(self.jugadas_permitidas) == 0:
                    print(f"\n\nNadie ha ganado este juego, ha sido empate, inténtalo otra vez.\n\n")
                    break
                print("\nLa máquina es la 'o' e hizo su jugada, ahora es tu turno.")


# Ejecución principal
if __name__ == "__main__":
    juego = TicTacToe()
    juego.mensaje_bienvenida()
    juego.elegir_quien_empieza()
    juego.jugar()