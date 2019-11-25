#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 29/10/19
# Python 3.7.3
# Suma los primeros n dígitos
n = int(input())
if n > 100 or n < 1:
    print("Only values between 1 and 100")
else:
    ans = sum(range(n+1))
print(ans)
