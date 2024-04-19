from DireccionLogica import DireccionLogica


class DireccionLogicaPrivada(DireccionLogica):
    
    def es_direccion_correcta(direccion_logica: str) -> bool:
        if not DireccionLogica.es_direccion_correcta(direccion_logica):
            return False
        
        if direccion_logica.startswith('10.') or direccion_logica.startswith('192.168.'):
            return True
        
        if direccion_logica[0:6] in ('172.16', '172.17', '172.18', '172.19', '172.20', '172.21', '172.22', '172.23', '172.24', '172.25', '172.26', '172.27', '172.28', '172.29', '172.30', '172.31'):
            return True
        
        return False