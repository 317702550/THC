#!/usr/bin/python3
# Maximiliano Proaño Bernal
# Python 3.7.3
# 
# Calcula y grafica las evoluciones de las células

import matplotlib.pyplot as plt
def Regla30(x,y,z): # x,y,z son los estados de las células respectivamente
    if x == 0:
        if y == 0:
            if z == 0:
                answer = 0
            else:
                answer = 1
        else:
            answer = 1
    else:
        if y == 0:
            if z == 0:
                answer = 1
            else:
                answer = 0
        else:
            answer = 0
    return(answer)

cells = []
for x in range(43):
    cells.append(0)
cells[21] = 1
print(cells)
for c in cells:
    if c == 1:
        plt.plot([21],[23],"co")

for a in range(22,0,-1):
    gen1 = []
    for i in range(42):
        gen1.append(Regla30(cells[i-1],cells[i],cells[i+1]))
    gen1.append(Regla30(cells[41],cells[42],cells[0]))
    cells = gen1
    print(cells)
    e = []
    n = len(cells)
    for v in range(n):
        if cells[v] == 1:
            e.append(v)
            
    z = len(e)
    for m in range(z):
        plt.plot([e[m]],[a],"co")

#plt.plot([1],[2],"ro")
#plt.axis([0,22,0,22])
plt.show()
