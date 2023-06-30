#pip install colorama
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(Fore.RED + 'Texto en rojo')
print(Back.GREEN + 'Fondo en verde')
print(Style.DIM + 'Texto en tono bajo')
print(Fore.YELLOW + Back.BLUE + 'Texto amarillo en fondo azul')

#pip install openpyxl
#trabajar archivos de excel

