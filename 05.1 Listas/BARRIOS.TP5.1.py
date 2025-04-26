# Ejercicio 1
lista = []

for items in range(0, 101, 4):
    lista.append(items)

print(lista)

# Ejercicio 2
lista = ["Perro", "Gato", "Pato", "Pinguino", "Cabra"]

print(lista[len(lista) - 2])

# Ejercicio 3
lista = []

lista.append(2)
lista.append("Dos")
lista.append(True)

print(lista)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]

animales[len(animales) - 2] = "loro"
animales[len(animales) - 1] = "oso"

print(animales)

# Ejercicio 5
numeros = [8, 15, 3, 22, 7]

numeros.remove(max(numeros))

print(numeros,"\nLo que hace este programa es crear un lista de numeros, luego con la funcion remove(max()) se elimina el numero mas alto y luego se imprime")

# Ejercicio 6
lista = []

for items in range(10, 31, 5):
    lista.append(items)

print(lista[0:2])

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "golf"
autos[2] = "vento"

print(autos)

# Ejercicio 8
dobles = []

dobles.append(2 * 5)
dobles.append(2 * 10)
dobles.append(2 * 15)

print(dobles)

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

# Ejercicio 10
lista_anidada = [[15], [True], [[25.5], [57.9], [30.6]], [False]]

print(lista_anidada)