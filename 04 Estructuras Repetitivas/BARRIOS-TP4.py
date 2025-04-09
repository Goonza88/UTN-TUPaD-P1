import random

# Ejercicio 1
# Loop que arranca en 0 y termina en 100
for i in range(101): 
    print(i)

# Ejercicio 2
# Pido un numero, lo paso a string, me fijo la longitud y lo muestro
num = int(input("Por favor ingrese un numero entero: "))
num = len(f"{num}")
print(f"El numero ingresado tiene {num} digitos.")

# Ejercicio 3
# Pido lo dos numeros
num1 = int(input("Por favor ingrese un numero entero: "))
num2 = int(input("Por favor ingrese otro numero entero: "))

# Pongo condicionales para cuando el primer numero es mayor que el segundo, y cuando el segundo es mayor que el primero
if num1 < num2:
    num1 = num1 + 1
    num2 = num2 - 1
    tot1 = num1
    # Loop para sumar los numeros entre ambos
    while num1 < num2:
        num1 += 1
        tot1 = tot1 + num1
    print(f"La suma de los numeros entre esos dos es {tot1}.")
elif num1 > num2:
    num1 = num1 - 1
    num2 = num2 + 1
    tot2 = num2
    while num1 > num2:
        num2 += 1
        tot2 = tot2 + num2 
    print(f"La suma de los numeros entre esos dos es {tot2}.")
else:
    print(f"La suma de los numeros entre esos dos es 0")

# Ejercicio 4
stop = 1
tot = 0
# Loop que para cuando el usuario ingresa el 0
while stop != 0:
    stop = int(input("Ingrese un numero para sumar. Si quiere terminar de sumar, presione 0: "))
    # Se suman todos los numeros ingresados y luego se muestra el total
    tot += stop
print(f"El total de las sumas es {tot}.")

# Ejercicio 5
# Genero un numero aleatorio entre 0 y 9 y luego pido un numero al usuario
num1 = random.randint(0, 9)
num2 = int(input("Adivina el numero entre 0 y 9!: "))
tot = 1
# Loop hasta que el usuario ponga el numero correcto y luego muestra la cantidad de intentos
while num1 != num2:
    tot += 1
    num2 = int(input("Ese no es, ingresa otro!: "))
print(f"Bien hecho! Te llevo {tot + 1} intentos!")

# Ejercicio 6
n = 100
# Loop hasta que 100 sea 1, mostrando los numeros pares
while n != 1:
    n -= 1
    if n % 2 == 0:
        print(n)

# Ejercicio 7
# Pido numero al usuario
num = int(input("Por favor ingrese un numero: ")) - 1
tot = 0
# Loop desde 0 hasta el numero que ingreso el usuario - 1 y los suma entre ellos
for i in range(num):
    i += 1
    tot = tot + i
print(f"La suma de todos los números comprendidos entre 0 y {num + 1} es {tot}.")

# Ejercicio 8 
suma = 0
pares = 0
impares = 0
positivos = 0
negativos = 0
# Loop que para cuando llega a 100 numeros pedidos
while suma != 100:
    num = int(input("Ingrese un numero: "))
    # Condicionales que suman segun el numero y luego muestra los resultados
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1
    num = 0
    suma += 1
print(f"De los numeros ingresados: \nPares: {pares}.\nImpares: {impares}.\nPositios: {positivos}.\nNegativos: {negativos}.")

# Ejercicio 9
suma = 0
tot = 0
# Loop que para cuando llega a 100 numeros pedidos, suma los numeros y luego divide por la cantidad de numeros ingresados
while suma != 100:
    num = int(input("Ingrese un numero: "))
    tot += num
    suma += 1
print(f"La media entre los numeros ingresados es {tot / suma}")

# Ejercicio 10
# Pide un numero para ser invertido
num = int(input("Ingrese un numero: "))
inv = 0
# Loop hasta que el numero llega a 0
while num > 0:
    # Toma el resto 
    digito = num % 10
    # Agregas el ultimo digito como el primero
    inv = inv * 10 + digito
    # Eliminas el digito ya usado y luego muestras el numero invertido
    num //= 10

print("Numero invertido:", inv)