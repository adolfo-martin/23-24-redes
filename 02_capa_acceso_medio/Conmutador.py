from PuertoRed import PuertoRed


class Conmutador:
    __puertos: list[PuertoRed] = []
    __encendido: bool = False

    def __init__(self, cantidad_puertos: int) -> None:
        self.__cantidad_puertos = cantidad_puertos


    @property
    def puertos(self) -> list[PuertoRed]:
        return self.__puertos
    

    @property
    def cantidad_puertos(self) -> int:
        return self.__cantidad_puertos


    @property
    def encendido(self) -> bool:
        return self.__encendido
    

    def encender(self):
        self.__encendido = True


    def apagar(self):
        self.__encendido = False


    def añadir_puerto(self, puerto: PuertoRed):
        if self.__encendido:
            raise ConmutadorError('El conmutador está encendido.')
        elif len(self.__puertos) == self.__cantidad_puertos:
            raise ConmutadorError('El conmutador está completo.')
        else:
            self.__puertos.append(puerto)


class ConmutadorError(Exception):
    ...