from Red import Red
from Capa1AccesoMedio import Capa1AccesoMedio, TipoMedio, TipoTecnologia

def main():
    capaAccesoMedio = Capa1AccesoMedio(TipoMedio.INALAMBRICO, TipoTecnologia.WIFI_5)
    red = Red(capaAccesoMedio)


if __name__ == '__main__':
    main()