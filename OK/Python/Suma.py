# !/usr/bin/python3
# Maximiliano Proaño Bernal
# 14/11/19
# Python 3.7.3
# Funciones que calculan la suma de los primeros n dígitos

def suma1(n):
    return((n*(n+1))/2)

def suma2(n):
    if n == 1:
        return(n)
    else:
        return(n + suma2(n-1))

def suma3(n):
        l = [i for i in range(n+1)]
        return(sum(l))
    
def suma4(n):
    if n == 1:
        return(n)
    else:
        
