import unittest

from PuntoAcceso import PuntoAcceso, PuntoAccesoError, TipoFiltrado

class PuntoAccesoTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.punto_acceso = PuntoAcceso('wifi_adolfo', 'Hola1234')
        self.equipo1 = 'AA:AA:AA:AA:AA:01'
        self.equipo2 = 'AA:AA:AA:AA:AA:02'
        self.equipo3 = 'AA:AA:AA:AA:AA:03'
        self.equipo4 = 'AA:AA:AA:AA:AA:04'
        self.equipo5 = 'AA:AA:AA:AA:AA:05'
        

    def test_init(self):
        self.assertIsInstance(self.punto_acceso, PuntoAcceso)
        self.assertEqual(self.punto_acceso.ssid, 'wifi_adolfo')
        self.assertEqual(self.punto_acceso.contraseña, 'Hola1234')
        self.assertListEqual(self.punto_acceso.equipos_conectados, [])
        self.assertFalse(self.punto_acceso.esta_cortafuegos_activado)
        self.assertEqual(self.punto_acceso.tipo_filtrado, TipoFiltrado.LISTA_BLANCA)
        self.assertListEqual(self.punto_acceso.equipos_filtrados, [])


    def test_getter_ssid(self):
        self.assertEqual(self.punto_acceso.ssid, 'wifi_adolfo')


    def test_esta_cortafuegos_activado(self):
        self.assertFalse(self.punto_acceso.esta_cortafuegos_activado)

    
    def test_activar_cortafuegos(self):
        self.punto_acceso.activar_cortafuegos()
        self.assertTrue(self.punto_acceso.esta_cortafuegos_activado)


    def test_desactivar_cortafuegos(self):
        self.punto_acceso.activar_cortafuegos()
        self.punto_acceso.desactivar_cortafuegos()
        self.assertFalse(self.punto_acceso.esta_cortafuegos_activado)


    def test_agregar_equipo_filtrado(self):
        self.assertListEqual(self.punto_acceso.equipos_filtrados, [])
        self.punto_acceso.agregar_equipo_filtrado(self.equipo1)
        self.assertListEqual(self.punto_acceso.equipos_filtrados, [self.equipo1])
        self.punto_acceso.agregar_equipo_filtrado(self.equipo2)
        self.assertListEqual(self.punto_acceso.equipos_filtrados, [self.equipo1, self.equipo2])


    def test_conectar_equipo(self):
        self.punto_acceso.conectar_equipo(self.equipo1, 'Hola1234')
        self.assertListEqual(self.punto_acceso.equipos_conectados, [self.equipo1])
        self.punto_acceso.conectar_equipo(self.equipo2, 'Hola1234')
        self.assertListEqual(self.punto_acceso.equipos_conectados, [self.equipo1, self.equipo2])

        with self.assertRaises(PuntoAccesoError):
            self.punto_acceso.conectar_equipo(self.equipo3, 'Hola5678')
            self.assertListEqual(self.punto_acceso.equipos_conectados, [self.equipo1, self.equipo2])

        # Ahora estamos con lista blanca
        with self.assertRaises(PuntoAccesoError):
            self.punto_acceso.activar_cortafuegos()
            self.punto_acceso.conectar_equipo(self.equipo3, 'Hola1234')
            self.assertListEqual(self.punto_acceso.equipos_conectados, [self.equipo1, self.equipo2])

        self.punto_acceso.agregar_equipo_filtrado(self.equipo3)
        self.punto_acceso.conectar_equipo(self.equipo3, 'Hola1234')
        self.assertListEqual(self.punto_acceso.equipos_conectados, [self.equipo1, self.equipo2, self.equipo3])

        # Ahora estamos con lista negra
        self.punto_acceso.tipo_filtrado = TipoFiltrado.LISTA_NEGRA

        self.punto_acceso.conectar_equipo(self.equipo4, 'Hola1234')
        self.assertListEqual(self.punto_acceso.equipos_conectados, [self.equipo1, self.equipo2, self.equipo3, self.equipo4])

        with self.assertRaises(PuntoAccesoError):
            self.punto_acceso.agregar_equipo_filtrado(self.equipo5)
            self.punto_acceso.conectar_equipo(self.equipo5, 'Hola1234')
            self.assertListEqual(self.punto_acceso.equipos_conectados, [self.equipo1, self.equipo2, self.equipo3, self.equipo4])

if __name__ == '__main__':
    unittest.main()