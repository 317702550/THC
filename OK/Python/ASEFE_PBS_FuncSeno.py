#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 10/11/19
# 12/11/19
# Python 3.7.3
# Calcula el seno

from math import sin, pi, sqrt
def seno(alfa):
    """ Calcula el seno de \
el ángulo alfa"""
    b = alfa/(2**5)
    for i in range(5):
        c = 2*sin(b)*sqrt(1-sin(b)**2)
        b = 2*b
    resultado = c
    return(resultado)
    
if __name__ == "__main__":
    seno(.5)
    print("Este bloque se ejecuta si el programa \
es llamado desde IDLE, la variable __name__ tiene \
almacenada la cadena '__main__' ")
    print(__name__)
else:
    print("Si el archivo se utiliza como modulo,\
 es decir se importa, la variable __name__ contiene\
el nombre nombre del archivo")
    print(__name__)
