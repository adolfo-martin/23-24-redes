from Segmento import Segmento

PUERTO_SERVIDOR_WHATSAPP = 2514

class CapaTransporte:

    def enviar(datos: bytes):
        segmento = Segmento(36478, PUERTO_SERVIDOR_WHATSAPP, 1, 0, datos)

    def recibir(datos: bytes): ...