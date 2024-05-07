import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.0.100', 8080))
    while True:
        mensaje = input('Mensaje a enviar: ')
        s.sendall(mensaje)