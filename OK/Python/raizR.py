#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 21/11/19
# Python 3.7.3
# Calcula la raíz cuadrada de forma recursiva

from math import fabs
def raizR(b,h,x,e,i):
    if fabs(b-h) > e:
        print(b,h)
        return(raizR((b+h)/2,x/((b+h)/2),x,e,i+1))
    else:
        print("fin")
        return [b,i]

def raiz(x):
    return(raizR(9,1,9,0.00001,0))

print(raizR(9,1,9,0.00001,0))
print(raiz(9))
[r,y] = raiz(9)
print(r)
print(y)
