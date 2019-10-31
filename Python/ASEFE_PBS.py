# Maximiliano Proaño Bernal
# 30/10/19
# 31/10/19
# Python 3.7.3
# Calcula una aproximación de la raíz cuadrada del valor dado

def rc(x):
    b = x
    h = 1
    print("""
Proceso para la raíz de """ + str(x) + ":") # La función str() convierte una variable numérica a forma de texto para poder concatenarlo con más texto
    for i in range(20):
        b_new = (b + h)/2
        h_new = x/b
        b = b_new
        h = h_new
        print("Rectángulo %.0f---%.5f---%.5f"%(i,b,h))
    return("Resultado final: "+str(b))
print(rc(81))
print(rc(95))
print(rc(0.5))
print(rc(0.125))
