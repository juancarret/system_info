from system import *
from termcolor import cprint, colored
import os

def main():
    os.system('cls')    
    info = True
    while info:
        try:
            print()
            cprint(f'*** S Y S T E M  I N F O  v{app_version()} ***', 'green')
            print(colored(f'Station: ', 'green'), colored(f'{node()}', 'white'))
            print('-'*50)
            menu()
            quest_menu = int(input('Chose an option(0/1/2/3/4/5/6/7): '))
            if quest_menu >= 0 and quest_menu <= 7:
                if quest_menu == 0:
                    os.system('cls')
                    print()
                    cprint('*** W O R K  S T A T I O N ***', 'green')
                    print(colored(f'Station: ', 'green'), f'{node()}')
                    print('/'*60)
                    print()
                if quest_menu == 1:
                    os.system('cls')
                    print()
                    cprint('*** O S ***', 'green')
                    print(colored(f'OS: ', 'green'), f'{system()}')
                    print('/'*60)
                    print()
                elif quest_menu == 2:
                    os.system('cls')
                    print()
                    cprint(f'*** {system()} V E R S I O N ***', 'green')
                    print(colored(f'Version: ', 'green'), f'{releaseInfo()}')
                    print('/'*60)
                    print()
                elif quest_menu == 3:
                    os.system('cls')
                    print()
                    cprint('*** C P U ***', 'green')
                    print(colored(f'CPU: ', 'green'), f'{processor()}')
                    print('/'*60)
                    print()
                elif quest_menu == 4:
                    os.system('cls')
                    print()
                    cprint('*** M O T H E R  B O A R D ***', 'green')
                    print(colored(f'Mother board: ', 'green'), f'{machine()}')
                    print('/'*60)
                    print()        
                elif quest_menu == 5:
                    os.system('cls')
                    print()
                    cprint('*** A R C H I T E C T U R E ***', 'green')
                    print(colored(f'Architecture version: ', 'green'), f'{architecture()}')
                    print('/'*60)
                    print()
                elif quest_menu == 6:
                    os.system('cls')
                    print()
                    cprint('*** S U M A R Y ***', 'green')
                    print(colored(f'Station: ', 'green'), f'{nodeInfo()}')
                    print(colored(f'OS: ', 'green'), f'{systemInfo()}')
                    print(colored(f'Version: ', 'green'), f'{releaseInfo()}')
                    print(colored(f'Release: ', 'green'), f'{version()}')
                    print(colored(f'CPU: ', 'green'), f'{cpuInfo()}')
                    print(colored(f'Mother board: ', 'green'), f'{machineInfo()}')
                    print(colored(f'Architecture version: ', 'green'), f'{architecture()}')
                    print('/'*60)
                    print()
                elif quest_menu == 7:
                    quest_exit = input('Are you sure?(y/n): ')
                    if quest_exit == 'y' or quest_exit == 'Y':
                        info = False
                        os.system('cls')
                    elif quest_exit == 'n' or quest_exit == 'N':                    
                        info = True
                        os.system('cls')
                    else:
                        os.system('cls')
                        cprint('Error!, Wrong option', 'red')
            else:
                os.system('cls')
                cprint('ERROR, wrong option! Select between 0 and 7', 'red')
        except ValueError:
            os.system('cls')
            cprint('ERROR, wrong option!', 'red')
                
            
if __name__ == '__main__':
    main()
