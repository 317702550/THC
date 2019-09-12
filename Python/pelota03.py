#
# Maximiliano Proaño Bernal
# Python 3.7.3
# 12/09/19
#
# Calcula la posición de la pelota con una velocidad inicial
# de 5 m/s y un tiempo de 0.6 segundos utilizando nombres de variables
# descriptivos pero muuuuy largos

velocidad_inicial = 5
constante_de_gravedad = 9.81
TIEMPO = 0.6
PosiciónVerticalDeLaBola = velocidad_inicial*TIEMPO-0.5*constante_de_gravedad*TIEMPO**2
print(PosiciónVerticalDeLaBola)

# Apesar de que funciona, es ortodoxo ya que es fácil equivocarse
