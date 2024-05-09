import socket
from threading import Thread
from config import IP_SERVIDOR, PUERTO


class Servidor:

    def __init__(self, direccion_ip: str, puerto: int) -> None:
        self.direccion_ip = direccion_ip
        self.puerto = puerto


    def esperar_a_cliente(self):
        print(f'Servidor escuchando en el puerto {self.puerto} de la dirección {self.direccion_ip}')
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_servidor:
            socket_servidor.bind((self.direccion_ip, self.puerto))
            socket_servidor.listen()
            socket_cliente, direccion_remota = socket_servidor.accept()
            print(f'Cliente conectado desde el equipo {direccion_remota}')

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
    servidor = Servidor(IP_SERVIDOR, PUERTO)
    servidor.esperar_a_cliente()


if __name__ == '__main__':
    main()