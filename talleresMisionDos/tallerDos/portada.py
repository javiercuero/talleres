from colorama import Fore, Style, init
from tabulate import tabulate


datos = [
     [Fore.CYAN + "Talento Tech" + Style.RESET_ALL, ""],
     [Fore.YELLOW + "Proyecto:" + Style.RESET_ALL, "Taller 2"],
     [Fore.MAGENTA + "Campista:" + Style.RESET_ALL, "Javier Alexander Cuero Castillo"],
]

print(tabulate(datos, tablefmt="grid", stralign="center"))