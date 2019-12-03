#!/usr/bin/python3
# Maximilano Proaño Bernal, Antonino Equihua Lombera
# 10/10/19
# Python 3.7.3
# Define las diferentes funciones dadas
"""
Funciones definidas por el usuario
"""
def vabs(x):
    '''Regresa el valor absoluto del numero x.
Regresa  x si x es mayor que cero
Regresa -x si x es menor que cero
'''
    if x >= 0:
        resultado = x
    else:
        resultado = -x
    return(resultado)
print(vabs(-3))
print(vabs(5))
print("-----------------")
def signo(x):
    '''Regresa el signo del numero x.
Regresa  1 si x es positivo
Regresa  0 si x es cero
Regresa -1 si x es negativo
'''
    if x > 0:
        resultado = 1
    else:
        if x < 0:
            resultado = -1
        else:
            resultado = 0
    return(resultado)
print(signo(-5))
print(signo(0))
print(signo(7))
print("-----------------")
def multiplica(a,b):
    '''Regresa el resultado de multiplicar
    el numero a por el numero b
'''
    resultado = a*b
    return(resultado)
print(multiplica(2,3))
print(multiplica(-3,9))
print("-----------------")
def elMayor(a,b):
    '''Regresa el mayor de los numeros: a, b
'''
    if a < b:
        resultado = b
    else:
        resultado = a
    return(resultado)
print(elMayor(35,230))
print(elMayor(-2222,894))
print(elMayor(0.6,0.601))
print("-----------------")
def elMenor(a,b):
    '''Regresa el menor de los numeros: a, b
'''
    if a < b:
        resultado = a
    else:
        resultado = b
    return(resultado)
print(elMenor(35,230))
print(elMenor(-2222,894))
print(elMenor(0.6,0.601))
print("-----------------")
def rectangular(x):
    '''Regresa la evaluacion de x en
la funcion definida como:
Regresa 0   si |x| > 1/2
Regresa 1/2 si |x| = 1/2
Regresa 1   si |x| < 1/2
'''
    if vabs(x) > 1/2:
        resultado = 0
    else:
        if vabs(x) < 1/2:
            resultado = 1
        else:
            resultado = 1/2
    return(resultado)
print(rectangular(0.9))
print(rectangular(-0.4))
print(rectangular(0.5))
print("-----------------")
def identidad(x):
    '''regresa la identidad del valor x
'''
    resultado = x
    return(resultado)
print(identidad(1000))
print(identidad(150.00009))
print(identidad(-0.8))
print("-----------------")
def rampa(x):
    '''Regresa 0 si x < 0
Regresa x si x >= 0
'''
    if x >= 0:
        resultado = x
    else:
        resultado = 0
    return(resultado)
print(rampa(4))
print(rampa(0))
print(rampa(-5))
print("-----------------")
def parte_entera(x):
    ''' Regresa la parte entera de x,
por ejemplo si x = 9.23 regresa 9
'''
    resultado = x//1
    return(resultado)
print(parte_entera(9.23))
print(parte_entera(3.43))
print(parte_entera(7))
print("-----------------")
def enteroMayor(x):
    '''Regresa el entero mayor de x
ej, si x = 7.1 regresaria 8
'''
    if x == x//1:
        resultado = x
    else:
        resultado = (x//1)+1
    return(resultado)
print(enteroMayor(8.001))
print(enteroMayor(9))
print(enteroMayor(6.89))
print("-----------------")
def enteroMenor(x):
    '''Regresa el entero meno de x
ej, si x = 7.1 regresaria 7
'''
    resultado = x//1
    return(resultado)
print(enteroMenor(8.93))
print(enteroMenor(9.43))
print(enteroMenor(5))
print("-----------------")
def parte_fraccionaria(x):
    ''' Regresa la parte fraccionaria de x definida como
x - enteroMenor(x)
ej, si x = 9.23 regresaria:
    9.23 - floor(9.23) = 9.23 - 9
regresa 0.23
ej, si x = -7.26 regresaria:
    -7.26 - floor(-7.26) = -7.26 - (-8) = -7.26 + 8
regresa 0.74
'''
    resultado = x - enteroMenor(x)
    return(resultado)
print(parte_fraccionaria(8.23))
print(parte_fraccionaria(7.35))
print(parte_fraccionaria(9.82))
print("-----------------")
def ulam(n):
    '''Regresa n/2 si n es par
Regresa 3*n + 1 si n es impar
'''
    if n/2==enteroMenor(n/2):
        resultado = n/2
    else:
        resultado = 3*n + 1
    return(resultado)
print(ulam(3))
print(ulam(8))
print(ulam(0))

def prom():
    """Calcula el promedio
de tus calificaiones"""
    l = []
    p = "Si"
    while p == "Si":
        print("Ingrese la calificación")
        x = float(input())
        l.append(x)
        print("¿Desea agregar otra calificación?")
        p = str(input())
    R = sum(l)/len(l)
    return(print("Su cailificación es: " + str(R)))
prom()