'''
Leer dos números y hallar: la sumatoria, su diferencia, su producto, su cociente y su residuo, NO usar funciones.
'''
# definir variables
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

if num2 != 0:
     division = num1 / num2
     residuo = num1 % num2
else:
     division = "No se puede dividir por cero"
     residuo = "No se puede realizar el calculo al dividir entre cero"

# mostrar resultados
print("El resultado de las operaciones es:\n\n",)
print(f"La suma de los números es: {suma}\n")
print(f"La resta de los números es: {resta}\n")
print(f"La multiplicacion de los números es: {multiplicacion}\n")
print(f"La división de los números es: {division}\n")
print(f"El residuo de los números es: {residuo}\n")

'''
Notas del código:
- Se utilizó la función float para poder ingresar números decimales, ya que no indica que tipo de numero se debe ingresar.
- Se utilizó un if para evitar la división entre cero, ya que no es posible realizarla.
- Se utilizó \n para hacer un salto de línea en el print.
- Se corre debug para verificar que el código funcione correctamente.
'''