'''
Hallar la edad de una persona, conociendo su año de nacimiento; declarar una CONSTANTE con el año actual.
'''
# Definicion de variables y captura de datos
anioActual = int(2025)                                                     # Se declara la constante con el año actual.
anioNacimiento = int(input("Por favor ingrese su año de nacimiento: "))    # Se captura el año de nacimiento del usuario.

# Procesamiento y salida de datos

print(f"Su edad es: {anioActual - anioNacimiento} años.")                  # Se imprime la edad del usuario.