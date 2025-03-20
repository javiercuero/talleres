import math

def calcularRaiz(a, b, c):                                                      # Se determina funcion para calcular raices
     discriminante = b**2 - 4*a*c

     if discriminante < 0:                                                      # si la determinante es negativa, no hay solucion.
          return "Error: El discriminante es negativo, no hay solución en los reales."

# Se calculan las raices
     raizPositiva = (-b + math.sqrt(discriminante)) / (2 * a)
     raizNegativa = (-b - math.sqrt(discriminante)) / (2 * a)

     return raizPositiva, raizNegativa

try:
     a = float(input("Ingrese el valor de a: "))

     if a == 0:
          print("Error: No es una ecuación cuadrática, 'a' no puede ser 0.")
     else:
          b = float(input("Ingrese el valor de b: "))
          c = float(input("Ingrese el valor de c: "))

          resultado = calcularRaiz(a, b, c)

          print(f"Las raíces son: Raíz Positiva = {resultado[0]} y Raíz Negativa = {resultado[1]}")

except ValueError:
     print("Error: Ingrese un valor numérico válido.")