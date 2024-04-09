from DireccionFisica import DireccionFisica
from enum import Enum, auto


class Tecnologia(Enum):
    PAR_TRENZADO_100 = auto()
    PAR_TRENZADO_1000 = auto()
    FIBRA_OPTICA_100 = auto()
    FIBRA_OPTICA_1000 = auto()
    WIFI_300 = auto()
    WIFI_600 = auto()


class PuertoRed:

    def __init__(self, direccion_fisica: DireccionFisica, tecnologia: Tecnologia):
        self.__direccion_fisica = direccion_fisica
        self.__tecnologia = tecnologia


    @property
    def tecnologia(self) -> Tecnologia:
        return self.__tecnologia