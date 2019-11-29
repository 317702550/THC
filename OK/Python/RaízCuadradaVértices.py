#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 25/11/19
# Python 3.7.3
# Calcula una aproximación de la raíz cuadrada del valor dado y grafica el cuadrado correspondiente

import matplotlib.pyplot as plt
def rc(x):
    b = x
    h = 1
    print("""
Proceso para la raíz de """ + str(x) + ":") # La función str() convierte una variable numérica a forma de texto para poder concatenarlo con más texto
    for i in range(1,9):
        b = (b + h)/2
        h = x/b
        print("Rectángulo %.0f---%.5f---%.5f"%(i,b,h))
        plt.plot([0,b],[0,0],linewidth = 1.5, color = "c")
        plt.plot([0,b],[h,h],linewidth = 1.5, color = "b")
        plt.plot([0,0],[0,h],linewidth = 1.5, color = "b")
        plt.plot([b,b],[0,h],linewidth = 1.5, color = "c")
        plt.show()
        print("""
\draw (0,0) -- (0,%.0f) -- (%.0f,%.0f) -- (%.0f,0) -- (0,0);
\\filldraw[black] (2.3,.2) circle (0pt)
node[anchor=west] {$\\frac{b+h}{2}$};        
\\filldraw[black] (5,.5) circle (0pt)
node[anchor=west] {$\\frac{x}{b}$};"""%(b,h,b,h))
        print("____________________________________")
    return("Resultado final: "+str(b))
print(rc(81))
#print(rc(95))
#print(rc(0.5))
#print(rc(0.125))

