from TerminalColors import TerminalColors

import socket

LOCALHOST = '127.0.0.1'

def main():
    print('Escaneando puertos de servidor abiertos.')
    puertos = obtener_puertos_abiertos(puerto_inicial=440, puerto_final=450)
    mostrar_puertos_abiertos(puertos)


def obtener_puertos_abiertos(
    direccion_ip: str = '127.0.0.1', 
    puerto_inicial: int = 1, 
    puerto_final: int = 65535
) -> list[int]:
    puertos_abiertos: list[int] = []
    for puerto in range(puerto_inicial, puerto_final):
        if esta_puerto_abierto(direccion_ip, puerto):
            puertos_abiertos.append(puerto)

    return puertos_abiertos


def mostrar_puertos_abiertos(puertos: list[int]) -> None:
    for puerto in puertos:
        print(f'Puerto {puerto} {TerminalColors.BLACK_RED}ABIERTO{TerminalColors.BLACK_WHITE}')


def esta_puerto_abierto(direccion_ip: str, puerto: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((direccion_ip, puerto))
            return True
        except ConnectionRefusedError as error:
            return False 


if __name__ == '__main__':
    main()