from enum import Enum, auto

class TipoWifi(Enum):
    WIFI1 = auto()
    WIFI2 = auto()
    WIFI3 = auto()
    WIFI4 = auto()
    WIFI5 = auto()
    WIFI6 = auto()


class PuntoAcceso:
    """
    Un punto de acceso permite añadir dispositivos inalámbricos a la red.
    """
    def __init__(self, ssid: str, contraseña: str, tipos_wifi: list[TipoWifi]) -> None:
        self.__ssid = ssid
        self.__contraseña = contraseña
        self.__tipos_wifi = tipos_wifi

    @property
    def ssid(self) -> str:
        return self.__ssid
    
    @ssid.setter
    def ssid(self, valor: str) -> None:
        """
        El SSID debe tener al menos seis caracteres
        """
        self.__ssid = valor

    @property
    def contraseña(self) -> str:
        return self.__contraseña
    
    @contraseña.setter
    def contraseña(self, valor: str) -> None:
        self.__contraseña = valor

    @property
    def tipos_wifi(self) -> list[TipoWifi]:
        return self.__tipos_wifi