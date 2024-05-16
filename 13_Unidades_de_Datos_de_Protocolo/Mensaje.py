type Telefono = int

class Mensaje:
    def __init__(self, mensaje: str, telefono_emisor: Telefono, telefono_receptor: Telefono, hora_envio: str) -> None:
        """
        Un mensaje representa un tipo de información que gestiona Whatsapp.
        """
        self.mensaje = mensaje
        self.telefono_emisor = telefono_emisor
        self.telefono_receptor = telefono_receptor
        self.hora_envio = hora_envio
