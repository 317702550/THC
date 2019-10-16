def Regla30(x,y,z): # x,y,z son los estados de las células respectivamente
    if x == 0:
        if y == 0:
            if z == 0:
                answer = 0
            else:
                answer = 1
        else:
            answer = 1
    else:
        if y == 0:
            if z == 0:
                answer = 1
            else:
                answer = 0
        else:
            answer = 0
    return(answer)

cells = []
for x in range(43):
    list.append(cells,0)
cells[21] = 1
print(cells)

for a in range(22):
    gen1 = []
    for i in range(42):
        list.append(gen1,Regla30(cells[i-1],cells[i],cells[i+1]))
    list.append(gen1,Regla30(cells[41],cells[42],cells[0]))
    cells = gen1
    print(cells)

