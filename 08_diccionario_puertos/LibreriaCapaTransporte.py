from enum import Enum


type NumeroPuerto = int
type Aplicacion = str


class TipoServicio(Enum):
    UDP = 'udp'
    TCP = 'tcp'


class PuertoRed:

    def __init__(self, numero_puerto: NumeroPuerto, tipo_servicio: TipoServicio) -> None:
        self.numero_puerto = numero_puerto
        self.tipo_servicio = tipo_servicio