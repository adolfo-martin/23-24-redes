import unittest

from PuntoAcceso import PuntoAcceso, TipoWifi

class TestPuntoAcceso(unittest.TestCase):
    
    def test_init(self):
        punto_acceso = PuntoAcceso("wifi_adolfo", "Hola1234", [TipoWifi.WIFI5])
        self.assertIsInstance(punto_acceso, PuntoAcceso)

    def test_getter_ssid(self):
        punto_acceso = PuntoAcceso("wifi_adolfo", "Hola1234", [TipoWifi.WIFI5])
        self.assertEqual(punto_acceso.ssid, "wifi_adolfo")

    def test_getter_contraseña(self):
        punto_acceso = PuntoAcceso("wifi_adolfo", "Hola1234", [TipoWifi.WIFI5])
        self.assertEqual(punto_acceso.contraseña, "Hola1234")

    def test_getter_tipos_wifi(self):
        punto_acceso = PuntoAcceso("wifi_adolfo", "Hola1234", [TipoWifi.WIFI4, TipoWifi.WIFI5])
        self.assertListEqual(punto_acceso.tipos_wifi, [TipoWifi.WIFI4, TipoWifi.WIFI5])

    def test_setter_ssid(self):
        punto_acceso = PuntoAcceso("wifi_adolfo", "Hola1234", [TipoWifi.WIFI5])
        punto_acceso.ssid = "wifi_adolfo_martin"
        self.assertEqual(punto_acceso.ssid, "wifi_adolfo_martin")

    def test_setter_contraseña(self):
        punto_acceso = PuntoAcceso("wifi_adolfo", "Hola1234", [TipoWifi.WIFI5])
        punto_acceso.contraseña = "Hola5678"
        self.assertEqual(punto_acceso.contraseña, "Hola5678")



if __name__ == '__main__':
    unittest.main()