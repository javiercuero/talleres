'''
Leer las tres notas de los parciales y mostrar su definitiva aplicando los respectivos porcentajes:
Primer y Segundo Parcial 25%, Final del 20% 
y los Talleres 30% (tres talleres por separado)
'''
# declaración de variables 
while True:                                                 # Se define captura de datos para el primer parcial
     try:
          parcial1 = float(input("Ingrese la nota del primer parcial (entre 0 y 5): "))
          if 0 <= parcial1 <= 5:
               break
          else:
               print("Error, la nota ingresada no se encentra en el rango permitido (entre 0 y 5), Intente nuevamente.")
     except ValueError: 
          print("Error, Debe ingresar un número.")

while True:                                                 # Se define captura de datos para el segundo parcial
     try:
          parcial2 = float(input("Ingrese la nota del segundo parcial (entre 0 y 5): "))
          if 0 <= parcial2 <= 5:
               break
          else:
               print("Error, la nota ingresada no se encentra en el rango permitido (entre 0 y 5), Intente nuevamente.")
     except ValueError: 
          print("Error, Debe ingresar un número.")

while True:                                                 # Se define captura de datos para el tercer parcial
     try:
          parcial3 = float(input("Ingrese la nota del tercer parcial (entre 0 y 5): "))
          if 0 <= parcial3 <= 5:
               break
          else:
               print("Error, la nota ingresada no se encentra en el rango permitido (entre 0 y 5), Intente nuevamente.")
     except ValueError: 
          print("Error, Debe ingresar un número.")

while True:                                                 # Se define captura de datos para el primer taller
     try:
          taller1 = float(input("Ingrese la nota del primer taller (entre 0 y 5): "))
          if 0 <= taller1 <= 5:
               break
          else:
               print("Error, la nota ingresada no se encentra en el rango permitido (entre 0 y 5), Intente nuevamente.")
     except ValueError: 
          print("Error, Debe ingresar un número.")

while True:                                                 # Se define captura de datos para el segundo taller
     try:
          taller2 = float(input("Ingrese la nota del segundo taller (entre 0 y 5): "))
          if 0 <= taller2 <= 5:
               break
          else:
               print("Error, la nota ingresada no se encentra en el rango permitido (entre 0 y 5), Intente nuevamente.")
     except ValueError:
          print("Error, Debe ingresar un número.")

while True:                                                 # Se define captura de datos para el tercer taller
     try:
          taller3 = float(input("Ingrese la nota del tercer taller (entre 0 y 5): "))
          if 0 <= taller3 <= 5:
               break
          else:
               print("Error, la nota ingresada no se encentra en el rango permitido (entre 0 y 5), Intente nuevamente.")
     except ValueError:
          print("Error, Debe ingresar un número.")

# variable fijas de los porcentajes de cada parcial
porcent1 = 0.25                                             # Se definen los porcentajes para parcial 1 y 2
porcent2 = 0.20                                             # se definen los porcentajes para el parcial 3
porcent3 = 0.10                                             # Se definen los porcentajes para los talleres

# Se calcula la nota definitiva de cada parcial
definitiva1 = round(parcial1 * porcent1, 2)                         # Se calcula la nota definitiva del primer parcial
definitiva2 = round(parcial2 * porcent1, 2)                         # Se calcula la nota definitiva del segundo parcial
definitiva3 = round(parcial3 * porcent2, 2)                          # Se calcula la nota definitiva del tercer parcial
definitivaTaller1 = round(taller1 * porcent3, 2)                     # Se calcula la nota definitiva del primer taller
definitivaTaller2 = round(taller2 * porcent3, 2)                     # Se calcula la nota definitiva del segundo taller
definitivaTaller3 = round(taller3 * porcent3, 2)                     # Se calcula la nota definitiva del tercer taller

# Se calcula la nota definitiva de los parciales y talleres
definitivaParciales = definitiva1 + definitiva2 + definitiva3
definitivaTalleres = definitivaTaller1 + definitivaTaller2 + definitivaTaller3

#se calcula la nota definitiva total
definitivaTotal = round(definitivaParciales + definitivaTalleres, 2)

# Se imprime la nota definitiva total
print("_" * 90)
print(f"La nota definitiva es de: {definitivaTotal}\n")
print(f"La nota definitiva de los parciales es de: {definitivaParciales}")
print(f"Parcial 1 \t Definitiva \t Parcial 2 \t Definitiva \t Parcial 3 \t Definitiva ")
print("_" * 90)
print(f"{parcial1} \t\t {definitiva1} \t\t {parcial2} \t\t {definitiva2} \t\t {parcial3} \t\t {definitiva3}\n")
print(f"La nota definitiva de los talleres es de: {definitivaTalleres}")
print(f"Taller 1 \t Definitiva \t Taller 2 \t Definitiva \t Taller 3 \t Definitiva ")
print("_" * 90)
print(f"{taller1} \t\t {definitivaTaller1} \t\t {taller2} \t\t {definitivaTaller2} \t\t {taller3} \t\t {definitivaTaller3}\n")

print("Fin del programa")

'''
Notas del código:'
- Se utilizó un ciclo while para capturar los datos de los parciales y talleres, con el fin de evitar errores al ingresar los datos.
- Se utilizó un ciclo try-except para evitar errores al ingresar los datos, en caso de que se ingrese un dato diferente a un número.
- Se utilizó el operador de comparación f para poder ingresar variables en un string.
- se utiliza round para redondear los valores de las notas definitivas a dos decimales.
- se corre debug para verificar que el código funcione correctamente.
'''


