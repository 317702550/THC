def Regla30(x,y,z):
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
cells[22] = 1

gen = []  
for c in cells:
    print(cells.index(c,0,44))
