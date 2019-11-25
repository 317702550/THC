#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 29/10/19
# Python 3.7.3
# Te dice la calificación en letra según tu promedio
n = int(input())
if n < 0 or n > 100:
    print("Only values between 0 and 100 inclusive")
else:
    if 0 <= n <= 59:
        print("F")
    if 60 <= n <= 69:
        print("D")
    if 70 <= n <= 79:
        print("C")
    if 80 <= n <= 89:
        print("B")
    if 90 <= n <= 100:
        print("A")
