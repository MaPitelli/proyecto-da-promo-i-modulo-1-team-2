import streamlit as st
import random

from tarea1 import tarea1 as t1
from tarea2 import tarea2 as t2
from tarea3 import tarea3 as t3
from tarea4 import tarea4 as t4
from tarea5 import tarea5 as t5

class Trivial:

    def __init__(self):
        self.preguntas_respuestas = None
        self.aciertos = 0
        self.errores = 0
        self.respuesta_correcta = None
        self.temas = {
            "1": "GOBIERNO, LEGISLACIÓN Y PARTICIPACIÓN CIUDADANA",
            "2": "DERECHOS Y DEBERES FUNDAMENTALES",
            "3": "ORGANIZACIÓN TERRITORIAL DE ESPAÑA - GEOGRAFÍA FÍSICA Y POLÍTICA",
            "4": "CULTURA E HISTORIA DE ESPAÑA",
            "5": "SOCIEDAD ESPAÑOLA",
            "S": "Sorteo"
        }

    def mostrar_tareas(self):        
        st.subheader("Elige un tema:")
        tema_elegido = st.selectbox("Selecciona un tema", list(self.temas.values()))
        return tema_elegido

    def elige_tarea(self, tema):
        if tema == "Sorteo":
            tareas = [t1, t2, t3, t4, t5]
            tarea_elegida = random.choice(tareas)
            self.preguntas_respuestas = tarea_elegida
        else:
            tema_invertido = {v: k for k, v in self.temas.items()}
            tarea_elegida = tema_invertido[tema]
            if tarea_elegida == "1":
                self.preguntas_respuestas = t1
            elif tarea_elegida == "2":
                self.preguntas_respuestas = t2
            elif tarea_elegida == "3":
                self.preguntas_respuestas = t3
            elif tarea_elegida == "4":
                self.preguntas_respuestas = t4
            elif tarea_elegida == "5":
                self.preguntas_respuestas = t5

    def imprime_pregunta_respuestas(self):
        st.subheader(f"Pregunta:")
        pregunta = random.choice(list(self.preguntas_respuestas.keys()))
        st.write(pregunta)
        st.subheader(f"Opciones:")
        respuestas = self.preguntas_respuestas[pregunta]
        for i, respuesta in enumerate(respuestas):
            st.write(f"{chr(65 + i)}. {respuesta}")

    def verifica_respuesta_jugador(self):
        respuesta_jugador = st.text_input("Cuál es la respuesta correcta? (Escribe A, B, o C)")
        respuesta_jugador = respuesta_jugador.lower()
        if respuesta_jugador in "abc":
            if self.respuesta_correcta == respuesta_jugador:
                self.aciertos += 1
                st.write(f"Muy bien, la respuesta correcta es {self.respuesta_correcta}. Tienes {self.aciertos} acierto(s).")
            else:
                self.errores += 1
                st.write(f"La respuesta correcta es {self.respuesta_correcta}. Tienes {self.errores} fallo(s).")
        else:
            st.write("Opción no válida, intenta otra vez.")

    def ganar_perder(self):
        if self.aciertos == 3:
            st.write("¡Enhorabuena! Ganaste el juego.")
        elif self.errores == 3:
            st.write("Ooohhhh qué pena, perdiste. ¡No te rindas! Inténtalo de nuevo.")

    def cambiar_tema(self):
        return st.radio("Deseas seguir en el mismo tema o prefieres cambiar de tema?", ('s', 'c'))

if __name__ == "__main__":
    juego = Trivial()
    st.title("Trivial España")
    st.write("Bienvenido al Trivial España. Reglas del juego: Si tienes 3 aciertos ganas. Si tienes 3 fallos pierdes.")
    while juego.aciertos < 3 and juego.errores < 3:
        tema = juego.mostrar_tareas()
        juego.elige_tarea(tema)
        
        juego.imprime_pregunta_respuestas()
        juego.verifica_respuesta_jugador()
        juego.ganar_perder()

        st.button("Siguiente")
