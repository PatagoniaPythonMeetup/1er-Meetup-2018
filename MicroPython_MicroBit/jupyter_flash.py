"""
Cargar 
"""
from IPython.core.magic import register_cell_magic
from sh import Command

uflash = Command('uflash')

@register_cell_magic
def grabar(nombre, contenido):
    "Graba un archivo y lo flashea con uFlash"
    
    if not nombre:
        nombre = 'main.py'
    elif not nombre[:-3] != '.py':
        nombre += '.py'

    full_name = '/tmp/{}'.format(nombre)
    with open(full_name, 'wb') as fp:
        fp.write(contenido.encode('utf-8'))
        print("Grabando en Micro:bit")
        uflash(full_name)
    
