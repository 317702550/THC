#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 28/11/19
# Python 3.7.3
# Crea el laberinto en formato de lista

def cargaLaberinto(laberinto):
    archivo = open(laberinto,"r")
    l = []
    l1 = " "
    while l1:
        l1 = archivo.readline()
        if l1:
            l1 = [int(x) for x in list(l1.strip())]
            l.append(l1)
    return(l)
l = cargaLaberinto("LMaximiliano.txt")
print(l)
