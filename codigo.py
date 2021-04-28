import menu
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
[3] - UnicornScan
[4] - Wpscan
[5] - Wireshark
[0] - menu inicial
        ''')

        answer = input("Seleciona uma opção: ")
        answers = [str(x) for x in range(12)]

        while answer not in answers:
            print(f"{Fore.RED}Seleciona uma opção valida")
            answer = input()
####################################################################################################################
        if answer == '1':
            if platform.system() == 'Windows':
                print(f"Sua Plataforma é: {platform.system()}, você deve instalar no site:\nLink: https://nmap.org/download.html")

                answer = input("Voltar ao Menu: [S/N] ") 
                while answer.lower() not in ['S', 'N', '']:
                    print("Seleciona uma valida:")
                    answer = input()
                if answer.lower() == 'S':
                    return menu.home()
                elif bool(answer) == False:
                    return menu.home()
                elif answer.lower() == 'N':
                    sys.exit("te vejo em breve!")
            elif platform.system() == 'Linux':
                print(os.system("sudo apt install nmap -y"))
                os.system("clear")
                print(f"{Fore.BLUE}[!] NMAP instalado com sucesso!")
                print('\n')
                answer = input("Voltar ao Menu: [S/N] ") 
                while answer.lower() not in ['S', 'N', '']:
                    print("Seleciona uma valida:")
                    answer = input()
                if answer.lower() == 'S':
                    return menu.home()
                elif bool(answer) == False:
                    return menu.home()
                elif answer.lower() == 'N':
                    sys.exit(" te vejo em breve!")
########################################################################################################################################################################################################################################
        elif answer == '2':
            if platform.system() == 'Windows':
                print(f"Sua plataforma é: {platform.system()}, você tem que baixar no site:\n https://gitlab.com/kalilinux/packages/nikto")

                answer = input("Voltar ao menu: [Y/n] ")
                while answer.lower() not in  ['y', 'n', '']:
                    print("Seleciona uma valida: ")
                    answer = input()
                if answer.lower() == 'y':
                    return menu.home()
                elif bool(answer) == False:
                    return menu.home()
                elif answer.lower() == 'n':
                    sys.exit("te vejo em breve!")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/nikto.git tools/nikto"))
                os.system("clear")
                print(f"{Fore.RED}[!] nikto baixado com sucesso abra a pasta tools.")
                print("\n")
                answer = input("Voltar ao menu: [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("seleciona uma valida: ")
                    answer = input()
                if answer.lower() == 'y':
                    return menu.home()
                elif bool(answer) == False:
                    return menu.home()
                elif answer.lower() == 'n':
                    sys.exit("te vejo em breve!")
####################################################################################################################
        elif answer == '3':
            if platform.system() == 'Windows':
                print(f"Sua plataforma é: {platform.system()}, você tem que baixar no site:\n https://gitlab.com/kalilinux/packages/unicornscan")

                answer = input("Voltar ao menu: [Y/n] ")
                while answer.lower() not in  ['y', 'n', '']:
                    print("Seleciona uma valida: ")
                    answer = input()
                if answer.lower() == 'y':
                    return menu.home()
                elif bool(answer) == False:
                    return menu.home()
                elif answer.lower() == 'n':
                    sys.exit("te vejo em breve!")
            elif platform.system() == 'Lhttps://gitlab.com/kalilinux/packages/unicornscaninux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/unicornscan.git tools/unicornscan"))
                os.system("clear")
                print(f"{Fore.RED}[!] unicornscan baixado com sucesso abra a pasta tools.")
                print("\n")
                answer = input("Voltar ao menu: [Y/n]  ")
                while answer.lower() not in ['y', 'N', '']:
                    print("seleciona uma valida: ")
                    answer = input()
                if answer.lower() == 'y':
                    return menu.home()
                elif bool(answer) == False:
                    return menu.home()
                elif answer.lower() == 'n':
                    sys.exit("te vejo em breve!")
####################################################################################################################
        elif answer == '4':
            if platform.system() == 'Windows':
                print(f"Sua plataforma é: {platform.system()}, você tem que baixar no site:\n https://github.com/wpscanteam/wpscan")

                answer = input("Voltar ao menu: [Y/n] ")
                while answer.lower() not in  ['y', 'n', '']:
                    print("Seleciona uma valida: ")
                    answer = input()
                if answer.lower() == 'y':
                    return menu.home()
                elif bool(answer) == False:
                    return menu.home()
                elif answer.lower() == 'n':
                    sys.exit("te vejo em breve!")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://github.com/wpscanteam/wpscan tools/wpscan"))
                os.system("clear")
                print(f"{Fore.RED}[!] wpscan baixado com sucesso abra a pasta tools.")
                print("\n")
                answer = input("Voltar ao menu: [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("seleciona uma valida: ")
                    answer = input()
                if answer.lower() == 'y':
                    return menu.home()
                elif bool(answer) == False:
                    return menu.home()
                elif answer.lower() == 'n':
                    sys.exit("te vejo em breve!")  
####################################################################################################################
        elif answer == '5':
            if platform.system() == 'Windows':
                print(f"Sua plataforma é: {platform.system()}, você tem que baixar no site:\n  https://gitlab.com/kalilinux/packages/wireshark")

                answer = input("Voltar ao menu: [Y/n] ")
                while answer.lower() not in  ['y', 'n', '']:
                    print("Seleciona uma valida: ")
                    answer = input()
                if answer.lower() == 'y':
                    return menu.home()
                elif bool(answer) == False:
                    return menu.home()
                elif answer.lower() == 'n':
                    sys.exit("te vejo em breve!")
            elif platform.system() == 'Linux':
                print(os.system("git clone https://gitlab.com/kalilinux/packages/wireshark.git tools/wireshark"))
                os.system("clear")
                print(f"{Fore.RED}[!] wireshark baixado com sucesso abra a pasta tools.")
                print("\n")
                answer = input("Voltar ao menu: [Y/n]  ")
                while answer.lower() not in ['y', 'n', '']:
                    print("seleciona uma valida: ")
                    answer = input()
                if answer.lower() == 'y':
                    return menu.home()
                elif bool(answer) == False:
                    return menu.home()
                elif answer.lower() == 'n':
                    sys.exit("te vejo em breve!")  
####################################################################################################################

    except KeyboardInterrupt:
        sys.exit("\n\nU pressed CTRL + C (ノಠ益ಠ)ノ彡┻━┻ ")