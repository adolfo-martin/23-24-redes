from ProtocoloIp import DireccionIp, DireccionMac, MascaraRed


class Equipo:

    def __init__(self, direccion_mac: DireccionMac, nombre: str) -> None:
        self.nombre = nombre
        self.direccion_mac = direccion_mac

        self.direccion_ip: DireccionIp = None
        self.mascara_red: MascaraRed = None
        self.puerta_enlace: DireccionIp = None
        self.servidor_dns: DireccionIp = None


    def establecer_parametros_red_estaticos(self, 
        direccion_ip: DireccionIp, 
        mascara_red: MascaraRed, 
        puerta_enlace: DireccionIp, 
        servidor_dns: DireccionIp
    ):
        """
        Este método permite establecer manualmente cuatro parámetros de red, 
        y así no hay que emplear un servidor DHCP.

        :param DireccionIp direccion_ip: La dirección IP del equipo.
        :param MascaraRed mascara_red: La máscara de red.
        :param DireccionIp puerta_enlace: La puerta de enlace es el equipo que une la red local con el resto de redes.
        :param DireccionIp servidor_dns: El servidor DNS transforma un nombre de equipo en su correspondiente direccion IP.
        """
        self.direccion_ip = direccion_ip
        self.mascara_red = mascara_red
        self.puerta_enlace = puerta_enlace
        self.servidor_dns = servidor_dns


    def __repr__(self) -> str:
        return f'[{self.nombre}] {self.direccion_mac} - {self.direccion_ip}'