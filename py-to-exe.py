import colorama
from colorama import Fore
import fade
import clear
import os


ascii_art = """
.----..-.  .-.  .----..-.  .-..----.
| {}  }\ \/ /   | {_   \ \/ / | {_  
| .--'  }  { to | {__  / /\ \ | {__ 
`-'     `--'    `----'`-'  `-'`----'
[!]Le fichier .py à compiler dois etre dans le dossier ou est ce tool.
[!]Veuillez lancer le setup , avant de lancer ce tool.
"""
ascii_art = fade.greenblue(ascii_art)
print(ascii_art)
py_to_exe = input(Fore.RED+'Entrée le nom du fichier .py à compiler en .exe : ')
os.system(f'pyinstaller --onefile {py_to_exe}')
clear.clear()
print(Fore.MAGENTA+"[+]Merci d'utiliser ce tool.")
input(Fore.MAGENTA+f'[+]Le fichier "{py_to_exe}" à bien etais compiler dans le dossier "dist"...')
