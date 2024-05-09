import socket
from threading import Thread
from config import IP_SERVIDOR, PUERTO



class Cliente:
    
    def conectar_a_servidor(self, ip_servidor, puerto_servidor):
        print(f'Intentando conectar al servidor y puerto ({ip_servidor}, {puerto_servidor})')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_cliente:
            socket_cliente.connect((ip_servidor, puerto_servidor))

            hilo_recibir = Thread(target=self.__recibir, args=(socket_cliente,))
            hilo_enviar = Thread(target=self.__enviar, args=(socket_cliente,))
            hilo_recibir.start()
            hilo_enviar.start()
            hilo_recibir.join()
            hilo_enviar.join()


    def __enviar(self, socket_cliente):
        while True:
            print('\033[0;32;40m')
            mensaje = input('>>>')
            socket_cliente.send(mensaje.encode())
    

    def __recibir(self, socket_cliente):
        while True:
            mensaje = socket_cliente.recv(1024)
            print('\033[0;34;40m', f'<<<{mensaje.decode()}')


def main():
    cliente = Cliente()
    cliente.conectar_a_servidor(IP_SERVIDOR, PUERTO)


if __name__ == '__main__':
    main()