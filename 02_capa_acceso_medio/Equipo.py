from PuertoRed import PuertoRed, Tecnologia


class Equipo:
    
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    def añadir_puerto_red(self, puerto: PuertoRed):
        self.__puerto_red = puerto

    def conectar_a_wifi(self, ssid: str, contraseña: str):
        if self.__puerto_red is None:
            raise EquipoError('El equipo no tiene tarjeta de red.')
        if self.__puerto_red.tecnologia != Tecnologia.WIFI_300 or self.__puerto_red.tecnologia != Tecnologia.WIFI_600:
            raise EquipoError('El equipo no tiene una tarjeta de red WIFI.')

        # falta comprobar ssid y contraseña
        # nos conectamos        

class EquipoError(Exception):
    ...