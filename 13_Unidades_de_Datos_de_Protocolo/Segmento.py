class Segmento:
    def __init__(self, 
        puerto_origen: int, 
        puerto_destino: int, 
        numero_secuencia: int, 
        suma_verificacion: bytes, 
        datos: bytes
    ) -> None:
        """
        Un segmento representa la información que gestiona la capa de transporte
        """
        self.puerto_origen = puerto_origen
        self.puerto_destino = puerto_destino
        self.numero_secuencia = numero_secuencia
        self.suma_verificacion  = suma_verificacion
        self.datos = datos
        
