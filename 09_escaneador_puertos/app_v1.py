from TerminalColors import TerminalColors

import socket

LOCALHOST = '127.0.0.1'

print('Escaneando puertos de servidor abiertos.')

for puerto in range(440, 450):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f'{TerminalColors.BLACK_WHITE}Probando puerto {puerto}', end=': ')
        try:
            s.connect((LOCALHOST, puerto))
            print(f'{TerminalColors.BLACK_RED}ABIERTO')
        except ConnectionRefusedError as error:
            print(f'{TerminalColors.BLACK_GREEN}CERRADO')
        finally:
            print(f'{TerminalColors.BLACK_WHITE}', end='')
