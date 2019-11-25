#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 08/10/19
# Python 3.7.3
# Calcula el polen según el número de abejas en la lista
acumulado = 0
numero_veces = [7,8,16,9,13,6,4]

for i in range(len(numero_veces)):
    if numero_veces[i]>=10:
        acumulado = acumulado + numero_veces[i]*3+18.5
    else:
        acumulado = acumulado + numero_veces[i]*2/7+2.1

numero_veces1 = [41,65,89,74,85,4,6,6,4,7,8,5,4,1,2,4,4,77,85,96,12,45]

def totalPolen(numero_veces):
    acumulado = 3
    for i in range(len(numero_veces)):
        if numero_veces[i]>=10:
            acumulado = acumulado + numero_veces[i]*3+18.5
        else:
            acumulado = acumulado + numero_veces[i]*2/7+2.1
    return(acumulado)
print(totalPolen(numero_veces))
print(totalPolen(numero_veces1))
