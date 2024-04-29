from CuatroOctetos import CuatroOctetos


class MascaraRed(CuatroOctetos):
    
    def __init__(self, mascara: str) -> None:
        if not MascaraRed.es_mascara_correcta(mascara):
            raise MascaraRedError(f'La máscara no es posible: {mascara}')
        
        self.mascara = mascara


    def es_mascara_correcta(mascara: str) -> bool:
        if mascara in ("255.0.0.0", "255.255.0.0", "255.255.255.0"):
            return True
        else:
            return False
        

    def existe_comunicacion_directa(direccion_origen: str, direccion_destino: str, mascara: str) -> bool: 
        partes_mascara = mascara.split('.')
        partes_direccion_origen = direccion_origen.split('.')
        partes_direccion_destino = direccion_destino.split('.')

        for i in range(0, len(partes_mascara)):
            if partes_mascara[i] == '255':
                if partes_direccion_origen[i] != partes_direccion_destino[i]:
                    return False
                
        return True


class MascaraRedError(Exception): ...