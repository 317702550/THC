# Maximiliano Proaño Bernal, Antonino Equihua
# Triángulo equilátero de lado 2
# con un vértice en el origen en
# el cuadrante I y un lado sobre el eje x

# Coordenadas del triángulo:
from math import sqrt
a = 0
b = 0
c = a+2
d = b
e = c/2
f = sqrt((2**2)-(e**2))

A = (a,b)
B = (c,d)
C = (e,f)

print("""Las coordenadas del triángulo equilátero de
lado 2 con vértice en el origen en
cuadrante I y un lado sobre el eje de las x son A = (a=%g, b=%g),
B = (c=%g, d=%g), C=(e=%g, f=%g)"""%(a,b,c,d,e,f))

# Cuadrado de lado 2 con vértice en el origen 
# en el primer cuadrante y un lado sobre el eje de las x

# Coordenadas del cuadrado:
a = 0
b = 0
c = a+2
d = b
e = c
f = d+2
g = 0
h = b+2

A = (a,b)
B = (c,d)
C = (e,f)
D = (g,h)
print("""Las coordenadas del cuadrado de
lado 2 con vértice en el origen en
cuadrante I y un lado sobre el eje de las x son A = (a=%g, b=%g),
B = (c=%g, d=%g), C=(e=%g, f=%g), D = (g=%g, h=%g)"""%(a,b,c,d,e,f,g,h))

# Paralelogramo de lados 2 y 2sqrt(2) con vértice en el origen 
# en el primer cuadrante y un lado 2 sobre el eje de las x
a = 0
b = 0
c = a+2
d = b
e = 2*c
f = 2*sqrt(2)
g = c
h = 2*sqrt(2)

A = (a,b)
B = (c,d)
C = (e,f)
D = (g,h)
print("""Las coordenadas del paralelogramo de lados 2 y 2sqrt(2) con vértice en
el origen, en el primer cuadrante y un lado 2 sobre el eje de las x son A = (a=%g, b=%g),
B = (c=%g, d=%g), C=(e=%g, f=%g), D = (g=%g, h=%g)"""%(a,b,c,d,e,f,g,h))

# Rectángulo de base 6 y altura 2 con vértice en el origen 
# en el primer cuadrante y un lado 6 sobre el eje de las x
a = 0
b = 0
c = a+6
d = b
e = a+6
f = d+2
g = 0
h = b+2

A = (a,b)
B = (c,d)
C = (e,f)
D = (g,h)
print("""Las coordenadas del rectángulo de base 6 y altura 2 con vértice en
el origen, en el primer cuadrante y un lado 6 sobre el eje de las x son A = (a=%g, b=%g),
B = (c=%g, d=%g), C=(e=%g, f=%g), D = (g=%g, h=%g)"""%(a,b,c,d,e,f,g,h))

