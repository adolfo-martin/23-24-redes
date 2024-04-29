import unittest

from CuatroOctetos import CuatroOctetos, CuatroOctetosError

class TestCuatroOctetos(unittest.TestCase):

    def test_init(self):
        self.assertIsInstance(CuatroOctetos("192.168.1.1"), CuatroOctetos)

        with self.assertRaises(CuatroOctetosError):
            CuatroOctetos("hola")


    def test_es_direccion_correcta(self):
        self.assertTrue(CuatroOctetos.es_formato_correcto("192.168.1.1"))
        self.assertTrue(CuatroOctetos.es_formato_correcto("172.16.0.1"))
        self.assertTrue(CuatroOctetos.es_formato_correcto("10.0.0.1"))
        self.assertTrue(CuatroOctetos.es_formato_correcto("80.73.158.126"))

        self.assertFalse(CuatroOctetos.es_formato_correcto(1))
        self.assertFalse(CuatroOctetos.es_formato_correcto(1.1))
        self.assertFalse(CuatroOctetos.es_formato_correcto(True))
        self.assertFalse(CuatroOctetos.es_formato_correcto([]))
        self.assertFalse(CuatroOctetos.es_formato_correcto({}))
        self.assertFalse(CuatroOctetos.es_formato_correcto("hola"))
        self.assertFalse(CuatroOctetos.es_formato_correcto("192.168.1.hola"))
        self.assertFalse(CuatroOctetos.es_formato_correcto("192.168.1"))
        self.assertFalse(CuatroOctetos.es_formato_correcto("192.168.1.1.1"))
        
        self.assertFalse(CuatroOctetos.es_formato_correcto("-1.192.168.1"))
        self.assertFalse(CuatroOctetos.es_formato_correcto("256.192.168.1"))
        self.assertFalse(CuatroOctetos.es_formato_correcto("192.-1.168.1"))
        self.assertFalse(CuatroOctetos.es_formato_correcto("192.256.1.1"))
        self.assertFalse(CuatroOctetos.es_formato_correcto("192.168.-1.1"))
        self.assertFalse(CuatroOctetos.es_formato_correcto("192.168.256.1"))
        self.assertFalse(CuatroOctetos.es_formato_correcto("192.168.1.-1"))
        self.assertFalse(CuatroOctetos.es_formato_correcto("192.168.1.256"))



if __name__ == '__main__':
    unittest.main()