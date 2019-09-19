# Maximiliano Proaño Bernal
# Figuras inscritas en un una circunferencia
# de radio 5
# 17/09/19
# 19/09/19

# Coordenadas del triángulo inscrito en la circunferencia de radio 5
from math import sqrt, cos, sin, pi # se importarán del módulo math raíz, coseno, seno y pi
r = 5
L = 3
a = (2*pi)/L
x = r*cos(a)
y = r*sin(a)
c = r*cos(2*a)
d = r*sin(2*a)
e = r*cos(3*a)
f = r*sin(3*a)

A = (x,y)
B = (c,d)
C = (e,f)

print("""La coordenadas del triángulo inscrito en la circunferencia de radio
5 son:
A(%.2f,%.2f)
B(%.2f,%.2f)
C(%.2f,%.2f)"""%(x,y,c,d,e,f))
