import unittest

from DireccionFisica import DireccionFisica
from PuertoRed import PuertoRed, Tecnologia

class TestPuertoRed(unittest.TestCase):

    def test_init(self):
        direccion = DireccionFisica('A1:B2:C3:D4:E5:F6')
        puerto = PuertoRed(direccion, Tecnologia.PAR_TRENZADO_1000)
        self.assertIsInstance(puerto, PuertoRed)


    def test_getter_tecnologia(self):
        direccion = DireccionFisica('A1:B2:C3:D4:E5:F6')
        puerto = PuertoRed(direccion, Tecnologia.PAR_TRENZADO_1000)
        self.assertEqual(puerto.tecnologia, Tecnologia.PAR_TRENZADO_1000)



if __name__ == '__main__':
    unittest.main()