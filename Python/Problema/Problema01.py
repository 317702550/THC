# Maximiliano Proaño Bernal
# Python 3.7.3
# 10/09/19
# 12/09/19
#
# Calcula la energía cinética de un tren con masa 500
# toneladas y velocidad 80 m/s
def mult(a,b):
    answer = a*b
    return(answer)

v0 = 80
m = 500000
Ec = (m*v0**2)/2
print(Ec)
print("------------")
ListEc = []
VelIni = [390,120,30,425,19,34]
Masas = [150000, 40000,10250]
for v0 in VelIni:
    for m in Masas:
        Ec = mult(v0,m)
        list.append(ListEc,Ec)
        print("""La energía cinética de tren con velocidad %.0f m/s y masa %.0f
kg es de %.0f Joules"""%(v0,m,Ec))
        print("------------")
print("""El máximo de las energías cinéticas de todos los trenes es de
%.0f Joules"""%(max(ListEc)))
print("""El mínimo de las energías cinéticas de todos los trenes es de
%.0f Joules"""%(min(ListEc)))
