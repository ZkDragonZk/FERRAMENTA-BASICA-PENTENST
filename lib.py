import returnn
import platform
import webbrowser
import sys
import os
from colorama import Fore, init
init(autoreset=True)

def pentesting():

    try:
        print('''
[1] - Nmap
[2] - Nikto
[0] - menu inicial
        ''')

        answer = input("Seleciona uma opção: ")
        answers = [str(x) for x in range(12)]

        while answer not in answers:
            print(f"{Fore.RED}Seleciona uma opção valida")
            answer = input()
####################################################################################################################
        if answer == '1': # NMAP
            if platform.system() == 'Windows':
                print(f"Sua Plataforma é: {platform.system()}, você deve instalar no site:\nLink: https://nmap.org/download.html")

                answer = input("Voltar ao Menu: [S/N] ") 
                while answer.lower() not in ['S', 'N', '']:
                    print("Seleciona uma opção:")
                    answer = input()
                if answer.lower() == 'S':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'N':
                    sys.exit("Bye te vejo em breve!")
            elif platform.system() == 'Linux':
                print(os.system("sudo apt install nmap -y"))
                os.system("clear")
                print(f"{Fore.BLUE}[!] NMAP instalado com sucesso!")
                print('\n')
                answer = input("Voltar ao Menu: [S/N] ") 
                while answer.lower() not in ['S', 'N', '']:
                    print("Seleciona uma opção:")
                    answer = input()
                if answer.lower() == 'S':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'N':
                    sys.exit("Bye te vejo em breve!")
########################################################################################################################################################################################################################################
        elif answer == '2': #NIKTO
            if platform.system() == 'Windows':
                print(f"Sua plataforma é: {platform.system()}, você tem que baixar no site:\n https://gitlab.com/kalilinux/packages/nikto")

                answer = input("Voltar ao menu: [S/N] ")
                while answer.lower() not in  ['S', 'N', '']:
                    print("Seleciona uma opção: ")
                    answer = input()
                if answer.lower() == 'S':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'N':
                    sys.exit("Bye te vejo em breve!")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/nikto.git tools/nikto"))
                os.system("clear")
                print(f"{Fore.RED}[!] nikto baixado com sucesso abra a pasta tools.")
                print("\n")
                answer = input("Voltar ao menu: [S/N]  ")
                while answer.lower() not in ['S', 'N', '']:
                    print("seleciona uma opção: ")
                    answer = input()
                if answer.lower() == 'S':
                    return returnn.home()
                elif bool(answer) == False:
                    return returnn.home()
                elif answer.lower() == 'N':
                    sys.exit("Bye te vejo em breve!")
   
    except KeyboardInterrupt:
        sys.exit("\n\nU pressed CTRL + C (ノಠ益ಠ)ノ彡┻━┻ ")