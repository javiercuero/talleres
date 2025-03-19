'''
Leer un número de 1 al 255 y mostrar que carácter corresponde a su código ASCII, por ejemplo 64 muestra @.
'''
# Declarar la variable que almacenará el número ingresado por el usuario. y la impresion del mensaje.

while True:
     try:
          num = int(input("Ingrese un número entre 1 y 255: "))

          if 1 <= num <= 255:
               codeascii = chr(num)
               print(f"El número {num} corresponde al código ASCII: {codeascii}")
               break  # Se sale del bucle si el usuario ingresa un número válido
          else:
               print("El número ingresado está fuera del rango permitido (entre 1 y 255). Intente nuevamente.")

     except ValueError:
          print("Error!: Debe ingresar un número válido.")

'''
Notas del código:
- Se utiliza un bucle while para solicitar al usuario que ingrese un número entre 1 y 255.
- Se utiliza un bloque try-except para manejar errores en caso de que el usuario ingrese un valor no numérico.
- Se verifica si el número ingresado está dentro del rango permitido (entre 1 y 255).
'''
