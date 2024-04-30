from Menu import Menu
from ServidorDhcp import ServidorDhcp

def main():
    servidor: ServidorDhcp = None

    menu = Menu()
    while True:
        menu.mostrar_menu()
        opcion = menu.pedir_opcion()
        match opcion:
            case '1':
                nombre_servidor, direccion_mac, direccion_ip, mascara_red, puerta_enlace, servidor_dns, direccion_inicial, direccion_final = \
                    menu.pedir_configuracion_servidor_dhcp()
                servidor = ServidorDhcp(nombre_servidor, direccion_mac)
                servidor.establecer_parametros_ip(direccion_ip, mascara_red, puerta_enlace, servidor_dns)
                servidor.establecer_parametros_dhcp(direccion_inicial, direccion_final)

            case '2':
                if len(servidor.direcciones_asignadas) == 0:
                    print('\tNo hay direcciones asignadas.')
                else:
                    print('\tLas direcciones asignadas son:')
                    for direccion_mac in servidor.direcciones_asignadas:
                        print(f'\t\t{direccion_mac} - {servidor.direcciones_asignadas[direccion_mac]}')

            case '3':
                if len(servidor.direcciones_reservadas) == 0:
                    print('\tNo hay direcciones reservadas.')
                else:
                    print('\tLas direcciones reservadas son:')
                    for direccion_mac in servidor.direcciones_reservadas:
                        print(f'\t\t{direccion_mac} - {servidor.direcciones_reservadas[direccion_mac]}')

            case '4':
                direccion_mac = menu.pedir_direccion_mac()
                parametros_dhcp = servidor.solicitar_parametros_dhcp_para_equipo(direccion_mac)
                print('\tLa configuración obtenida por DHCP del equipo es: ')
                print(f'\t\t{parametros_dhcp}')

            case '5':
                direccion_mac = menu.pedir_direccion_mac()
                direccion_ip = menu.pedir_direccion_ip()
                servidor.reservar_direccion(direccion_mac, direccion_ip)


if __name__ == '__main__':
    main()