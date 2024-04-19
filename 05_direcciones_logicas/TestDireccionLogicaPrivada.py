import unittest
from DireccionLogicaPrivada import DireccionLogicaPrivada


class TestDireccionLogicaPrivada(unittest.TestCase):
    
    def test_es_direccion_correcta(self):

        self.assertFalse(DireccionLogicaPrivada.es_direccion_correcta('25'))
        self.assertFalse(DireccionLogicaPrivada.es_direccion_correcta('80.73.158.126'))

        self.assertFalse(DireccionLogicaPrivada.es_direccion_correcta('9.0.0.1'))
        self.assertTrue(DireccionLogicaPrivada.es_direccion_correcta('10.0.0.1'))
        self.assertFalse(DireccionLogicaPrivada.es_direccion_correcta('11.0.0.1'))

        self.assertFalse(DireccionLogicaPrivada.es_direccion_correcta('172.15.0.1'))
        self.assertTrue(DireccionLogicaPrivada.es_direccion_correcta('172.16.0.1'))
        self.assertTrue(DireccionLogicaPrivada.es_direccion_correcta('172.31.0.1'))
        self.assertFalse(DireccionLogicaPrivada.es_direccion_correcta('172.32.0.1'))

        self.assertFalse(DireccionLogicaPrivada.es_direccion_correcta('191.168.0.1'))
        self.assertTrue(DireccionLogicaPrivada.es_direccion_correcta('192.168.0.1'))
        self.assertFalse(DireccionLogicaPrivada.es_direccion_correcta('193.168.0.1'))
        self.assertFalse(DireccionLogicaPrivada.es_direccion_correcta('192.167.0.1'))
        self.assertFalse(DireccionLogicaPrivada.es_direccion_correcta('192.169.0.1'))



if __name__ == '__main__':
    unittest.main()