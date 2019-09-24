# Maximiliano Proaño Bernal
# Python 3.7.3
# 19/09/12
# 24/09/12
# Ejercicio 01

2 + 2 # Realiza y muestra el reslutado de la suma de 2 más 2
50 - 5*6 # Realiza y muestra el reslutado de la resta de 50 menos el producto de 5 por 6
(50 - 5*6) / 4 # Realiza y muestra el reslutado de la división de la resta de 50 menos el producto de 5 por 6 entre 4
8 / 5 # Realiza y muestra el resultado de dividir 8 entre 5

17 / 3 # Realiza y muestra el resultado de dividir 17 entre 3
17 // 3 # Realiza y muestra el resultado del mayor entero menor o igual al dividir 17 entre 3
17 % 3 # Realiza la divisón 17 entre 3 y muestra el residuo de la división
5 * 3 + 2 # Realiza y muestra el resultado de la suma de 2 más el producto de 5 por 3

5 ** 2 # Realiza y muestra el resultado de elevar 5 al cuadrado
2 ** 7 # Realiza y muestra el resultado de elevar 2 a la séptima potencia
9 ** 0.5 # Realiza y muestra el resultado de sacar raíz cuadrada a 9
2 ** 1/2 # Realiza y muestra el resultado de elevar 2 a la primera potencia y dividirlo entre 2
2 ** (1/2) # Realiza y muestra el resultado de sacar raíz cuadrada a 2

ancho = 20 # Guarda "ancho" con valor de 20
alto = 5 * 9 # Guarda "alto" con valor de 5*9
ancho * alto # Realiza y muestra el resultado de multiplicar ancho por alto

n # Manda error, ya que "n" no está definido

4 * 3.75 - 1 # Realiza y muestra el reslutado de la resta del producto de 4 por 3.75 menos 1

iva = 16/100 # Guarda "iva" con valor de 16/100
precio = 120.5 # Guarda "precio" con valor de 120.5
precio * iva # Realiza y muestra el resultado de multiplicar precio por iva
precio + _ # Realiza y muestra el resultado de sumar precio más el precio por el iva
round(_, 2) # Redondea el resultado anterior a dos decimales

# Cadenas
'una cadena' # Imprime entre comillas simples "una cadena"
'La comilla simple \'' # Imprime entre comillas simples "La comilla simple'"
"\"Si,\" afirmo" # Imprime entre comillas simples " "Si", afirmo "
print("\"Si,\" afirmo") # Imprime " "Si", afrimo "

c = 'Primera linea.\nSegunda linea.' # Guarda "c" como "Primer Linea (salto de renglón) Segunda linea" sin respetar los saltos de lineas
c # Muestra el valor entrecomillado de "c"
print(c) # Imprime la variable "c" con salto de línea debido al \n
len(c) # Muestra el número de caracteres usados, incluyendo espacios

print('Una ruta en windows C:\algun\nombre') # Imprime "Una ruta en windows C:lgun ombre" (/a se representa como  y /n como un salto de linea).
print(r'Una ruta en windows C:\algun\nombre') # Imprime "Una ruta en windows C:\algun\nombre" (r nulifica las propiedades de /a y /n).


print("""\
Uso: ssh [OPCIONES] <usuario>@<servidor>
     -v                 muestra informacion adiciona de la conexion
     -p puerto          Puerto para la conexion segura, 22 es el predeterminado
""") # Imprime lo que se encuentra dentro de las comillas tal cual está 

2 * 'goya ' + 'cachun' # Imprime 2 veces "goya" y agrega una vez "cachun"

'Py' 'thon' # Imprime "Python" todo junto

text = ('Escribe varias cadenas dentro del paréntesis '
        'para tenerlas unidas') # Guarda "text" como 'Escribe varias cadenas dentro del paréntesis para tenerlas unidas"
text # Imprime el valor de "text"

prefijo = 'Py' # Guarda la variable 'prefijo' con el valor 'Py'.
prefijo 'thon' # Guarda la variable 'prefijo' con el valor 'thon'. #????
('un' * 3) 'ium' #?????

prefijo + 'thon' # Muestra la palabra Python entre comillas sencillas.

nombre = "Ada" # Guarda la variable "nombre" con el valor "Ada"
apellido = "Lovelace" # Guarda la variable "apellido" con el valor "Lovelace"

print(nombre.upper()) # Imprime "nombre" con letras mayúsculas "ADA"
print(nombre.lower()) # Imprime "nombre" con letra minúsculas "ada"
print(nombre.isalnum()) # Imprime "True", ya que la variable tiene caracteres alfanumérico.
print(nombre.isalpha()) # Imprime "True", ya que la variable tiene caracteres alfabeticos
print(nombre.islower()) # Imprime "False", ya que no todos los caracteres de la variable son minúsculas.
print(nombre.isnumeric()) # Imprime "False", ya que la variable no es numérica.
print(nombre.isspace()) # Imprime "False", ya que la variable no contiene solamente espacios.
print(nombre.istitle()) # Imprime "True", ya que la varibale contiene caracteres en mayusculas y en minusculas.
asignatura = "Taller De Herramientas Computacionales"
print(asignatura.istitle()) # Imprime "True", ya que la variable contiene caracteres tanto en minusculas como en mayusculas.
print(asignatura.isupper()) # Imprime "False", ya que no todos los caracteres de la varibale son mayusculas.

numero = "1024" # Guarda "numero" como el valor de 1024
vocales = "aeiou" # Guarda "vocales" como "aeiou"
print(numero.isnumeric()) # Analiza si la variable "numero" tiene valor numérico e imprime el resultado (True)
print(vocales.isnumeric()) # Analiza si la variable "vocales" tiene valor numérico e imprime el resultado (False)

pelicula = "2001: UNA MENTE BRILLANTE" # Guarda "pelicula" como "2001: UNA MENTE BRILLANTE"
libro = "Cinco Ecuaciones Que Cambiaron Al Mundo" # Guarda "Libro" como "Cinco Ecuaciones Que Cambiaron Al Mundo"
poema = "nadie en oro se convertirá:" # Guarda "poema" como "nadie en oro se convertirá"
print(pelicula.islower()) # Analiza si la variable "pelicula" está escrita con minúsculas e imprime el resultado (False)
print(pelicula.isupper()) # Analiza si la variable "pelicula" está escrita con mayúsculas e imprime el resultado (True)

print(libro.istitle()) # Analiza si la variable "libro" está escrita en el formato de título imprime el resultado (True)
print(libro.isupper()) # Analiza si la variable "libro" está escrita con mayúsculas e imprime el resultado (False)

print(poema.istitle()) # Analiza si la variable "poema" está escrita en el formato de título imprime el resultado (False)
print(poema.islower()) # Analiza si la variable "libro" está escrita con miníusculas e imprime el resultado (True)

cadena = "Linux es un kernel." # Guarda la variable "Cadena" como "Linux es un kernel."
" ".join(cadena) # Agrega un espacio entre cada caractér, incluyendo espacios
print(cadena) # Muestra la variable "Cadena"
print(" ".join(cadena)) # Muestra la variable "Cadena" con espacios añadidos

print("".join(reversed(cadena))) # Muestra la variable "Cadena" escrita de derecha a izquierda"

# https://docs.python.org/3/tutorial/introduction.html#strings
# https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3
