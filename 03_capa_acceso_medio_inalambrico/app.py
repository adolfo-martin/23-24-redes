import os

from OrdenadorPortatil import OrdenadorPortatil
from PuntoAcceso import PuntoAcceso, PuntoAccesoError
from TelefonoInteligente import TelefonoInteligente

os.system('cls')

punto_acceso = PuntoAcceso('wifi_adolfo', 'Hola1234')

portatil1 = OrdenadorPortatil('Asus', 'AA:AA:AA:AA:AA:01')
portatil2 = OrdenadorPortatil('Lenovo', 'AA:AA:AA:AA:AA:02')
movil1 = TelefonoInteligente('Xiaomi', 'AA:AA:AA:AA:AA:03')
tableta1 = TelefonoInteligente('Samsung', 'AA:AA:AA:AA:AA:04')

print(portatil1)
print(portatil2)
print(movil1)
print(tableta1)

print(punto_acceso.equipos_conectados)
try:
    portatil1.conectar_a_wifi(punto_acceso, 'Hola1234')
except PuntoAccesoError as error:
    print(error)

print(punto_acceso.equipos_conectados)
try:
    portatil2.conectar_a_wifi(punto_acceso, 'Hola5678')
except PuntoAccesoError as error:
    print(error)

print(punto_acceso.equipos_conectados)