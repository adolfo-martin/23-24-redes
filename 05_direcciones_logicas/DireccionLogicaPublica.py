
from CuatroOctetos import CuatroOctetos
from DireccionLogicaPrivada import DireccionLogicaPrivada


class DireccionLogicaPublica(CuatroOctetos):
    
    def es_formato_correcto(direccion_logica: str) -> bool:
        if not CuatroOctetos.es_formato_correcto(direccion_logica):
            return False
        
        return not DireccionLogicaPrivada.es_formato_correcto(direccion_logica)