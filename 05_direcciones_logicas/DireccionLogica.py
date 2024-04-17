class DireccionLogica:

    def __init__(self, direccion_logica: str) -> None:
        pass


    def es_direccion_correcta(direccion_logica: str) -> bool:
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