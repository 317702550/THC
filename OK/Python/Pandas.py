import pandas as pd

""" El primer ejemplo que vamos a poner va a ser el de definir una estructura de datos "Series" que como ya comentamos
es un array de datos unidimensional con idexación. Las "Series" se definen de la siguiente manera:serie = pd.Series(data, index=index)
Es decir, que en el primer parámetro le indicamos los datos del array y en el segundo parámetro los índices.

Aqui un ejemplo.
"""
index=[1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7]
JugadoresEspañoles = pd.Series(
    ['Casillas', 'Ramos', 'Pique', 'Puyol', 'Capdevila', 'Xabi Alonso', 'Busquets', 'Xavi Hernandez', 'Pedrito',
     'Iniesta', 'Villa'],index)
print("------")
print ("Jugadores Españoles De Futbol: \n%s" % JugadoresEspañoles)
print("------")

"""  En este siguiente caso; en el que no le indiquemos los índices de forma explícita, no generará los índices
de forma automática empezando desde el valor cero:
"""
JugadoresEspañoles= pd.Series(
    ['Casillas', 'Ramos', 'Pique', 'Puyol', 'Capdevila', 'Xabi Alonso', 'Busquets', 'Xavi Hernandez', 'Pedrito',
    'Iniesta', 'Villa'])
print ("Jugadores Españoles De Futbol: \n%s" % JugadoresEspañoles)

"""También podemos crearnos una estructura de datos "Series" a partir de una lista o de un diccionario.
Si la construimos a partir de una lista nos pondrá los índices por defecto y si lo creamos a partir de un diccionario, pondrá como
índices las claves. Vamos en este ejemplo a que me refiero y tambien, de como crear una Serie a partir de un diccionario y además
vamos a ver como insertar en esta serie un nuevo elemento:

Aqui el ejemplo.
"""
Jugadores = {1: 'Casillas', 15: 'Ramos', 3: 'Pique', 5: 'Puyol', 11: 'Capdevila', 14: 'Xabi Alonso',
               16: 'Busquets', 8: 'Xavi Hernandez', 18: 'Pedrito', 6: 'Iniesta', 7: 'Villa'}
Jg= pd.Series(Jugadores)
#Insert new player
Jg[10] = 'Isco'
print ("Jugadores Españoles: \n%s" % Jg)

""" Vamos a pasar a continuación a ver un ejemplo con la estructura de datos "DataFrame".
Como ya se ha comentado es una estructura de datos similar a una tabla de una base de
datos relacionar, una tabla de excel, etc.

Para construir un DataFrame se puede hacer de diferentes formas, como por ejemplo a partir de una lista, de un diccionario,
de una Serie,de otro DataFrame, leyendo una tabla excel, csv, etc. Vamos a ver a continuación como construiríamos un DataFrame.

Aqui el ejemplo.
"""
JugadoresEspañoles = pd.DataFrame(
    {
        'Nombre': ['Casillas', 'Ramos', 'Pique', 'Puyol', 'Capdevila', 'Xabi Alonso', 'Busquets', 'Xavi Hernandez',
                 'Pedrito', 'Iniesta', 'Villa'],
        'Posicion': ['Portero', 'Lateral Derecho', 'Defensa Central', 'Defensa Central', 'Lateral Izquierdo', 'Defensor De Medio Campo',
                    'Defensor De Medio Campo', 'Mediocampista', 'Extremo Izquierdo', 'Extremo Derecho','centro delantero'],
        'Equipo': ['Real Madrid', 'Real Madrid', 'FC Barcelona', 'FC Barcelona', 'Villareal', 'Real Madrid',
                 'FC Barcelona', 'FC Barcelona', 'FC Barcelona', 'FC Barcelona', 'FC Barcelona']
    }, columns=['Nombre', 'Posicion', 'Equipo'],index=[1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7])

print(JugadoresEspañoles)
