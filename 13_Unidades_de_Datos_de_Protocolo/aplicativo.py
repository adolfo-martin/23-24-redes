from Mensaje import Mensaje
import pickle
import os

os.system('cls')

# mensaje = Mensaje('Hola, cómo estás 😊', 666333111, 666777888, '2024-05-16 13:06')

def serializar(informacion: object) -> bytes:
    return pickle.dumps(informacion)


def deserializar(datos: bytes) -> object:
    return pickle.loads(datos)


# alumno = { 
#     'nombre': 'Jimena',
#     'apellido': 'Sánchez',
#     'edad': 39,
#     'aficiones': ['cantar', 'bailar', 'programar'],
#     'avatar': '😃'
# }

# alumno_serializado = serializar(alumno)
# alumno_deserializado = deserializar(alumno_serializado)

# print(alumno)
# print(alumno_serializado)
# print(alumno_deserializado)


# alumno_serializado = pickle.dumps(alumno)
# print(alumno)
# print(alumno_serializado)
# # guardaríamos alumno en un fichero o lo enviaríamos por la red
# alumno_deserializado = pickle.loads(alumno_serializado)
# print(alumno_deserializado)