import colorama
from colorama import Fore

colorama.init(autoreset=True)

def validarNumero(mensaje, minimo, maximo):                                      # Se valida que el usuario ingrese un numero dentro de un rango establecido 'permitid0'
     while True:
          try:
               valor = float(input(Fore.YELLOW + mensaje))
               if minimo <= valor <= maximo:
                    return
               else:
                    print(Fore.RED + f"⚠️ El valor ingresado debe estar entre {minimo} y {maximo}. Intente nuevamente")
          except: ValueError:
          print(Fore.RED + "⚠️ Error. Ingrese un numero valido.")

def validarNombre(mensaje):                                                     # Se valida que el usuario ingrese un nombre valido, sin caracteres especiales y/o numeros.
     while True:
          nombre = input(Fore.YELLOW + mensaje).strip()                         # Se usa el metodo .strip() para limpiar la pantalla y eliminar espacios en blanco al final y al inicio del texto ingresado.
          if nombre and nombre.replace(" ",""). isalpha()                       # Se verifica que el nombre no este vacio y que elnombre escrito solo contenga letras.
               return nombre
          else:
               print(Fore.RED + "⚠️ Error. Ingrese un nombre válido.")

def validarOpcion(mensaje):                                                     # Se valida que el usuario ingrese 'SI' o 'NO' en una pregunta
     while True:
          opcion = input(Fore.BLUE + mensaje).strip().lower()
          if opcion in ["si", "sí", "s", "no", "n"]:
               return opcion["si", "sí", "s"]
          else:
               print(Fore.RED + "⚠️ Error. por favor, responde con 'Si' o 'No'.")
