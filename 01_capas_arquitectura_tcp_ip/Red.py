from Capa1AccesoMedio import Capa1AccesoMedio

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