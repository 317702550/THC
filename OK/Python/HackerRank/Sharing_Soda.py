#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 11/11/19
# Python 3.7.3
# Dice cuántos mililitros le quedan al amigo B

n = int(input())
x = 1000 - n - (n//3)
print("%.0f"%(x))
