from ProtocoloIp import DireccionIp, DireccionMac, MascaraRed


class Equipo:

    def __init__(self, nombre: str, direccion_mac: DireccionMac) -> None:
        self.nombre = nombre
        self.direccion_mac = direccion_mac
        self.direccion_ip: DireccionIp = None
        self.mascara_red: MascaraRed = None
        self.puerta_enlace: DireccionIp = None
        self.servidor_dns: DireccionIp = None


    def establecer_parametros_ip(self, 
        direccion_ip: DireccionIp, 
        mascara_red: MascaraRed, 
        puerta_enlace: DireccionIp,
        servidor_dns: DireccionIp
    ) :
        self.direccion_ip = direccion_ip
        self.mascara_red = mascara_red
        self.puerta_enlace = puerta_enlace
        self.servidor_dns = servidor_dns
