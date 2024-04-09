import unittest

from Conmutador import Conmutador
from DireccionFisica import DireccionFisica
from PuertoRed import PuertoRed, Tecnologia

class TestConmutador(unittest.TestCase):
    
    def test_init(self):
        direccion1 = DireccionFisica('00:00:00:00:00:01')
        puerto1 = PuertoRed(direccion1, Tecnologia.PAR_TRENZADO_1000)
        direccion2 = DireccionFisica('00:00:00:00:00:02')
        puerto2 = PuertoRed(direccion1, Tecnologia.PAR_TRENZADO_1000)
        direccion3 = DireccionFisica('00:00:00:00:00:03')
        puerto3 = PuertoRed(direccion1, Tecnologia.PAR_TRENZADO_1000)
        direccion4 = DireccionFisica('00:00:00:00:00:04')
        puerto4 = PuertoRed(direccion1, Tecnologia.PAR_TRENZADO_1000)
        conmutador = Conmutador([puerto1, puerto2, puerto3, puerto4])
        self.assertIsInstance(conmutador, Conmutador)

if __name__ == '__main__':
    unittest.main()