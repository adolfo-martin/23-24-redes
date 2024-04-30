from Equipo import Equipo
from ProtocoloIp import DireccionIp, DireccionMac, MascaraRed


class ServidorDhcp(Equipo):

    def __init__(self, nombre: str, direccion_mac: DireccionMac) -> None:
        super().__init__(nombre, direccion_mac)
        self.direccion_inicial: DireccionIp = None
        self.direccion_final: DireccionIp = None
        self.direcciones_asignadas: dict[DireccionMac, DireccionIp] = {}
        self.direcciones_reservadas: dict[DireccionMac, DireccionIp] = {}


    def establecer_parametros_dhcp(self, direccion_inicial: DireccionIp, direccion_final: DireccionIp) -> None:
        self.direccion_inicial = direccion_inicial
        self.direccion_final = direccion_final


    def solicitar_parametros_dhcp_para_equipo(self, direccion_mac: DireccionMac) -> tuple | None:
        ip = self.direcciones_asignadas.get(direccion_mac)
        if ip is not None:
            return (ip, self.mascara_red, self.puerta_enlace, self.servidor_dns)

        if self.esta_mac_en_direcciones_reservadas(direccion_mac):
            ip = self.direcciones_reservadas[direccion_mac]
            self.direcciones_asignadas[direccion_mac] = ip
            return (ip, self.mascara_red, self.puerta_enlace, self.servidor_dns)

        partes_direccion = self.direccion_inicial.split('.')
        prefijo_direcciones = f'{partes_direccion[0]}.{partes_direccion[1]}.{partes_direccion[2]}'
        numero_inicial = int(partes_direccion[3])
        numero_final= int(self.direccion_final.split('.')[3])
        direcciones_ip_asignadas = list(self.direcciones_asignadas.values())
        direcciones_ip_reservadas = list(self.direcciones_reservadas.values())
        for numero in range(numero_inicial, numero_final + 1):
            ip = f'{prefijo_direcciones}.{numero}'
            if ip in direcciones_ip_asignadas:
                continue

            if ip in direcciones_ip_reservadas:
                continue

            self.direcciones_asignadas[direccion_mac] = ip
            return (ip, self.mascara_red, self.puerta_enlace, self.servidor_dns)
        
        return None
    

    def esta_mac_en_direcciones_asignadas(self, direccion_mac: DireccionMac) -> bool:
        return direccion_mac in list(self.direcciones_asignadas.keys())
    

    def esta_ip_en_direcciones_asignadas(self, direccion_ip: DireccionIp) -> bool:
        return direccion_ip in list(self.direcciones_asignadas.values())


    def reservar_direccion(self, direccion_mac: DireccionMac, direccion_ip: DireccionIp) -> None:
        if self.esta_ip_en_direcciones_reservadas(direccion_ip):
            raise DhcpDireccionReservadaError()

        if self.esta_mac_en_direcciones_reservadas(direccion_mac):
            raise DhcpDireccionReservadaError()
        
        if self.esta_ip_en_direcciones_asignadas(direccion_ip):
            raise DhcpDireccionReservadaError()
        
        if self.esta_mac_en_direcciones_asignadas(direccion_mac):
            raise DhcpDireccionReservadaError()

        self.direcciones_reservadas[direccion_mac] = direccion_ip


    def esta_mac_en_direcciones_reservadas(self, direccion_mac: DireccionMac) -> bool:
        return direccion_mac in list(self.direcciones_reservadas.keys())
    

    def esta_ip_en_direcciones_reservadas(self, direccion_ip: DireccionIp) -> bool:
        return direccion_ip in list(self.direcciones_reservadas.values())
            



class DhcpDireccionReservadaError(Exception): ...
            