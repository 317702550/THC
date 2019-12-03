#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 02/12/19
# Python 3.7.3
# Fractal de Peano

import matplotlib.pyplot as plt
def fr(x):
  l = []
  for i in range(x):
    l.append(0)
    l.append(1)
  return(l)

plt.plot(fr(4))
plt.show()

