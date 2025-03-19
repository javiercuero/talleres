'''
Punto 10: De su autoría crear un programa que contenga entradas, procesos y salidas.

a continuacion se crea un programa que simula un juego para adivinar un numero secreto entre 1 y 100,
se pide al usuario que ingrese un numero y se dan las pistas para que adivine, mostrando al final 
el numero de intentos y el numero secreto.
'''


import random  # Se importa la libreria random

# Aleatoreamente se define un numero entre 1 y 100
numeroSecreto = random.randint(1, 100)
intentos = 0                                                            # Cuenta el numero de intentos del usuario.

print("Este es el juego de adivinar Un número secreto")
print("Tu mision es adivinar el el numero secreto entre 1 y 100, Buena Suerte!")

while True:
    try:
        intento = int(input("Tu intento: "))                           # Se ingresa el numero del usuario.
        intentos += 1                                                  # se aumenta el contador de intentos.

        if intento < 1 or intento > 100:
            print("El número debe estar entre 1 y 100. Intenta de nuevo.")
            continue                                                    # se vuelva a pedir el numero al usuario.

        if intento < numeroSecreto:
            print("El numero secreto es mayor, intenta de nuevo.")
        elif intento > numeroSecreto:
            print("El numero secreto es menor, intenta de nuevo.")
        else:
            print(f" Bien hecho!, Adivinaste el número {numeroSecreto} en un total de {intentos} intentos.")
            break                                                       # Termina el bucle cuando el usuario adivina el numero secreto.

    except ValueError:
        print("Error!, ingresa un numero valido entre el rango de 1 a 100.")
