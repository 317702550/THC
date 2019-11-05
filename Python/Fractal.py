# Maximiliano Proaño Bernal
# 03/11/19
# 05/11/19
# Python 3.7.3
# Fractal de Cantor

import matplotlib.pyplot as plt
def frac(x):
    "Grafica el fractal de Cantor hasta el paso x"
    b = 10
    plt.plot([0,b],[b,b], linewidth = 3.0, color = "b") #linewidth modifica el grosor de la línea que grafica
    plt.draw()
    for t in range(x):
        plt.plot([0,(1/3)*b],[10 - (t + 1),10 - (t + 1)], linewidth = 3.0, color = "b")
        plt.plot([10 - ((1/3)*b),10],[10 - (t + 1),10 - (t + 1)], linewidth = 3.0, color = "b")
        plt.draw()
        b = (1/3)*b
    b = 10
    c = b/3
    d = (2*b)/3 
    plt.plot([0,b],[b,b],linewidth = 3.0, color = "b")
    for i in range (x):
        plt.plot([0,c],[10-(i+1),10-(i+1)], linewidth = 3.0, color = "b")
        plt.plot([d,b],[10-(i+1),10-(i+1)], linewidth = 3.0, color = "b")
        plt.draw()
        b = b/3
        c = b/3
        d = (2*b)/3
        plt.draw()
    plt.show()
frac(7)

# Fue lo mejor que pude hacer profe :c
