import re

class DireccionFisica:
    """
    La clase DireccionFisica representa una dirección física, también llamada dirección MAC.
    La dirección física está formada por 6 bytes expresados en hexadecimal. Aquí vamos a seguir
    el criterio de que están separados por dos puntos (:) y escrito en mayúsculas.
    """

    def __init__(self, direccion: str) -> None:
        self.direccion = direccion

    def es_direccion_correcta(direccion: str) -> bool:
        if not type(direccion) is str:
            return False
        
        if len(direccion) != 17:
            return False
        
        
        partes = direccion.split(':')
        if len(partes) != 6:
            return False            
        
        for parte in partes:
            if len(parte) != 2:
                return False
            
        return True