#Codigo en Constantes.py

Marcas_de_coches = ['HONDA', 'MAZDA', 'TOYOTA']
FORMATOS_Y_TIPOS = {
    int : '\d+',
    str : '[a-zA-z]+',
    }
from nis import match
import re
from dataclasses import dataclass
from typing import Any
from Constantes import MARCAS_DE_COCHES, FORMATOS_Y_TIPOS

@dataclass
class Coche:
    marca:str
    modelo:str

    def __post_int__(self):
        f_cadenas = Fromateador('Formateador de cadenas', FORMATOS_Y_TIPOS[str],str)
        self.marca = f_cadenas.comprueba_valor(self.marca)
        self.modelo = f_cadenas.comprueba_valor(self.modelo)

        if self.marca.upper() not in MARCAS_DE_COCHES:
            raise ValueError('Marvca de coche no disponible')
@dataclass
class Formateador:
    nombre:str
    regex:str
    tipo:Any
    def comprubea_valor(self,valor):
        marches = re.match(self.regex,valor)
        if not match:
            raise ValueError(f'Formato de "{valor}"incorrecto para {self.tipo}')
        else:
            return match[0]

if __name__ == '__main__':
    while True:
        try:
            marca_coche = input('introduzca la marca del coche: ')
            modelo_coche = input('Introduzca el modelo del coche')
        except ValueError as e:
            print(f'Error{e}')
        except KeyboardInterrupt:
            print('Finalizando programa')
            break
        print()


