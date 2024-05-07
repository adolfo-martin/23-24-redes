class Arquitectura(str): ...
class Capa(str): ...

arquitecturas_estandar_de_red: dict[Arquitectura,list[Capa]] = {

    'TPC/IP': [

        'Capa de acceso a la red',
        'Capa de internet',
        'Capa de transporte',
        'Capa de aplicación'

    ],

    'OSI':[
        'Capa de enlace de datos',
        'Capa de red',
        'Capa de transporte',
        'Capa de sesión',
        'Capa de presentación',
        'Capa de aplicación'

    ]

}


print('Las arquitecturas estándares de red son: ')


for arquitectura in arquitecturas_estandar_de_red.keys():
        print(f'\t* {arquitectura}')

for arquitectura in arquitecturas_estandar_de_red.keys():
    print(f'Las capas de la arquitectura {arquitectura} son: ')
    for capa in arquitecturas_estandar_de_red[arquitectura]:
        print(f'\t* {capa}')












