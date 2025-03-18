'''
Hallar la edad de una persona, conociendo su año de nacimiento; declarar una CONSTANTE con el año actual.
'''
# Definicion de variables y captura de datos
anioActual = 2025                                                     # Se declara la constante con el año actual.

# Procesamiento y salida de datos
try:
     anioNacimiento = int(input("Por favor ingrese su año de nacimiento: "))    # Se captura el año de nacimiento del usuario.
     print(f"Su edad es: {anioActual - anioNacimiento} años.")                  # Se imprime la edad del usuario.
except ValueError:
     print("Por favor ingrese un año valido.")                                  # Se imprime un mensaje de error si el año ingresado no es valido.