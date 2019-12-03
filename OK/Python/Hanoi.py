#!/usr/bin/python
# Maximiliano Proaño Bernal
# 02/12/19
# Python 3.7.3
# Programa copiado de internet que calcula la solución de las torres de Hanoi

def hanoi(N, inc='1', temp='2', fin='3'): # en este caso N es el número de discos, inc es la torre 1 (el inicio), temp es la torre 2 (la torre "ancla"), fin es la torre 3 (el fin)
    if N > 0:
        hanoi(N-1, inc, fin, temp) # se llama de forma recursiva a la función
        print ('se mueve de torre', inc, 'a torre', fin)
        hanoi(N-1, temp, inc, fin)
discos = int(input("Ingresa el numero de discos:"))
hanoi(discos)
