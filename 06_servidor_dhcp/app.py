import os
from Equipo import Equipo
from ServidorDhcp import ServidorDhcp


os.system('cls')

servidor = ServidorDhcp('00:11:22:33:44:55', 'servidor-dhcp')
print(servidor)
servidor.establecer_parametros_red_estaticos('192.168.1.1', '255.255.255.0', '192.168.1.1', '8.8.8.8')
servidor.establecer_parametros_dhcp('192.168.1.101', '192.168.1.254')

equipo1 = Equipo("AA:AA:AA:AA:AA:01", "ordenador-01")
equipo1.establecer_parametros_red_estaticos('192.168.1.11', '255.255.255.0', '192.168.1.1', '8.8.8.8')
print(equipo1)

equipo2 = Equipo("AA:AA:AA:AA:AA:02", "ordenador-02")
print(equipo2)