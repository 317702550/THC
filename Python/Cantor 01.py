# Maximiliano Proaño Bernal
# 03/11/19
# 05/11/19
# Python 3.7.3
# Fractal de Cantor
import matplotlib as plt
def frac(x):
    def div(a,b):
        c = a + (1/3)*(b-a)
        d = a + (2/3)*(b-a)
        return([[a,c],[d,b]])
    t0 = div(0,1)
    #print(t0)
    #print("-------------------")
    for i in range(x):
        tn = []
        for t in t0:
            [r1,r2] = div(t[0],t[1])
            tn.append(r1)
            tn.append(r2)
        #print(tn)
        #print("-------------------")
        t0 = tn.copy()
    
