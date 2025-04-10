import math

# Ejercicio 1
# Se imprime automaticamente el mensaje
def imprimir_hola_mundo():
    return print("Hola Mundo!")

imprimir_hola_mundo()

# Ejercicio 2
# Se pide el nombre al usuario y se imprime con un mensaje
def saludar_usuario(nombre):
    return print(f"Hola {nombre}, buenos dias!")

nombre = input("Como te llamas? ")
saludar_usuario(nombre)

# Ejercicio 3
# Se pide informacion al usuario y se imprime un mensaje con la informacion
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre, apellido, edad, residencia = input("Ingresa tu nombre, apellido, edad y lugar de residencia en ese orden y separados por espacio: ").split()
informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4
# Se pide el radio de un circulo al usuario y se ejecutan dos funciones para calcular area y perimetro y luego se imprime en un solo mensaje
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio 

radio = int(input("Por favor ingresa el radio de un circulo: "))
print(f"El area es {calcular_area_circulo(radio)}\nEl perimetro es {calcular_perimetro_circulo(radio)}")

# Ejercicio 5
# Se pide la cantidad de segundos al usuario y luego se calculan la cantidad de hora/s
def segundos_a_horas(segundos):
    return print(f"La cantidad de hora/s es {segundos / 60 / 60}.")

segundos = int(input("Por favor ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)

# Ejercicio 6
# Se pide un numero al usuario y luego se ejecuta una funcion con un loop para multiplicar e imprimir cada resultado 
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} multiplicado por {i} es: {numero * i}")
        i += 1
    return 
numero = int(input("Ingresa un numero para saber su tabla del 1 al 10: "))
tabla_multiplicar(numero)

# Ejercicio 7
# Se piden dos numeros al usuario y luego se imprime la suma, resta, multiplicacion y division en un solo mensaje
def operaciones_basicas(a, b):
    print(f"La suma entre ellos es: {a + b}.\nLa resta entre ellos es: {a - b}.\nLa multiplicacion entre ellos es: {a * b}.\nLa division entre ellos es: {a / b}.")
    return

a, b = map(int, input("Ingresa dos numeros separados por espacio: ").split())
operaciones_basicas(a, b)

# Ejercicio 8
# Se pide el peso y la altura al usuario y luego se imprime el IMC
def calcular_imc(peso, altura):
    print(f"Tu indice de masa corporal es: {peso / altura ** 2}")
    return

peso, altura = map(float, input("Ingresa tu peso(kg) y luego tu altura(m) separados por espacio: ").split())
calcular_imc(peso, altura)

# Ejercicio 9
# Se pide la temperatura en grados celsius al usuario y luego se transforma en fahrenheit y se imprime el resultado
def celsius_a_fahrenheit(celsius):
    print(f"{celsius}° pasado a fahrenheit son: {(celsius * 9/5) + 32}°.")
    return

celsius = int(input("Por favor ingresa la temperatura en grados Celsius: "))
celsius_a_fahrenheit(celsius)

# Ejercicio 10
# Se piden tres numero al usuario, se saca el promedio y se imprime
def calcular_promedio(a, b, c):
    print(f"El promedio entre esos numeros es: {(a + b + c) / 3}")
    return

a, b, c = map(int, input("Ingresa tres numeros separados por espacio: ").split())
calcular_promedio(a, b, c)