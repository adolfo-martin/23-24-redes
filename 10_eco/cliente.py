import socket


EQUIPO = '192.168.0.100'
PUERTO = 8080

print(f'Servidor escuchando en el puerto {PUERTO}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((EQUIPO, PUERTO))
    s.listen()
    conexion, direccion_remota = s.accept()
    print('Alguien se ha conectado.')