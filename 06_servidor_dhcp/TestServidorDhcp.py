import unittest

from ServidorDhcp import ServidorDhcp

class TestServidorDhcp(unittest.TestCase):
    
    def test_init(self):
        servidor = ServidorDhcp('00:11:22:33:44:55', 'servidor-dhcp')
        self.assertIsInstance(servidor, ServidorDhcp)
        self.assertIsNone(servidor.direccion_ip_inicio)
        self.assertIsNone(servidor.direccion_ip_fin)
        self.assertDictEqual(servidor.direcciones_asignadas, {})


if __name__ == '__main__':
    unittest.main()