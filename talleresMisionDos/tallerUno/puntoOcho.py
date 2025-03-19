'''Leer un carácter y mostrar su código ASCII, por ejemplo, al ingresar @ debe mostrar 64
'''
# Definir el carácter ingresado por el usuario y la impresión del mensaje.
while True:
     try:
          caracter = input("Ingrese el carácter del cual queire saber su código ASCII: ")

          if len(caracter) == 1:
               codigoAscii = ord(caracter)
               print(f"El carácter ingresado '{caracter}',  corresponde al código ASCII: {codigoAscii}")
               break  # Sale del bucle si el usuario ingresa un carácter válido.
          else:
               print("Debe ingresar un único carácter. Intente nuevamente.")

     except ValueError:
          print("Error!: Debe ingresar un carácter válido.")

'''
Notas del código:
- Se utiliza un bucle while para que el usuario pueda ingresar un carácter válido.
- Se utiliza la función ord() para obtener el código ASCII del carácter ingresado.
- Se valida que el usuario ingrese un único carácter.
- Se utiliza la función len() para obtener la longitud del carácter ingresado.
- Se utiliza la instrucción break para salir del bucle cuando el usuario ingresa un carácter válido.
- Se utiliza la instrucción try-except para manejar errores de tipo ValueError.
'''