from Equipo import Equipo
from ProtocoloIp import DireccionIp, DireccionMac


class ServidorDhcp(Equipo):
    
    def __init__(self, direccion_mac: DireccionMac, nombre: str) -> None:
        super().__init__(direccion_mac, nombre)
        self.direccion_ip_inicio = None
        self.direccion_ip_fin = None
        self.direcciones_asignadas: dict[DireccionMac, DireccionIp] = {}


    def establecer_parametros_dhcp(self, 
        direccion_ip_inicio: DireccionIp,
        direccion_ip_fin: DireccionIp,
    ):
        """
        La máscara de red será la que ya tiene establecida.
        La puerda de enlace será la que ya tiene establecida.
        El servidor DNS será el que ya tiene establecido.
        """
        self.direccion_ip_inicio = direccion_ip_inicio
        self.direccion_ip_fin = direccion_ip_fin


    def asignar_direccion_ip_a_equipo(self, direccion_mac: DireccionMac) -> DireccionIp:
        numero_inicio = int(self.direccion_ip_inicio.split('.')[3])
        numero_fin = int(self.direccion_ip_fin.split('.')[3])