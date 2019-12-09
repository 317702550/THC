#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 28/11/19
# Python 3.7.3
# Crea el laberinto en formato de lista

import sys
print(sys.argv)
#print(sys.argv[1])
#print(len(sys.argv))

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
if len(sys.argv) == 1:
    nombreLaberinto = "L1.txt"
else:
    nombreLaberinto = sys.argv[1]
l = cargaLaberinto(nombreLaberinto)
print(l)

from prettytable import PrettyTable
p = PrettyTable()

for renglon in l:
    p.add_row(renglon)

print(p.get_string(header=False, border=False))

def avanza(L,i,j,s):
    if L[i-1][j] == 0:
        L[i-1][j] == 2
        s.append([i-1,j])
        avanza(L,i-1,j,s)
    elif L[i][j+1] == 0:
        L[i][j+1] == 2
        s.append([i,j+1])
        avanza(L,i,j+1,s)
    elif L[i+1][j] == 0:
        L[i+1][j] == 2
        s.append([i+1,j])
        avanza(L,i+1,j,s)
    elif L[i][j-1] == 0:
        L[i][j-1] == 2
        s.append([i,j-1])
        avanza(L,i,j-1,s)
    return(s)
