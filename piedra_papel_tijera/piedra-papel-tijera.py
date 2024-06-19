
# Importa la biblioteca random para generar elecciones aleatorias
import random 
import os

os.system("clear")
# variable para controlar si se debe volver a jugar
volver_a_jugar = 's' 

# Bucle principal que se ejecuta mientras el jugador quiera volver a jugar
while volver_a_jugar == 's':

# Inicializa los contadores de partidas ganadas para el jugador y la máquina
    partidas_ganadas_jugador = 0

    partidas_ganadas_maquina = 0

    
# Bucle que se ejecuta hasta que el jugador o la máquina ganen 3 partidas

    while partidas_ganadas_jugador < 3 and partidas_ganadas_maquina < 3:

        #El jugador elije su opción
        
        jugador = input('''introduce:
                1 si quieres ✊
                2 si quieres 🖐️
                3 si quieres ✌️  
                ''')
        
        #Cambiamos el valor de la variable de la elección del jugador (1, 2, 3) a (✊, 🖐️, ✌️)

        if jugador == "1":
            jugador = "✊"

        elif jugador == "2":
            jugador = "🖐️"

        elif jugador == "3":
            jugador = "✌️"

 # Si el jugador no elige una opción válida, muestra un mensaje y vuelve a pedirle la entrada
        
        else:
            print("No has elegido opción correcta ❌❌")
    
            continue  # Salta el resto del bucle y vuelve a pedir la entrada del jugador

        #La maquina elige su opción de forma aleatoria

        maquina = ("✊", "🖐️", "✌️")
        maquina = random.choice(maquina)

#Hacemos las comparativas para ver quien ha ganado

#Las opciones donde el jugador gana:

        if (maquina == "✊" and jugador == "🖐️") or (maquina == "🖐️" and jugador == "✌️") or (maquina == "✌️" and jugador == "✊"):
            
            partidas_ganadas_jugador = partidas_ganadas_jugador +1 # Incrementa el contador de partidas ganadas del jugador

            print("el 🧟‍♀️ ha sacado",jugador, "y la 🤖", maquina,"ha ganado el 🧟‍♀️")       

#Las opciones donde la máquina gana:

        if (maquina == "✊" and jugador == "✌️") or (maquina == "🖐️" and jugador == "✌️") or (maquina == "✌️" and jugador == "🖐️"):    
            
            partidas_ganadas_maquina = partidas_ganadas_maquina +1 # Incrementa el contador de partidas ganadas de la máquina

            print("el 🧟‍♀️ ha sacado",jugador, "y la 🤖",maquina,"ha ganado la 🤖")
            
#Las opciones donde la máquina y el jugador empatan:

        if (maquina == "✊" and jugador == "✊") or (maquina == "🖐️" and jugador == "🖐️") or (maquina == "✌️" and jugador == "✌️"):

            print("el 🧟‍♀️ ha sacado",jugador, "y la 🤖", maquina,"🤝")

  # Muestra quién ha ganado la serie de 3 partidas

    if partidas_ganadas_maquina > partidas_ganadas_jugador:
            print("Ha ganado la 🤖")

    else:
        
        print("Ha ganado el 🧟‍♀️")

# Pregunta al jugador si quiere volver a jugar
    volver_a_jugar = input("¿Quieres volver a jugar(s) o no(n)?")

# Mensaje de despedida
print("Hasta la próxima 👋👋")