#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 26/11/19
# Python 3.7.3
# Calcula el estado del paciente
a = input()
p = a.count("lol") + 2*(a.count("rofl")) + 3*(a.count("lmao")) + 4*(a.count("lel"))
print(p)
if 1 <= p <= 5:
    print("Patient has bright red face")
elif 5 < p <= 12:
    print("Patient is unable to speak")
elif 12 < p <= 20:
    print("Patient's sides are mildly bruised")
elif 20 < p <= 30:
    print("Patient has broken jaw, fractured ribs")
elif 30 < p <= 40:
    print("Patient is in a coma")
else:
    print("Patient is dead")
