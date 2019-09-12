#
# Maximiliano Proaño Bernal
# Python 3.7.3
# 10/09/19
# 12/09/19
#
# Calcula la posición de una pelota con una velocidad inicial
# de 5 m/s y un tiempo de 0.6 segundos
v0 = 5
g = 9.81
t = 0.6
y = v0*t-0.5*g*t**2
print(y)
print("En el tiempo t=%g segundos, la altura de la pelota es %.2f metros"%(t,y))
print("""En el tiempo t=%g segundos, la altura de \nla pelota es %.2f metros"""%(t,y))
print("""
En el tiempo t=%g segundos, la pelota con velocidad=%.3E m/s, la altura de
la pelota es %.2f metros"""%(t,v0,y))

