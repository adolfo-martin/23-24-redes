import unittest

from ServidorDhcp import DhcpDireccionReservadaError, ServidorDhcp

class TestServidorDhcp(unittest.TestCase):
    
    def setUp(self) -> None:
        super().setUp()
        self.servidor = ServidorDhcp('servidor-dhcp-daw', 'AA:AA:AA:AA:AA:01')
        self.servidor.establecer_parametros_ip('192.168.1.1', '255.255.255.0', '192.168.1.1', '8.8.8.8')


    def test_init(self):
        self.assertIsInstance(self.servidor, ServidorDhcp)
        self.assertIsNone(self.servidor.direccion_inicial)
        self.assertIsNone(self.servidor.direccion_final)
        self.assertDictEqual(self.servidor.direcciones_asignadas, {})
        self.assertDictEqual(self.servidor.direcciones_reservadas, {})


    def test_establecer_parametros_dhcp(self):
        self.servidor.establecer_parametros_dhcp('192.168.1.101', '192.168.1.254')
        self.assertEqual(self.servidor.direccion_inicial, '192.168.1.101')
        self.assertEqual(self.servidor.direccion_final, '192.168.1.254')


    def test_esta_mac_en_direcciones_asignadas(self):
        self.servidor.establecer_parametros_dhcp('192.168.1.101', '192.168.1.254')

        self.assertFalse(self.servidor.esta_mac_en_direcciones_asignadas('EE:EE:EE:EE:EE:01'))

        self.servidor.solicitar_parametros_dhcp_para_equipo('EE:EE:EE:EE:EE:01')
        self.assertTrue(self.servidor.esta_mac_en_direcciones_asignadas('EE:EE:EE:EE:EE:01'))

        self.servidor.solicitar_parametros_dhcp_para_equipo('EE:EE:EE:EE:EE:02')
        self.assertTrue(self.servidor.esta_mac_en_direcciones_asignadas('EE:EE:EE:EE:EE:02'))


    def test_esta_ip_en_direcciones_asignadas(self):
        self.servidor.establecer_parametros_dhcp('192.168.1.101', '192.168.1.254')

        self.assertFalse(self.servidor.esta_ip_en_direcciones_asignadas('192.168.1.101'))

        self.servidor.solicitar_parametros_dhcp_para_equipo('EE:EE:EE:EE:EE:01')
        self.assertTrue(self.servidor.esta_ip_en_direcciones_asignadas('192.168.1.101'))

        self.servidor.solicitar_parametros_dhcp_para_equipo('EE:EE:EE:EE:EE:02')
        self.assertTrue(self.servidor.esta_ip_en_direcciones_asignadas('192.168.1.102'))


    def test_solicitar_parametros_dhcp_para_equipo(self):
        self.servidor.establecer_parametros_dhcp('192.168.1.101', '192.168.1.254')

        ip, mascara, puerta_enlace, servidor_dns = self.servidor.solicitar_parametros_dhcp_para_equipo('EE:EE:EE:EE:EE:01')
        self.assertEqual(ip, '192.168.1.101')
        self.assertEqual(mascara, '255.255.255.0')
        self.assertEqual(puerta_enlace, '192.168.1.1')
        self.assertEqual(servidor_dns, '8.8.8.8')

        ip, mascara, puerta_enlace, servidor_dns = self.servidor.solicitar_parametros_dhcp_para_equipo('EE:EE:EE:EE:EE:02')
        self.assertEqual(ip, '192.168.1.102')
        self.assertEqual(mascara, '255.255.255.0')
        self.assertEqual(puerta_enlace, '192.168.1.1')
        self.assertEqual(servidor_dns, '8.8.8.8')

        self.servidor.reservar_direccion('EE:EE:EE:EE:EE:03', '192.168.1.103')

        ip, mascara, puerta_enlace, servidor_dns = self.servidor.solicitar_parametros_dhcp_para_equipo('EE:EE:EE:EE:EE:04')
        self.assertEqual(ip, '192.168.1.104')


    def test_reservar_direccion(self): 
        self.assertFalse(self.servidor.esta_mac_en_direcciones_reservadas('EE:EE:EE:EE:EE:10'))
        self.assertFalse(self.servidor.esta_ip_en_direcciones_reservadas('192.168.1.110'))
        self.servidor.reservar_direccion('EE:EE:EE:EE:EE:10', '192.168.1.110')
        self.assertTrue(self.servidor.esta_mac_en_direcciones_reservadas('EE:EE:EE:EE:EE:10'))
        self.assertTrue(self.servidor.esta_ip_en_direcciones_reservadas('192.168.1.110'))

        with self.assertRaises(DhcpDireccionReservadaError, msg='Hay una ip en direcciones reservadas'):
            self.servidor.reservar_direccion('EE:EE:EE:EE:EE:11', '192.168.1.110')

        with self.assertRaises(DhcpDireccionReservadaError, msg='Hay una mac en direcciones reservadas'):
            self.servidor.reservar_direccion('EE:EE:EE:EE:EE:10', '192.168.1.111')
        
        self.servidor.direcciones_asignadas = {'EE:EE:EE:EE:EE:11', '192.168.1.111'}

        with self.assertRaises(DhcpDireccionReservadaError, msg='Hay una ip en direcciones asignadas'):
            self.servidor.reservar_direccion('EE:EE:EE:EE:EE:10', '192.168.1.111')
        
        with self.assertRaises(DhcpDireccionReservadaError, msg='Hay una mac en direcciones asignadas'):
            self.servidor.reservar_direccion('EE:EE:EE:EE:EE:11', '192.168.1.110')


    def test_esta_mac_en_direcciones_reservadas(self):
        self.assertFalse(self.servidor.esta_mac_en_direcciones_reservadas('EE:EE:EE:EE:EE:10'))
        self.servidor.reservar_direccion('EE:EE:EE:EE:EE:10', '192.168.1.110')
        self.assertTrue(self.servidor.esta_mac_en_direcciones_reservadas('EE:EE:EE:EE:EE:10'))
    

    def test_esta_ip_en_direcciones_reservadas(self):
        self.assertFalse(self.servidor.esta_ip_en_direcciones_reservadas('192.168.1.110'))
        self.servidor.reservar_direccion('EE:EE:EE:EE:EE:10', '192.168.1.110')
        self.assertTrue(self.servidor.esta_ip_en_direcciones_reservadas('192.168.1.110'))


if __name__ == '__main__':
    unittest.main()