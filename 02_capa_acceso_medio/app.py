import os
from DireccionFisica import DireccionFisica

os.system('cls')

try:
    direccion1 = DireccionFisica('G5:A3:14:BC:D9:6D')
except Exception as error:
    print(error)

print('FIN')