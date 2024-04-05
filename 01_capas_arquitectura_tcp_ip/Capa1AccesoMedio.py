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
        self.__medio = medio
        self.__tecnologia = tecnologia
    

    @property
    def medio(self):
        return self.__medio
    
    @medio.setter
    def medio(self, valor: TipoMedio):
        self.__medio = valor

    @property
    def tecnologia(self):
        return self.__tecnologia

    @tecnologia.setter
    def tecnologia(self, valor: TipoTecnologia):
        self.__tecnologia = valor


    # equivalente al toString de Java
    def __repr__(self) -> str:
        return f'(Capa1AccesoMedio) medio: {self.__medio} tecnologia: {self.__tecnologia}'

    # public constructor() {}
    # None ====== void
    # self ====== this