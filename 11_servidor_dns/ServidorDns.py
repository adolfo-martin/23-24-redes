type DireccionIp = str

type NombreDns = str

class ServidorDns:

    def __init__(self, direccion_ip: DireccionIp) -> None:
        self.__direccion_ip = direccion_ip
        self.__registros_tipo_AAA: dict[NombreDns, DireccionIp] = {}


    @property
    def direccion_ip(self) -> DireccionIp:
        return self.__direccion_ip
    

    @direccion_ip.setter
    def direccion_ip(self, valor: DireccionIp) -> None:
        self.__direccion_ip = valor


    def añadir_registro_tipo_AAA(self, nombre_dns: NombreDns, direccion_ip: DireccionIp) -> None:
        self.__registros_tipo_AAA[nombre_dns] = direccion_ip
        

    def traducir_nombre_a_direccion(self) -> DireccionIp: ...

    def obtener_registros_tipo_AAA(self) -> dict[NombreDns, DireccionIp]: 
        return self.__registros_tipo_AAA