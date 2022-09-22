#from modulo import* #no es recomendable ya que ocasiona colisiones con declaraciones futuras para los modulos

__all__ = ['hola_mundo']

def hola_mundo():
    return 'hola mundito'

def str(cdn):
    return cdn[0]


def primer_funcion(a):
   cadena = str (a)
   return ' '.join([hola_mundo(),cadena])

if __name__ == '__main__':
    print(primer_funcion('gato'))





