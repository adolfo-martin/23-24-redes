from enum import Enum, auto


class TipoFiltrado(Enum):
    LISTA_BLANCA = auto()
    LISTA_NEGRA = auto()


class PuntoAcceso:
    
    def __init__(self, ssid: str, contraseña: str) -> None:
        self.__ssid = ssid
        self.__contraseña = contraseña
        self.__equipos_conectados: list[str] = []
        self.__esta_cortafuegos_activado: bool = False
        self.__tipo_filtrado: TipoFiltrado = TipoFiltrado.LISTA_BLANCA
        self.__equipos_filtrados: list[str] = []


    @property
    def equipos_filtrados(self) -> list[str]:
        return self.__equipos_filtrados

    def agregar_equipo_filtrado(self, equipo: str) -> None:
        self.__equipos_filtrados.append(equipo)

    def desagregar_equipo_filtrado(self, equipo: str) -> None:
        self.__equipos_filtrados.remove(equipo)


    @property
    def tipo_filtrado(self) -> TipoFiltrado:
        return self.__tipo_filtrado

    @tipo_filtrado.setter
    def tipo_filtrado(self, valor: TipoFiltrado) -> None:
        self.__tipo_filtrado = valor


    @property
    def esta_cortafuegos_activado(self) -> bool:
        return self.__esta_cortafuegos_activado

    def activar_cortafuegos(self):
        self.__esta_cortafuegos_activado = True

    def desactivar_cortafuegos(self):
        self.__esta_cortafuegos_activado = False



    @property
    def ssid(self) -> str:
        return self.__ssid
    
    @ssid.setter
    def ssid(self, valor: str) -> None:
        self.__ssid = valor


    @property
    def contraseña(self) -> str:
        return self.__contraseña
    
    @contraseña.setter
    def contraseña(self, valor: str) -> None:
        self.__contraseña = valor


    @property
    def equipos_conectados(self) -> list[str]:
        return self.__equipos_conectados
    

    def conectar_equipo(self, direccion_equipo: str, contraseña: str) -> None:
        if self.esta_cortafuegos_activado:
            if self.tipo_filtrado == TipoFiltrado.LISTA_BLANCA:
                if self.equipos_filtrados.count(direccion_equipo) != 0:
                    self.__equipos_conectados.append(direccion_equipo)
                else:
                    raise PuntoAccesoError('El equipo no está en la lista blanca.')
            else: # LISTA_NEGRA
                if self.equipos_filtrados.count(direccion_equipo) == 0:
                    self.__equipos_conectados.append(direccion_equipo)
                else:
                    raise PuntoAccesoError('El equipo está en la lista negra.')

        else: #cortafuegos desactivado
            if contraseña == self.__contraseña:
                self.__equipos_conectados.append(direccion_equipo)
            else:
                raise PuntoAccesoError('La contraseña no es correcta.')





    def desconectar_equipo(self, direccion_equipo: str) -> None:
        self.equipos_conectados.remove(direccion_equipo)



class PuntoAccesoError(Exception):
    ...