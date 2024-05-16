from Capa_transporte import CapaTransporte
from Mensaje import Mensaje
# La librería pickle me permite serializar datos
import pickle



class Whatsapp:

    def establecer_capa_transporte(self, capa_transporte: CapaTransporte):
        self.capa_transporte = capa_transporte

    def enviar(self, mensaje: Mensaje):
        datos = pickle.dumps(mensaje)
        self.capa_transporte.enviar(datos)

    def recibir(self, datos: bytes):
        mensaje = pickle.loads(datos)
