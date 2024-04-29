import unittest

from MascaraRed import MascaraRed

class TestMascaraRed(unittest.TestCase):
    
    def test_existe_comunicacion_directa(self):
        self.assertFalse(MascaraRed.existe_comunicacion_directa('172.16.1.2', '172.16.2.2', '255.255.255.0'))
        self.assertTrue(MascaraRed.existe_comunicacion_directa('172.16.1.2', '172.16.2.2', '255.255.0.0'))



if __name__ == '__main__':
    unittest.main()