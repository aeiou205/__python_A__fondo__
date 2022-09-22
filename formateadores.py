from platform import python_branch
from re import S
from Clases import Formateador
MARCAS_DE_COCHES = ['HONDA', 'MANZANA', 'TOYOTA']

FORMATOS_Y_TIPOS = {
    int : '\d+',
    str : '[a-zA-z]+',
    }




FORMATEADORES ={
    int: Formateador('Formateador de enteros',
    FORMATOS_Y_TIPOS[int]),
    str:Formateador('Formateador de cadenas', FORMATOS_Y_TIPOS[str]),
    }
 

