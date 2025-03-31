import os
import colorama
import re
from colorama import Fore
from validaciones import validarNombre, validarNumero, validarOpcion
from tabulate import tabulate

colorama.init(autoreset=True)

# Se defiene las constantes

smlv                = 1423500
auxTransporte       = 200000
porcentajeSalud     = 0.04
porcentajePension   = 0.04
salarioMaximo       = 8000000
uvt                 = 49799

cedulasRegistradas = set()

def validarCedula(mensaje):                                          # Se valida que la cedula del usuario ingresado no este repetida y sea un numero valido.
     while True:
          cedula = validarNumero(mensaje, 1000000, 9999999999)         # se define el rango de la cedula a validar.
          if cedula in cedulasRegistradas:
               print(Fore.RED + "⚠️ Usuario ya se encuentra registrado, por favor ingrese otro.")
          else:
               cedulasRegistradas.add(cedula)
               return cedula

def validarCorreo(mensaje):                                           # Se valida que el correo ingresado este en un formato correcto.
     while True:
          correo = input(Fore.YELLOW + mensaje).strip()
          if re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", correo):
               return correo
          else:
               print(Fore.RED + "⚠️ El correo no es valido, intente nuevamente.")

def calcularAuxilioTransporte(salario):                             # Se valida si el empleado tiene derecho al auxilio de trnasporte.
     return auxTransporte if salario < (2 * smlv) else 0

def calcularDescuentos(salarioDevengado):                           # Se calculan los decuentos de salid y pension
     descuentoSalud = salarioDevengado * porcentajeSalud
     descuentoPension = salarioDevengado * porcentajePension
     return descuentoSalud, descuentoPension

def calcularRetencionFuente(salarioDevengado, descuentoSalud, descuentoPension):     # se calcula la retencion en la fuente, aplicanto tabla de retemncion. 
     baseRetencion = (salarioDevengado - (descuentoSalud + descuentoPension)) * 0.75 # de acuerdo a la norma, el 25% es libre de retencion.
     uvtBase = baseRetencion / uvt

     uvtBase = 95

     if uvtBase     <=   0:
          retencion =    0
     elif uvtBase   <=   95:
          retencion =    (uvtBase * uvt) * 0.19
     elif uvtBase   <=   150:
          retencion =    (uvtBase * uvt) *0.28
     else:
          retencion =    print (" 0 'El rango no cuenta con una tasa definida.'")
     
     return retencion

def calcularSalarioNeto(salario, diasTrabajados):                    # Se realizan los calculos para realizar el pago neto
     salarioDevengado = (salario / 30) * diasTrabajados
     auxilio = calcularAuxilioTransporte(salario)
     descuentoSalud, descuentoPension = calcularDescuentos(salarioDevengado)
     descuentoRetencion = calcularRetencionFuente(salarioDevengado, descuentoSalud, descuentoPension)

     salarioNeto = salarioDevengado + auxilio - (descuentoSalud + descuentoPension + descuentoRetencion)

     return salarioDevengado, salarioNeto, auxilio, descuentoSalud, descuentoPension, descuentoRetencion

def mostrarResultados(empleado):

     print("\n" + Fore.CYAN + "=== RESULTADOS DEL CÁLCULO ===")

     tabla = [
          ["Empleado", empleado["nombre"]],
          ["Cédula", empleado["cedula"]],
          ["Celular", empleado["celular"]],
          ["Dirección", empleado["direccion"]],
          ["Ciudad", empleado["ciudad"]],
          ["Correo", empleado["correo"]],
          ["Cargo", empleado["cargo"]],
          ["Salario Devengado", f"${empleado['salarioDevengado']:,.2f}"],
          ["Auxilio de Transporte", f"${empleado['auxilio']:,.2f}"],
          ["Descuento Salud (4%)", f"-${empleado['descuentoSalud']:,.2f}"],
          ["Descuento Pensión (4%)", f"-${empleado['descuentoPension']:,.2f}"],
          ["Retención en la Fuente", f"-${empleado['descuentoRetencion']:,.2f}"],
          ["Salario Neto a Pagar", f"${empleado['salarioNeto']:,.2f}"]
          ]

     print(tabulate(tabla, headers=["Concepto", "Valor"], tablefmt="fancy_grid"))
     print("\n" + Fore.CYAN + "==============================\n")

def main():                                                           # Con esta funcion se ejecutara el programa.

     while True:
          os.system('cls' if os.name == 'nt' else 'clear')            # limpiamos pantalla con esta linea.
          print(Fore.BLUE + "🧾 Calculo de salario para un empleado 2025 ")

# En esta seccion se hace la entrada de datos
          nombre = validarNombre("👤 Ingresa el nombre del empleado: ")
          cedula = validarCedula("🖋️ Ingresa la cédula de ciudadanía: ")
          celular = validarNumero("📲 Ingresa el número de celular: ", 3000000000, 3999999999)
          direccion = input(Fore.YELLOW + "🏢 Ingresa la dirección: ").strip()
          ciudad = input(Fore.YELLOW + "🗾 Ingresa la ciudad: ").strip()
          correo = validarCorreo("⌨️ Ingresa el correo electrónico: ")
          cargo = input(Fore.YELLOW + "📑 Ingresa el cargo: ").strip()
          salario = validarNumero("💵 Ingresa el salario básico mensual: ", 0, salarioMaximo)
          diasTrabajados = validarNumero("🗓️ Ingresa los días trabajados en el mes (1-30): ", 1, 30)

# En esta seccion Calculamos el salartio 
          salarioDevengado, salarioNeto, auxilio, descuentoSalud, descuentoPension, descuentoRetencion = calcularSalarioNeto(salario, diasTrabajados)

# En esta seccion, se guardan los datos cacturados en el diccionario.
          empleado = {
               "nombre": nombre, 
               "cedula": cedula, 
               "celular": celular,
               "direccion": direccion, 
               "ciudad": ciudad, 
               "correo": correo, 
               "cargo": cargo, 
               "salarioDevengado": salarioDevengado, 
               "auxilio": auxilio, 
               "descuentoSalud": descuentoSalud, 
               "descuentoPension": descuentoPension, 
               "descuentoRetencion": descuentoRetencion, 
               "salarioNeto": salarioNeto
               }

          mostrarResultados(empleado)                                           # Con esta linea, mostramos los resultados

          if not validarOpcion("¿Deseas calcular otro salario? (Sí/No): "):     # en esta linea se pregunta si el usuario desea calcular otro salario
               print(Fore.GREEN + "👋 Gracias por usar el sistema. ¡Hasta pronto!")
               break

if __name__ == "__main__":
     main()