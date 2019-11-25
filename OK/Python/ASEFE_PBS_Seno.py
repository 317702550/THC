#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 11/11/19
# 12/11/19
# Python 3.7.3
# Calcula el seno del ángulo a

from math import pi, sin, sqrt
a = 0.1
b = a/(2**5)
print("""
Para a = 0.1:""")
for i in range(5):
    c = 2*sin(b)*sqrt(1-sin(b)**2)
    print("Paso %.0f: sin(%.5f) = %.5f"%(i+1,2*b,c))
    b = 2*b

a = 0.5
b = a/(2**5)
print("""
Para a = 0.5:""")
for i in range(5):
    c = 2*sin(b)*sqrt(1-sin(b)**2)
    print("Paso %.0f: sin(%.5f) = %.5f"%(i+1,2*b,c))
    b = 2*b

a = 1.5
b = a/(2**5)
print("""
Para a = 1.5:""")
for i in range(5):
    c = 2*sin(b)*sqrt(1-sin(b)**2)
    print("Paso %.0f: sin(%.5f) = %.5f"%(i+1,2*b,c))
    b = 2*b

a = pi
b = a/(2**5)
print("""
Para a = pi:""")
for i in range(5):
    c = 2*sin(b)*sqrt(1-sin(b)**2)
    print("Paso %.0f: sin(%.5f) = %.5f"%(i+1,2*b,c))
    b = 2*b

