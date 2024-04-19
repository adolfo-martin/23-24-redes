
from DireccionLogica import DireccionLogica
from DireccionLogicaPrivada import DireccionLogicaPrivada


class DireccionLogicaPublica(DireccionLogica):
    
    def es_direccion_correcta(direccion_logica: str) -> bool:
        if not DireccionLogica.es_direccion_correcta(direccion_logica):
            return False
        
        return not DireccionLogicaPrivada.es_direccion_correcta(direccion_logica)