import unittest

from ServidorDns import DireccionIp, NombreDns, ServidorDns


class Alumno:
    def __init__(self, nre: str, nombre: str, apellido: str) -> None:
        self.nre = 41835
        self.nombre = nombre
        self.apellido = apellido

    def __eq__(self, value: object) -> bool:
        return self.nre == value.nre and self.nombre == value.nombre and self.apellido == value.apellido

    def __repr__(self) -> str:
        return f'[{self.nre}] {self.nombre} {self.apellido}'



class ServidorDnsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.alumnos = []       
        alumno1 = Alumno(41835, 'Alberto', 'Cánovas')
        self.alumnos.append(alumno1)

    
    # def test_init(self):
    #     servidor = ServidorDns('192.168.1.254')
    #     self.assertIsInstance(servidor, ServidorDns)
    #     self.assertEqual(servidor.direccion_ip, '192.168.1.254')
    #     self.assertDictEqual(servidor.obtener_registros_tipo_AAA(), {})


    # def test_añadir_registro_tipo_AAA(self) -> None:
    #     servidor = ServidorDns('192.168.1.254')
    #     nombre_dns = 'www.iesramonarcas.es'
    #     direccion_ip = '217.160.0.70'
    #     servidor.añadir_registro_tipo_AAA(nombre_dns, direccion_ip)
    #     # print(servidor.obtener_registros_tipo_AAA())
    #     # self.assertDictEqual(servidor.obtener_registros_tipo_AAA(), {nombre_dns: direccion_ip})
    #     self.assertDictEqual(servidor.obtener_registros_tipo_AAA(), {'www.iesramonarcas.es': '217.160.0.70'})


    def test_falso(self):              
        alumno1 = Alumno(41835, 'Alberto', 'Cánovas')
        self.assertListEqual(self.alumnos, [alumno1])

        # print(alumno1.__eq__(alumno2))
        # print(alumno1 == alumno2)
        # print(alumno1)
        # print(alumno2)




        # print(alumno1 == {'nombre': 'Alberto', 'apellido': 'Cánovas'})




if __name__ == '__main__':
    unittest.main()