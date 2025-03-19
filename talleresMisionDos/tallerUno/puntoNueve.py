'''
Leer un número de 1 al 255 y mostrar que carácter corresponde a su código ASCII, por ejemplo 64 muestra @.
'''
# Declarar la variable que almacenará el número ingresado por el usuario.

num = int(input("Ingrese un número entre 1 y 255: "))

# Se realizan los arreglos para verificar que el número ingresado se encuentre en el rango permitido.

while True:
     try:
          if 1 <= num <= 255:
               codeascii = chr(num)
               print(f"El numero {num} corresponde al código ASCII: {codeascii}")
               break
          else:
               print("El numero ingresado se encuentra fuera del rango permitido (entre 1 y 255), Intente nuevamente.")
     except ValueError:
          print("Error, Debe ingresar un número.")