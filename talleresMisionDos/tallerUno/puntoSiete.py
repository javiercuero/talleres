import math

def calcularRaiz(a, b, c):                                                      # Se determina funcion para calcular raices
     discriminante = b**2 - 4*a*c

     if discriminante < 0:                                                      # si la determinante es negativa, no hay solucion.
          return "Error: El discriminante es negativo, no hay solución en los reales."

# Se calculan las raices
     raizPositiva = (-b + math.sqrt(discriminante)) / (2 * a)                   # Se calcula la raiz positiva
     raizNegativa = (-b - math.sqrt(discriminante)) / (2 * a)                   # Se calcula la raiz negativa

     return raizPositiva, raizNegativa

try:                                                                            # Se captura la excepcion de error en caso de que el usuario no ingrese un valor numerico
     a = float(input("Ingrese el valor de a: "))

     if a == 0:                                                                 # Si a es igual a 0, no es una ecuacion cuadratica
          print("Error: No es una ecuación cuadrática, 'a' no puede ser 0.")
     else:
          b = float(input("Ingrese el valor de b: "))
          c = float(input("Ingrese el valor de c: "))

          resultado = calcularRaiz(a, b, c)                                     # Se llama a la funcion para calcular las raices

          print(f"Las raíces son: Raíz Positiva = {resultado[0]} y Raíz Negativa = {resultado[1]}") # Se imprime los resultados.

except ValueError:
     print("Error: Ingrese un valor numérico válido.")