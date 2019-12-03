#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 03/12/19
# Python 3.7.3
# Número concatenado

if __name__ == '__main__':
    n = int(input())
def num(k):
    l = [i+1 for i in range(k)]
    return "".join(str(l[t]) for t in range(len(l))) # me salió de pura casualidad pero intentaré comprender bien esta línea :o
print(int(num(n)))
