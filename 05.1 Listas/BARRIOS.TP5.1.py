# Ejercicio 1
# Se crea lista
lista = []

# Loop for in range para vaya de 4 en 4 (es decir los multiplos de 4)
for items in range(4, 101, 4):
    lista.append(items)

# Se imprime la lista
print(lista)

# Ejercicio 2
# Se crea lista
lista = ["Perro", "Gato", "Pato", "Pinguino", "Cabra"]

# Se imprime el penultimo elemento de la lista
print(lista[len(lista) - 2])

# Ejercicio 3
# Se crea la lista
lista = []

# Se agregan los tres elementos
lista.append(2)
lista.append("Dos")
lista.append(True)

# Se imprime la lista
print(lista)

# Ejercicio 4
# Se crea la lista de animales
animales = ["perro", "gato", "conejo", "pez"]

# Se cambian los ultimos dos elementos utilizando len para que siempre sean los ultimos dos elementos
animales[len(animales) - 2] = "loro"
animales[len(animales) - 1] = "oso"

# Se imprime la lista
print(animales)

# Ejercicio 5
# Se crea la lista de numeros
numeros = [8, 15, 3, 22, 7]

# Se remueve el numero mas alto
numeros.remove(max(numeros))

# Se imprime lista y explicacion
print(numeros,"\nLo que hace este programa es crear un lista de numeros, luego con la funcion remove(max()) se elimina el numero mas alto y luego se imprime")

# Ejercicio 6
# Se crea lista
lista = []

# Loop for in range para poner los elementos entre 10 y 30 en 5 en 5
for items in range(10, 31, 5):
    lista.append(items)

# Se imprimen solo los dos primeros elementos
print(lista[0:2])

# Ejercicio 7
# Se crea lista de autos
autos = ["sedan", "polo", "suran", "gol"]

# Se cambian los elementos del centro
autos[1] = "golf"
autos[2] = "vento"

# Se imprime la lista
print(autos)

# Ejercicio 8
# Se crea lista
dobles = []

# Se agregan los elementos multiplicados por dos
dobles.append(2 * 5)
dobles.append(2 * 10)
dobles.append(2 * 15)

# Se imprime la lista
print(dobles)

# Ejercicio 9
# Se crea la lista anidada de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# Se modifican sus elementos
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

# Se imprime la lista
print(compras)

# Ejercicio 10
# Se crea la lista anidada
lista_anidada = [[15], [True], [[25.5], [57.9], [30.6]], [False]]

# Se imprime la lista
print(lista_anidada)