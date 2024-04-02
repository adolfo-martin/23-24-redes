from enum import Enum, auto


class TipoMedio(Enum):
    ALAMBRICO = auto()
    INALAMBRICO = auto()


class TipoTecnologia(Enum):
    WIFI_4 = auto()
    WIFI_5 = auto()
    BLUETOOTH = auto()
    PAR_TRENZADO = auto()
    COAXIAL = auto()
    FIBRA_OPTICA = auto()


class Capa1AccesoMedio:
    """
    La capa de acceso al medio permite la comunicación entre dos 
    elementos adyacentes, es decir, conectados al mismo medio físico.
    """
    
    def __init__(self, medio: TipoMedio, tecnologia: TipoTecnologia) -> None:
        pass
    

    # public constructor() {}
    # None ====== void
    # self ====== this