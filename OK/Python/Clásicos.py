#!/usr/bin/python3
# Fecha de entrega: 13:00
# Python, implementación de funciones
# 10 puntos
# Luis Enrique Serrano 14 oct.
# El archivo Clasicos.py contiene las características para que implemente varias funciones y refuercen los elementos vistos de python.
# Clasicos.py
# Texto
# BuscarErrores.py
# Texto
# Comentarios de la clase
# Tu trabajo
# Tarea asignada
# Comentarios privados

'''

    Algunos ejercicios clasicos

'''

def celciusAfahrenheit(c):
    resultado = ((9*c)/5) + 32
    return(resultado)
print(celciusAfahrenheit(37))
print("----------------")


def fahrenheitAcelcius(f):
      resultado = (5/9)*(f - 32)
      return(resultado)
print(fahrenheitAcelcius(98.6))
print("----------------")
def alturaY(y):
    '''
Considerando la ecuacion
y(t)= v0*t - 1/2*g*t**2
implementar una funcion que dada una altura yc
muestre el tiempo que tardo la pelota en llegar a yc
'''
    
print("----------------")

# En los siguientes ejercicios se tiene que definir la funcion
# de principio a fin, es decir; desde definir el nombre y los datos de entrada
# hasta determinar si la funcion debe regresar algun valor o no(datos de salida)
'''
Implementar una funcion que convierta segundos a años
por ejemplo, un billon de segundos a años
'''
def SegAños(s):
    answer = s/60/60/24/365
    return(answer)
print(SegAños(1000000000000))
print(SegAños(599184000))
print("----------------")
'''
Implementar una funcion que convierta años a segundos
por ejemplo, un 16 años a segundos
'''
def AñosSeg(a):
    answer = a*365*24*60*60
    return(answer)
print(AñosSeg(16))
print(AñosSeg(19))
print("----------------")
'''
Convertir metros a pulgadas
'''
def MetPul(m):
    answer = m*254
    return(answer)
print(MetPul(1.69))
print(MetPul(0.135))
print("----------------")
'''
convertir metros a pies
'''
def MetPies(r):
    answer = r*0.0328
    return(answer)
print(MetPies(20))
print("----------------")
'''
convertir metros a yardas
'''
print("----------------")
'''
convertir metros a millas
'''
def MetMill(w):
    answer = w*1609
    return(answer)
print(MetMill(22))
print("----------------")
'''
Dados los numeros a y b mostrar
el desarrollo de
(a + b)^2
(a - b)^2
'''
def Binomio(a,b):
    answer1 = a**2 + 2*a*b + b**2
    answer2 = a**2 - b**2
    return(answer1,answer2)
print(Binomio(3,4))
print("----------------")
'''
Dados los coeficientes de una ecuacion cuadratica
de segundo grado en una variable (a,b,c) mostrar
las racies r1 y r2 de la ecuacion
'''
print("----------------")


##########
# Verificar que los siguientes bloques de codigo
# funcionen, en caso de no hacerlo
# corregirlos (depurarlos)
#

# programa 1
from math import sin, cos, pi
x = pi/4
val = (sin(x))**2 + (cos(x))**2
print(val)

# programa 2
A = 3
B = 2
C = A + B
print(C)


##########
# Buscar errores del en el archivo con nombre
#   BuscarErrores.py
# comentar que es lo que esta mal en cada linea


'''

    Recuerden:

/  es la division flotante
// es la division entera
%  es el modulo

no olviden dejar un espacio cuando utilicen
los operadores aritmeticos +, - y con el
de asignacion =

no utilicen espacios cuando utilicen los
operadores *, / y **


un igual es asignacion, dos iguales son comparacion
.git es el directorio con el que no hay que "meterse"

y finalmente:
"los peces son amigos, no comida"
(bueno esta no creo que sea muy util pero me acorde :) )

'''


