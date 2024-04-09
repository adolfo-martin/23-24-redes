import unittest
from DireccionFisica import DireccionFisica

class TestDireccionFisica(unittest.TestCase):

    def test_es_direccion_correcta(self):
        self.assertFalse(DireccionFisica.es_direccion_correcta(1))
        self.assertFalse(DireccionFisica.es_direccion_correcta("hola"))
        self.assertFalse(DireccionFisica.es_direccion_correcta(False))
        self.assertFalse(DireccionFisica.es_direccion_correcta("1234567890123456"))
        self.assertFalse(DireccionFisica.es_direccion_correcta("123456789012345678"))
        self.assertFalse(DireccionFisica.es_direccion_correcta("D0:37:45:DE:01"))
        self.assertFalse(DireccionFisica.es_direccion_correcta("D0:37:45:DE:01:F2:A1"))
        self.assertFalse(DireccionFisica.es_direccion_correcta("D0A:37:45:DE:01:F2"))
        self.assertFalse(DireccionFisica.es_direccion_correcta("D:37:45:DE:01:F2"))
        self.assertFalse(DireccionFisica.es_direccion_correcta("G0:37:45:DE:01:F2"))
        self.assertFalse(DireccionFisica.es_direccion_correcta("g0:37:45:dE:01:f2"))
        self.assertFalse(DireccionFisica.es_direccion_correcta("D0-37-45-DE-01-F2"))

        self.assertTrue(DireccionFisica.es_direccion_correcta("A0:B1:C2:D3:E4:F5"))
        self.assertTrue(DireccionFisica.es_direccion_correcta("a0:b1:c2:d3:e4:f5"))


    def test_init(self):
        direccion1 = DireccionFisica('E5:A3:14:BC:D9:6D')

        with self.assertRaises(Exception):
            direccion2 = DireccionFisica('G5:A3:14:BC:D9:6D')


    def test_getter_direccion(self):
        direccion1 = DireccionFisica('E5:A3:14:BC:D9:6D')
        self.assertEqual(direccion1.direccion, 'E5:A3:14:BC:D9:6D')


    def test_setter_direccion(self):
        direccion1 = DireccionFisica('E5:A3:14:BC:D9:6D')
        direccion1.direccion = 'A1:B2:C3:D4:E5:D6'
        self.assertEqual(direccion1.direccion, 'A1:B2:C3:D4:E5:D6')


if __name__ == '__main__':
    unittest.main()