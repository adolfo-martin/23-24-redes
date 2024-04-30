class Menu:

    def mostrar_menu(self):
        print('\n\n-------------------- MENU --------------------')
        print('1) Configurar servidor DHCP.')
        print('2) Mostrar direcciones asignadas.')
        print('3) Mostrar direcciones reservadas.')
        print('4) Pedir parámetros DHCP para equipo.')
        print('5) Reservar dirección IP.')


    def pedir_opcion(self) -> str:
        while True:
            opcion = input('\nElige una opción: ')
            if opcion in ('1', '2', '3', '4', '5'):
                return opcion
            

    def pedir_configuracion_servidor_dhcp(self):
        nombre_servidor = input('\tDime el nombre del servidor [servidor-dhcp-daw]: ')
        if nombre_servidor == '':
            nombre_servidor = 'servidor-dhcp-daw'

        direccion_mac = input('\tDime la dirección MAC [AA:AA:AA:AA:AA:01]: ')
        if direccion_mac == '':
            direccion_mac = 'AA:AA:AA:AA:AA:01'

        direccion_ip = input('\tDime la dirección IP [192.168.1.1]: ')
        if direccion_ip == '':
            direccion_ip = '192.168.1.1'

        mascara_red = input('\tDime la máscara de red [255.255.255.0]: ')
        if mascara_red == '':
            mascara_red = '255.255.255.0'

        puerta_enlace = input('\tDime la puerta de enlace [192.168.1.1]: ')
        if puerta_enlace == '':
            puerta_enlace = '192.168.1.1'

        servidor_dns = input('\tDime el servidor DNS [8.8.8.8]: ')
        if servidor_dns == '':
            servidor_dns = '8.8.8.8'

        direccion_inicial = input('\tDime la dirección inicial [192.168.1.101]: ')
        if direccion_inicial == '':
            direccion_inicial = '192.168.1.101'

        direccion_final = input('\tDime la dirección final [192.168.1.254]: ')
        if direccion_final == '':
            direccion_final = '192.168.1.254'

        return nombre_servidor, direccion_mac, direccion_ip, mascara_red, puerta_enlace, servidor_dns, direccion_inicial, direccion_final


    def pedir_direccion_mac(self):
        direccion_mac = input('\tDime la dirección MAC del equipo [EE:EE:EE:EE:EE:01]: ')
        if direccion_mac == '':
            direccion_mac = 'EE:EE:EE:EE:EE:01'
        return direccion_mac
    

    def pedir_direccion_ip(self):
        direccion_ip = input('\tDime la dirección IP del equipo [192.168.1.101]: ')
        if direccion_ip == '':
            direccion_ip = '192.168.1.101'
        return direccion_ip
