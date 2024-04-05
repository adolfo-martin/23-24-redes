import unittest

from Capa1AccesoMedio import Capa1AccesoMedio, TipoMedio, TipoTecnologia

class TestCapaAccesoMedio(unittest.TestCase):
    
    def test_getter_medio(self):
        capa = Capa1AccesoMedio(TipoMedio.INALAMBRICO, TipoTecnologia.WIFI_4)
        self.assertEqual(capa.medio, TipoMedio.INALAMBRICO)

    def test_getter_tecnologia(self):
        capa = Capa1AccesoMedio(TipoMedio.INALAMBRICO, TipoTecnologia.WIFI_4)
        self.assertEqual(capa.tecnologia, TipoTecnologia.WIFI_4)

    def test_setter_medio(self):
        capa = Capa1AccesoMedio(TipoMedio.INALAMBRICO, TipoTecnologia.WIFI_4)
        capa.medio = TipoMedio.ALAMBRICO
        self.assertEqual(capa.medio, TipoMedio.ALAMBRICO)

    def test_setter_tecnologia(self):
        capa = Capa1AccesoMedio(TipoMedio.INALAMBRICO, TipoTecnologia.WIFI_4)
        capa.tecnologia = TipoTecnologia.BLUETOOTH
        self.assertEqual(capa.tecnologia, TipoTecnologia.BLUETOOTH)

if __name__ == '__main__':
    unittest.main()