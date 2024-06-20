import random
import os

from tarea1 import tarea1 as t1
from tarea2 import tarea2 as t2
from tarea3 import tarea3 as t3
from tarea4 import tarea4 as t4
from tarea5 import tarea5 as t5

class Trivia:

    def __init__(self):
        self.preguntas_respuestas = None
        self.aciertos = 0
        self.errores = 0
        self.respuesta_correcta = None
        self.temas = ["1 - GOBIERNO, LEGISLACIÓN Y PARTICIPACIÓN CIUDADANA",
                 "2 - DERECHOS Y DEBERES FUNDAMENTALES",
                 "3 - ORGANIZACIÓN TERRITORIAL DE ESPAÑA - GEOGRAFÍA FÍSICA Y POLÍTICA", 
                 "4 - CULTURA E HISTORIA DE ESPAÑA", 
                 "5 - SOCIEDAD ESPAÑOLA", 
                 "S - No quiero elegir, que se haga un sorteo"]
        # self.temas_elegidos = []

    def mensaje_bienvenida(self):
        os.system('clear') 
        print("\n\n","\t"*6,"    *** TRIVIAL ESPAÑA ***")
        print("\t"*3,"----" *20,"\n")
        print("\t"*2,"     Reglas del juego: Si tienes 3 aciertos ganas. Si tienes 3 fallos pierdes.\n")
        print("\t"*3,"----" *20,"\n")
        
        
    def mostrar_tareas(self):        
        # if self.temas_elegidos:
        #     for i in self.temas_elegidos:
        #         temas.remove(i)

        self.preguntas_respuestas = None
        print("\t\t\t  Elige un tema:\n")
        for i in self.temas:
            print("\t"*4,i)
                            
 
    def elige_tarea(self):
        while self.preguntas_respuestas == None:
            tarea = input("\n\n\t\t\t  INGRESA TU OPCIÓN o 'q' para salir: ").lower()
            os.system('clear')
            if tarea == "s":
                tareas = [t1, t2, t3, t4, t5]
                tarea_elegida = random.choice(tareas)
                self.preguntas_respuestas = tarea_elegida
                indice_tarea = tareas.index(tarea_elegida)
                print(f"\nTema elegido: {self.temas[indice_tarea]}\n")
            elif tarea == "1":
                self.preguntas_respuestas = t1
                # self.temas_elegidos.append("1 - GOBIERNO, LEGISLACIÓN Y PARTICIPACIÓN CIUDADANA")
                print(f"\nTema elegido: GOBIERNO, LEGISLACIÓN Y PARTICIPACIÓN CIUDADANA\n")
            elif tarea == "2":
                self.preguntas_respuestas = t2
                # self.temas_elegidos.append("2 - DERECHOS Y DEBERES FUNDAMENTALES")
                print(f"\nTema elegido: DERECHOS Y DEBERES FUNDAMENTALES\n")
            elif tarea == "3":
                self.preguntas_respuestas = t3
                # self.temas_elegidos.append("3 - ORGANIZACIÓN TERRITORIAL DE ESPAÑA - GEOGRAFÍA FÍSICA Y POLÍTICA")
                print(f"\nTema elegido: ORGANIZACIÓN TERRITORIAL DE ESPAÑA - GEOGRAFÍA FÍSICA Y POLÍTICA\n")
            elif tarea == "4":
                self.preguntas_respuestas = t4
                # self.temas_elegidos.append("4 - CULTURA E HISTORIA DE ESPAÑA")
                print(f"\nTema elegido: CULTURA E HISTORIA DE ESPAÑA\n")
            elif tarea == "5":
                self.preguntas_respuestas = t5
                # self.temas_elegidos.append("5 - SOCIEDAD ESPAÑOLA")
                print(f"\nTema elegido: SOCIEDAD ESPAÑOLA\n")
            elif tarea == "q":
                self.__despedir_juego()
                self.aciertos = 10
                break
            else:
                print("\nOpción no valida, vuelve a intentarlo.")
        

    def imprime_pregunta_respuestas(self):
        print("----" *20)
        pregunta = (random.choice(list(self.preguntas_respuestas.keys())))
        print("\n\n",pregunta)
        print("----" *20)
        for clave, valor in self.preguntas_respuestas.items():
            if clave == pregunta:
                self.respuesta_correcta = valor[-1]
                if self.preguntas_respuestas == t2:
                    respuestas = valor[:2]
                else:
                    respuestas = valor[:3]
                for i in respuestas:
                    print(i, end="\t\t")


    def verifica_respuesta_jugador(self):
        while True:    
            while True:
                respuesta_jugador = input("Cuál es la respuesta correcta? ").lower()
                if self.preguntas_respuestas == t2:
                    if respuesta_jugador in "ab":
                        break
                    else:
                        print("\nOpción no válida, intenta otra vez.\n\n")
                else:
                    break
            if respuesta_jugador in "abc":
                if self.respuesta_correcta == respuesta_jugador:
                    self.aciertos += 1
                    print(f"\nMuy bien, la respuesta correcta es {self.respuesta_correcta}. Tienes {self.aciertos} acierto(s).\n\n")
                    break
                else:
                    self.errores += 1
                    print(f"\nLa respuesta correcta es {self.respuesta_correcta}. Tienes {self.errores} fallo(s).\n\n")
                    break
            else:
                print("\nOpción no válida, intenta otra vez.\n\n")


    def ganar_perder(self):
        if self.aciertos == 3:
            print("¡Enhorabuena! Ganaste el juego.\n\n") 
        elif self.errores == 3:
            print("Ooohhhh qué pena, perdiste. ¡No te rindas! Inténtalo de nuevo!\n\n")


    def __despedir_juego(self):
        print("\n"*5,"\t"*3,"Esperamos verte de nuevo por aquí pronto 😊 ¡Hasta luego! 👋\n\n\n")
                

    def cambiar_tema(self):
        print('''Deseas seguir en el mismo tema o prefieres cambiar de tema?\n
                                                's' - seguir
                                                'c' - cambiar''')
        while True:
            opcion = input("\n\t\t\t\t\topción: ").lower()
            os.system('clear')
            if opcion in 'sc':
                break
            else:
                print("\nOpción no válida, intenta otra vez.\n\n")
                
        return opcion



# # Ejecución principal
# if __name__ == "__main__":
#     juego = Trivia()
#     juego.mensaje_bienvenida()
#     while juego.aciertos < 3 and juego.errores < 3:
#         # Solo pide cambiar de tema después de cada ronda completa
#         if not juego.preguntas_respuestas or juego.cambiar_tema() == 'c':
#             juego.mostrar_tareas()
#             juego.elige_tarea()
        
#         juego.imprime_pregunta_respuestas()
#         juego.verifica_respuesta_jugador()
#         juego.ganar_perder()

#         if juego.aciertos >= 3 or juego.errores >= 3:
#             break


if __name__ == "__main__":
    juego = Trivia()
    juego.mensaje_bienvenida()
    while juego.aciertos < 3 and juego.errores < 3:
        # Solo pide cambiar de tema después de cada ronda completa
        if not juego.preguntas_respuestas or juego.cambiar_tema() == 'c':
            juego.mostrar_tareas()
            juego.elige_tarea()
        
        if juego.preguntas_respuestas:  # Verifica que preguntas_respuestas no sea None
            juego.imprime_pregunta_respuestas()
            juego.verifica_respuesta_jugador()
            juego.ganar_perder()

        if juego.aciertos >= 3 or juego.errores >= 3:
            break