from typing import Protocol


class PuntoAccesoProtocol(Protocol):
    def conectar(direccion_fisica: str, contraseña: str): ...


class Equipo:

    def __init__(self, nombre: str, direccion_fisica: str) -> None:
        self.nombre = nombre
        self.direccion_fisica = direccion_fisica


    def __repr__(self) -> str:
        return f'[{self.__class__.__name__}] {self.nombre} {self.direccion_fisica}'
    

    def conectar_a_wifi(self, punto_acceso: PuntoAccesoProtocol, contraseña: str):
        punto_acceso.conectar(self.direccion_fisica, contraseña)