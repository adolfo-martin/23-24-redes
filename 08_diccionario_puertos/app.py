from LibreriaCapaTransporte import Aplicacion, PuertoRed, TipoServicio


def main():
    puerto_http = PuertoRed(80, TipoServicio.TCP)
    puerto_https = PuertoRed(443, TipoServicio.TCP)
    puerto_mysql = PuertoRed(3306, TipoServicio.TCP)
    puerto_oracle = PuertoRed(5432, TipoServicio.TCP)
    puerto_ftp = PuertoRed(21, TipoServicio.TCP)

    puertos_ocupados: dict[PuertoRed, Aplicacion] = {}

    puertos_ocupados[puerto_ftp] = 'Filezilla Server.exe'
    puertos_ocupados[puerto_http] = 'Apache Server.exe'
    puertos_ocupados[puerto_https] = 'Apache Server.exe'
    puertos_ocupados[puerto_mysql] = 'mysqld.exe'


    RESTRICCION_PROHIBIDISIMA = 1023
    RESTRICCION_INFERIOR_PROGRAMADORES = 1024 
    RESTRICCION_SUPERIOR_PROGRAMADORES = 32767
    RESTRICCION_INFERIOR_WINDOWS = 32768
    RESTRICCION_SUPERIOR_WINDOWS = 65535

    puerto_chrome1 = PuertoRed(32768, TipoServicio.TCP)
    puerto_chrome2 = PuertoRed(32769, TipoServicio.TCP)
    puerto_firefox = PuertoRed(32770, TipoServicio.TCP)
    puerto_chrome3 = PuertoRed(32771, TipoServicio.TCP)

    puertos_ocupados[puerto_chrome1] = 'chrome.exe'
    puertos_ocupados[puerto_chrome2] = 'chrome.exe'
    puertos_ocupados[puerto_firefox] = 'firefox_browser.exe'
    puertos_ocupados[puerto_chrome3] = 'chrome.exe'

    print('Las conexiones activas son:')
    for puerto in puertos_ocupados:
        print(puerto.tipo_servicio.value, puerto.numero_puerto, puertos_ocupados[puerto])



if __name__ == '__main__':
    main()









# class Puerto:
#     PUERTOS_LIMITE_INFERIOR = 0         #Propiedad estática
#     PUERTOS_LIMITE_SUPERIOR = 65535     #Propiedad estática
    
#     def __init__(self, numero: int, tipo_puerto: TipoPuerto) -> None:
#         if not Puerto.es_numero_puerto_correcto(numero):
#             raise PuertoError(f'El número de puerto {numero} no es posible.')
        
#         self.__numero = numero
#         self.__tipo_puerto = tipo_puerto


#     @property
#     def numero(self) -> int:
#         return self.__numero
    

#     @numero.setter
#     def numero(self, valor: int) -> None:
#         if not Puerto.es_numero_puerto_correcto(valor):
#             raise PuertoError(f'El número de puerto {valor} no es posible.')
#         self.__numero = valor


#     @property
#     def tipo_puerto(self) -> TipoPuerto:
#         return self.__tipo_puerto
    

#     @tipo_puerto.setter
#     def tipo_puerto(self, valor: TipoPuerto) -> None:
#         self.__tipo_puerto = valor



#     def es_numero_puerto_correcto(numero: int) -> bool:
#         return numero >= Puerto.PUERTOS_LIMITE_INFERIOR and numero <= Puerto.PUERTOS_LIMITE_SUPERIOR


# if __name__ == '__main__':
#     main()