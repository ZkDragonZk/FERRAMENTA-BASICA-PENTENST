import platform
import codigo
import os
import sys
from colorama import Fore, init
init(autoreset=True)

if platform.system() == 'Windows':
    os.system("cls")
elif platform.system() == "Linux":
    os.system("clear")

if platform.system() == 'WIndows':
    os.system("cls")
elif platform.system() == 'Linux':
    os.system("clear")

banner = f'''{Fore.RED}
_____________ ¶¶¶¶¶¶¶¶ 
_________¶¶¶¶¶ _______¶¶¶¶¶ 
_______¶¶¶ ________________¶¶¶ 
_____¶¶¶ ____________________¶¶¶ 
____¶¶ ________________________¶¶ 
___¶ ______¶¶¶_____¶¶¶__________¶¶ 
__¶ _________¶¶______¶¶__________¶¶ 
_¶¶ __________¶¶______¶¶_________¶¶ 
_¶ ____________¶¶______¶¶___¶¶¶___¶¶ 
¶¶ _____¶¶_____¶¶______¶¶_____¶¶__¶¶ 
¶¶ ___¶¶¶______¶¶______¶¶______¶¶_¶¶ 
¶¶ __¶¶¶¶¶__________________¶¶_¶¶_¶¶ 
_¶ __¶¶__¶¶_________________¶¶____¶¶ 
_¶¶ ______¶¶______________¶¶¶____¶¶ 
__¶¶ ______¶¶____________¶¶¶_____¶¶ 
___¶¶ _______¶¶¶¶_____¶¶¶¶______¶¶ 
____¶¶ _________¶¶¶¶¶¶¶________¶¶ 
______¶¶ ____________________¶¶ 
________¶¶¶ ______________¶¶¶ 
__________ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
'''

def pergunta():
    a = input("\nEsta ferramenta foi desenvolvida apenas para fins educacionais\nNão o use para fazer coisas ruins.\n\nNão vamos assumir nenhuma responsabilidade sobre seus atos.\n\npressionar enter para Continuar...")

def home():
    try:

        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system("clear")

        print(banner)

        print('''
[1] - Pentesting Tools
[0] - Exit
    ''')

        answer = input("Seleciona uma opção:  ")
        answers = [str(x) for x in range(9)]
    
        while answer not in answers:
            print(f"{Fore.RED}Selecionar uma opção valida!!! ")
            answer = input()
        
        if answer == '1':
            return codigo.pentesting()
        elif answer == '2':
            return codigo.social()
        elif answer == '3':
            return codigo.reverse()
        elif answer == '4':
            return codigo.exploit()
        elif answer == '5':
            return codigo.forensic()
        elif answer == '6':
            return codigo.stress()
        elif answer == '7':
            return codigo.osint()
        elif answer == '8':
            return codigo.wireless()
        elif answer == '0':
            sys.exit("Good bye, i miss you (Y_Y) (´ᗣ｀) ")
    except KeyboardInterrupt:
        sys.exit("\n\nU pressed CTRL + C, Strong Hacker ლ(ಠ益ಠ)ლ")

if __name__ == '__main__':
    pergunta()
    home()