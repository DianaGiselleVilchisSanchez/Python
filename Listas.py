# Las listas

# Tipo de dato compuesto que puede almacenar distintos valores
#  (llamados items) ordenados entre [] y separadados con comas

numeros= [1,2,3,4]
print (numeros)

datos = [4, "Una cadena", -15, 3.14, "otra cadena"]
print (datos)

# Indices y Slicing
# Funciona de una forma muy similar a las cadenas de caracteres

datos = datos [-2:]
print(datos)

# Sumar listas
# como resulatado una nueva lista que incluye todos los items.

numeros = numeros + [5, 6, 7, 8]
print (numeros)

# Son modificables
pares = [0, 2, 4, 5, 8, 10]
pares [3]=6
print(pares)

# .append() sirve oara añadir un item al final de la lista

pares.append(12)
print (pares)

pares.append(7*2)
print(pares)

letras = ['a', 'b', 'c', 'd', 'e', 'f']
letritas= letras [:3]
print(letritas)

letras [:3] = ['A', 'B', 'C']
print(letras)

letras [:3] = []
print(letras)

#Funcion Len()
letras =[]
len(letras) 
print(letras)

#Listas anidadas
a = [1,2,3]
b=[4, 5,6]
c=[7, 8, 9]
r= [a, b, c]
print(r)

sub = r [-1] # primer sublista
print(sub)

sub = r [0] [0] #Primera sublista, y de ella, el primer item
print(sub)