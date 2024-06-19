import random
import os

os.system("clear")
palabras_ahorcado = [
    "python", "programacion", "desarrollo", "algoritmo", "computadora",
    "tecnologia", "internet", "software", "hardware", "inteligencia",
    "artificial", "robotica", "electronica", "ingenieria", "matematica",
    "estadistica", "física", "quimica", "biologia", "genetica",
    "medicina", "astronomia", "geografia", "historia", "filosofia",
    "literatura", "arte", "musica", "pintura", "escultura",
    "arquitectura", "dibujo", "fotografia", "cine", "teatro",
    "danza", "poesia", "novela", "cuento", "ensayo",
    "periodismo", "redaccion", "publicidad", "marketing", "comunicacion",
    "educacion", "pedagogia", "psicologia", "sociologia", "antropologia"
]
palabra = random.choice(palabras_ahorcado)
secreto = list("_" * len(palabra))
letras_falladas = []
vidas = 6
dibujo_ahoracado = list('''   +---+
   |   |
       |
       |
       |
       |
=========

''')
os.system("clear")
print(f"Bienvenido al ahorcado!!!\nLa palabra oculta contiene {len(palabra)} letras {' '.join(secreto)}\n\n\n") 
print("".join(dibujo_ahoracado)) 
while vidas > 0:        
    letra_escogida = input(f"Escoge una letra ")
    if letra_escogida in palabra:
        for indices, letra in enumerate(palabra):    
            if letra == letra_escogida:
                secreto[indices] = letra_escogida 
            os.system("clear")                      
            print(f"Felicidades tu letra está en la palabra oculta {' '.join(secreto)}") 
            print("".join(dibujo_ahoracado))             
        if palabra == "".join(secreto):
            print(f"FELICIDADES has acertado la palabra {''.join(secreto)}, te sobraron {vidas} vidas") 
            break        
    else:
        vidas -= 1
        letras_falladas.append(letra_escogida)
        os.system("clear")
        print(f"Lo siento, la palabra oculta no contiene la letra {letra_escogida}, las letras falladas son {letras_falladas}. \nSigue intentándolo {' '.join(secreto)} ")
        if vidas == 5:        
            dibujo_ahoracado[21] = "O"
            print("".join(dibujo_ahoracado))         
        if vidas == 4:
            dibujo_ahoracado[30] = "|"
            print("".join(dibujo_ahoracado))           
        if vidas == 3:
            dibujo_ahoracado[29] = "/"
            print("".join(dibujo_ahoracado))
        if vidas == 2:
            dibujo_ahoracado[31] = "\\"
            print("".join(dibujo_ahoracado))
        if vidas == 1:
            dibujo_ahoracado[38] = "/"
            print("".join(dibujo_ahoracado))
        if vidas == 0:  
            dibujo_ahoracado[40] = "\\"       
            print("".join(dibujo_ahoracado))  
else:
    print(f"Lo siento. Te has ahorcado la palabra era {palabra}")
