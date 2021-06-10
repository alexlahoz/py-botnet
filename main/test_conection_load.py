import time
import os
import sys

def connect_with_server():
        for i in range(1):
            v=i+1
            os.system('clear')

            sys.stdout.write('\033[34m[*~*]\033[0m Conectando con el servidor \033[34m[*~*]\033')
            sys.stdout.flush()
            time.sleep(0.3)
            os.system('clear')

            sys.stdout.write('\033[34m[*\*]\033[0m Conectando con el servidor \033[34m[*\*]\033')
            sys.stdout.flush()
            time.sleep(0.3)
            os.system('clear')

            sys.stdout.write('\033[34m[*|*]\033[0m Conectando con el servidor \033[34m[*|*]\033')
            sys.stdout.flush()
            time.sleep(0.3)
            os.system('clear')

            sys.stdout.write('\033[34m[*/*]\033[0m Conectando con el servidor \033[34m[*/*]\033')
            sys.stdout.flush()
            time.sleep(0.3)
            os.system('clear')

            sys.stdout.write('\033[34m[*~*]\033[0m Conectando con el servidor \033[34m[*~*]\033')
            sys.stdout.flush()
            time.sleep(0.3)
            os.system('clear')

            sys.stdout.write('\033[34m[*\*]\033[0m Conectando con el servidor \033[34m[*\*]\033')
            sys.stdout.flush()
            time.sleep(0.3)
            os.system('clear')

            sys.stdout.write('\033[34m[*|*]\033[0m Conectando con el servidor \033[34m[*|*]\033')
            sys.stdout.flush()
            time.sleep(0.3)
            os.system('clear')

            sys.stdout.write('\033[34m[*/*]\33[0m Conectando con el servidor \033[34m[*/*]\33')
            sys.stdout.flush()
            time.sleep(0.3)
        
        os.system('clear')
        print("\033[34m[INFO]\033[0m Conectado con exito al servidor ")
        time.sleep(2)

        host = '192.168.1.129'

        command = input('\033[0m \033[31m' + host + '\033[35m /\033[0m \033[36mhome\033[0m\033[0m > \033[33m')
        sys.stdout.write(command)

connect_with_server()