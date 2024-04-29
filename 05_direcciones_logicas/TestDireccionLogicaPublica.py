import unittest

from DireccionLogicaPublica import DireccionLogicaPublica

class TestDireccionLogicaPublica(unittest.TestCase):

    def test_es_direccion_correcta(self):
        self.assertTrue(DireccionLogicaPublica.es_formato_correcto('80.73.158.126'))

        self.assertFalse(DireccionLogicaPublica.es_formato_correcto('10.0.0.1'))
        self.assertFalse(DireccionLogicaPublica.es_formato_correcto('172.16.0.1'))
        self.assertFalse(DireccionLogicaPublica.es_formato_correcto('192.168.0.1'))

        self.assertFalse(DireccionLogicaPublica.es_formato_correcto('25'))
        


if __name__ == '__main__':
    unittest.main()