import random
import os

from tarea1 import tarea1 as t1
from tarea2 import tarea2 as t2
from tarea3 import tarea3 as t3
from tarea4 import tarea4 as t4
from tarea5 import tarea5 as t5

print("*** PREGUNTAS DEL EXAMEN PARA LA NACIONALIDAD ESPAÑOLA ***")
print("----" *30,"\n")

numero_total_intentos = 7
# Si tiene 4 aciertos ganas y si tienes 4 fallos pierdes.
aciertos = 0
errores = 0

print('''Elige una tarea:
                      
                      1 - GOBIERNO, LEGISLACIÓN Y PARTICIPACIÓN CIUDADANA
                      2 - DERECHOS Y DEBERES FUNDAMENTALES
                      3 - ORGANIZACIÓN TERRITORIAL DE ESPAÑA - GEOGRAFÍA FÍSICA Y POLÍTICA
                      4 - CULTURA E HISTORIA DE ESPAÑA
                      5 - SOCIEDAD ESPAÑOLA''')

while True:
    
    tarea = input("\n\nINGRESA TU OPCIÓN DEL 1 AL 5 o 'q' para salir: ").lower()

    if tarea == "1":
        preguntas_respuestas = t1
    elif tarea == "2":
        preguntas_respuestas = t2
    elif tarea == "3":
        preguntas_respuestas = t3
    elif tarea == "4":
        preguntas_respuestas = t4
    elif tarea == "5":
        preguntas_respuestas = t5
    elif tarea == "q":
        print("\n\n¿Pero tan pronto? ¡Hasta luego!\n\n")
        break
    else:
        print("\nOpción no valida, vuelve a intentarlo.")
        break

    pregunta = (random.choice(list(preguntas_respuestas.keys())))
    print("\n\n",pregunta)
    print("----" *30)

    for clave, valor in preguntas_respuestas.items():
        if clave == pregunta:
            respuesta_correcta = valor[-1]
            if tarea == "2":
                respuestas = valor[:2]
            else:
                respuestas = valor[:3]
            for i in respuestas:
                print(i, end="\t\t")
        
    respuesta_jugador = input("Cuál es la respuesta correcta? ").lower()

    if respuesta_jugador in "abc":

        if respuesta_correcta == respuesta_jugador:
            aciertos += 1
            numero_total_intentos -= 1
            print(f"\nMuy bien, la respuesta correcta es {respuesta_correcta}. Tienes {aciertos} acierto(s).\n\n")

        else:
            errores += 1
            numero_total_intentos -=1
            print(f"\nLa respuesta correcta es {respuesta_correcta}. Tienes {errores} fallo(s).\n\n")
        
    else:
        print("Opción no válida, intenta otra vez.")

    if aciertos == 3:
        print("¡Enhorabuena! Ganaste el juego.")
        break
    elif errores == 3:
        print("Ooohhhh qué pena, perdiste. ¡No te rindas! Inténtalo de nuevo!")
        break
