import unittest

from DireccionLogica import DireccionLogica

class TestDireccionLogica(unittest.TestCase):

    def test_es_direccion_correcta(self):
        self.assertTrue(DireccionLogica.es_direccion_correcta("192.168.1.1"))
        self.assertTrue(DireccionLogica.es_direccion_correcta("172.16.0.1"))
        self.assertTrue(DireccionLogica.es_direccion_correcta("10.0.0.1"))
        self.assertTrue(DireccionLogica.es_direccion_correcta("80.73.158.126"))

        self.assertFalse(DireccionLogica.es_direccion_correcta(1))
        self.assertFalse(DireccionLogica.es_direccion_correcta(1.1))
        self.assertFalse(DireccionLogica.es_direccion_correcta(True))
        self.assertFalse(DireccionLogica.es_direccion_correcta([]))
        self.assertFalse(DireccionLogica.es_direccion_correcta({}))
        self.assertFalse(DireccionLogica.es_direccion_correcta("hola"))
        self.assertFalse(DireccionLogica.es_direccion_correcta("192.168.1.hola"))
        self.assertFalse(DireccionLogica.es_direccion_correcta("192.168.1"))
        self.assertFalse(DireccionLogica.es_direccion_correcta("192.168.1.1.1"))
        
        self.assertFalse(DireccionLogica.es_direccion_correcta("-1.192.168.1"))
        self.assertFalse(DireccionLogica.es_direccion_correcta("256.192.168.1"))
        self.assertFalse(DireccionLogica.es_direccion_correcta("192.-1.168.1"))
        self.assertFalse(DireccionLogica.es_direccion_correcta("192.256.1.1"))
        self.assertFalse(DireccionLogica.es_direccion_correcta("192.168.-1.1"))
        self.assertFalse(DireccionLogica.es_direccion_correcta("192.168.256.1"))
        self.assertFalse(DireccionLogica.es_direccion_correcta("192.168.1.-1"))
        self.assertFalse(DireccionLogica.es_direccion_correcta("192.168.1.256"))



if __name__ == '__main__':
    unittest.main()