import unittest
from DireccionLogicaPrivada import DireccionLogicaPrivada


class TestDireccionLogicaPrivada(unittest.TestCase):
    
    def test_es_direccion_correcta(self):

        self.assertFalse(DireccionLogicaPrivada.es_formato_correcto('25'))
        self.assertFalse(DireccionLogicaPrivada.es_formato_correcto('80.73.158.126'))

        self.assertFalse(DireccionLogicaPrivada.es_formato_correcto('9.0.0.1'))
        self.assertTrue(DireccionLogicaPrivada.es_formato_correcto('10.0.0.1'))
        self.assertFalse(DireccionLogicaPrivada.es_formato_correcto('11.0.0.1'))

        self.assertFalse(DireccionLogicaPrivada.es_formato_correcto('172.15.0.1'))
        self.assertTrue(DireccionLogicaPrivada.es_formato_correcto('172.16.0.1'))
        self.assertTrue(DireccionLogicaPrivada.es_formato_correcto('172.31.0.1'))
        self.assertFalse(DireccionLogicaPrivada.es_formato_correcto('172.32.0.1'))

        self.assertFalse(DireccionLogicaPrivada.es_formato_correcto('191.168.0.1'))
        self.assertTrue(DireccionLogicaPrivada.es_formato_correcto('192.168.0.1'))
        self.assertFalse(DireccionLogicaPrivada.es_formato_correcto('193.168.0.1'))
        self.assertFalse(DireccionLogicaPrivada.es_formato_correcto('192.167.0.1'))
        self.assertFalse(DireccionLogicaPrivada.es_formato_correcto('192.169.0.1'))



if __name__ == '__main__':
    unittest.main()