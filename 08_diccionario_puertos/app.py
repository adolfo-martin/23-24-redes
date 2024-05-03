from enum import Enum


def main():
    puerto_ftp = Puerto(21, TipoPuerto.TCP)
    puerto_http = Puerto(80, TipoPuerto.TCP)
    puerto_https = Puerto(443, TipoPuerto.TCP)
    puerto_mysql = Puerto(3306, TipoPuerto.TCP)

    puertos_ocupados: dict[Puerto, str] = {}
    puertos_ocupados[puerto_ftp] = 'Filezilla Server.exe'
    puertos_ocupados[puerto_http] = 'Apache Server.exe'
    puertos_ocupados[puerto_https] = 'Apache Server.exe'
    puertos_ocupados[puerto_mysql] = 'mysqld.exe'


    restriccion_inferior_windows = 1024
    restriccion_superior_windows = 32768
    programa = 'chrome_browser.exe'

    puerto_chrome = ???




class TipoPuerto(Enum):
    TCP = 'tcp'
    UDP = 'udp'


class PuertoError(Exception): ...


class Puerto:
    PUERTOS_LIMITE_INFERIOR = 0         #Propiedad estática
    PUERTOS_LIMITE_SUPERIOR = 65535     #Propiedad estática
    
    def __init__(self, numero: int, tipo_puerto: TipoPuerto) -> None:
        if not Puerto.es_numero_puerto_correcto(numero):
            raise PuertoError(f'El número de puerto {numero} no es posible.')
        
        self.__numero = numero
        self.__tipo_puerto = tipo_puerto


    @property
    def numero(self) -> int:
        return self.__numero
    

    @numero.setter
    def numero(self, valor: int) -> None:
        if not Puerto.es_numero_puerto_correcto(valor):
            raise PuertoError(f'El número de puerto {valor} no es posible.')
        self.__numero = valor


    @property
    def tipo_puerto(self) -> TipoPuerto:
        return self.__tipo_puerto
    

    @tipo_puerto.setter
    def tipo_puerto(self, valor: TipoPuerto) -> None:
        self.__tipo_puerto = valor



    def es_numero_puerto_correcto(numero: int) -> bool:
        return numero >= Puerto.PUERTOS_LIMITE_INFERIOR and numero <= Puerto.PUERTOS_LIMITE_SUPERIOR


if __name__ == '__main__':
    main()