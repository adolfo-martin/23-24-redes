class CuatroOctetos:

    def __init__(self, octetos: str) -> None:
        if not CuatroOctetos.es_formato_correcto(octetos):
            raise CuatroOctetosError(f'El formato del octeto no es correcto: {octetos}')

        self.octetos = octetos


    def es_formato_correcto(direccion_logica: str) -> bool:
        if not isinstance(direccion_logica, str):
            return False

        partes = direccion_logica.split('.')
        if len(partes) != 4:
            return False

        for parte in partes:
            if not parte.isnumeric():
                return False

            numero = int(parte)
            if numero < 0 or numero > 255:
                return False
                
        return True
    

class CuatroOctetosError(Exception): ...