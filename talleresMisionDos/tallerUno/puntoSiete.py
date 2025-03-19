import math
# De entrada

b = float(input("Ingrese el valor de b: "))
a = float(input("Ingrese el valor de a: "))
c = float(input("Ingrese el valor de c: "))

# determinar el discriminante
discriminante = math.sqrt(b**2 - 4*a*c)

#funcion para calcular raiz positiva
def calcularRaizPositiva(a,b,c):

     if discriminante < 0:
          print("Error: El discriminante es negativo, no hay solucion en los reales.")
          exit()
     return( -b + math.sqrt(discriminante)) / (2 * a)

#funcion para calcular raiz negativa

def calcularRaiznegativa(a,b,c):

     if discriminante < 0:
          print("Error: El discriminante es negativo, no hay solucion en los reales.")
          exit()
     return( -b - math.sqrt(discriminante)) / (2 * a)
# datos de prueba
# a,b,c = 1, -3, 2
#funciones
raizPositiva = calcularRaizPositiva(a,b,c)
raizNegativa = calcularRaiznegativa(a,b,c)
#Mostrar resultados
print(f"Las raíces son: raizPositiva={raizPositiva} y raizNegativa={raizNegativa}")