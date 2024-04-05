from Capa1AccesoMedio import Capa1AccesoMedio
from Capa2Interred import Capa2Interred
from Capa3Transporte import Capa3Transporte
from Capa4Aplicacion import Capa4Aplicacion

class Red:
    """
    Esta clase representa una red construida empleando la arquitectura TCP/IP.
    """

    def __init__(self, 
        capaAccesoMedio: Capa1AccesoMedio, 
        capaInterred: Capa2Interred, 
        capaTransporte: Capa3Transporte, 
        capaAplicacion: Capa4Aplicacion
    ) -> None:
        self.capaAccesoMedio = capaAccesoMedio
        self.capaInterred = capaInterred
        self.capaTransporte = capaTransporte
        self.capaAplicacion = capaAplicacion