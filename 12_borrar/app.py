class TarjetaRed():
    def __init__(self, direccion_mac: str, nombre: str) -> None:
        self.direccion_mac = direccion_mac
        self.nombre = nombre


class Equipo():
    def __init__(self) -> None:
        self.tarjetas: dict[str, TarjetaRed] = {}


    def añadir_tarjeta(self, tarjeta: TarjetaRed) -> None:
        self.tarjetas[tarjeta.direccion_mac] = tarjeta





def main():
    equipo = Equipo()
    tarjeta1 = TarjetaRed('11:11:11:11:11:11', 'Tarjeta WIFI')
    tarjeta2 = TarjetaRed('11:11:11:11:11:12', 'Tarjeta Cable')
    tarjeta3 = TarjetaRed('11:11:11:11:11:13', 'Tarjeta Bluetooth')
    tarjeta4 = TarjetaRed('11:11:11:11:11:14', 'Tarjeta lte 5G')

    equipo.añadir_tarjeta(tarjeta1)
    equipo.añadir_tarjeta(tarjeta2)
    equipo.añadir_tarjeta(tarjeta3)
    equipo.añadir_tarjeta(tarjeta4)


if __name__ == '__main__':
    main()