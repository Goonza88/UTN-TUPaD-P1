from statistics import mode, median, mean
import random

# Ejercicio 1
edad = int(input("Por favor ingrese su edad: "))
while edad < 0: 
    edad = int(input("Por favor ingrese su edad correcta: "))

if edad > 18: 
   print(f"Usted es mayor de edad")
else: 
    print(f"Usted es menor de edad")

# Ejercicio 2
nota = int(input("Por favor ingrese su nota: "))
if nota >= 6: 
    print(f"Aprobado")
else: 
   print(f"Desaprobado")

# Ejercicio 3
num = int(input("Por favor ingrese un numero par: "))
while num % 2 != 0:
    num = int(input("Por favor ingrese un numero par: "))

if num % 2 == 0: 
    print(f"Ha ingresado un número par")


# Ejercicio 4
edad = int(input("Por favor ingrese su edad: "))
while edad < 0: 
    edad = int(input(f"Por favor ingrese una edad correcta: "))

if edad > 0 and edad < 12: 
   print(f"Usted es un Niño/a")
elif edad >= 12 and edad < 18: 
   print(f"Usted es un Adolescente")
elif edad >= 18 and edad < 30: 
   print(f"Usted es un Adulto/a joven")
else: 
   print(f"Usted es un Adulto/a")

# Ejercicio 5
contra = input("Por favor ingrese una contraseña entre 8 y 14 caracteres: ")
while len(contra) < 8 or len(contra) > 14:
    contra = input("Por favor ingrese una contraseña entre 8 y 14 caracteres: ")
if len(contra) >= 8 and len(contra) <= 14: 
    print(f"Ha ingresado una contraseña correcta")


# Ejercicio 6
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda: 
    print(f"Es sesgo positivo")
elif media < mediana and mediana < moda:
    print(f"Es sesgo negativo")
elif media == mediana == moda:
    print(f"Sin sesgo")

# Ejercicio 7
frase = input("Por favor ingrese una frase o palabra: ")
letra = frase[len(frase) - 1].lower()
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"{frase}!")
else:
    print(f"{frase}")

# Ejercicio 8
nombre = input("Por favor ingrese su nombre: ")
num = int(input("Si quiere que su nombre aparezca en mayusculas, presione 1, si lo quiere en minusculas, presione 2, si quiere la primera letra en mayusculas, presione 3: "))
while num < 0 or num > 3:
    num = int(input("Ingrese uno de los 3 numeros porfavor: "))

if num == 1:
    print(f"{nombre.upper()}")
elif num == 2:
    print(f"{nombre.lower()}")
elif num == 3:
    print(f"{nombre.title()}")

# Ejercicio 9
magnitud = float(input("Por favor ingrese la magnitud del terremoto: "))
if magnitud < 0: 
    print(f"No hubo terremoto")
elif magnitud > 0 and magnitud < 3: 
   print(f"Muy leve (imperciptible)")
elif magnitud >= 3 and magnitud < 4: 
   print(f"Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5: 
   print(f"Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6: 
   print(f"Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7: 
   print(f"Muy Fuerte (puede causar daños significativos)")
else: 
   print(f"Extremo (puede causar graves daños a gran escala)")

# Ejercicio 10
hemis = input("Por favor ingrese en que hemisferio se encuentra: ").lower()
while hemis != "norte" and hemis != "sur":
    hemis = input("Por favor ingrese un hemisferio correcto (Norte o Sur): ").lower()

periodo = 0
mes = input("Por favor ingrese que mes es: ").lower()

dia = int(input("Por favor ingrese que dia es: "))
while dia < 1 or dia > 31:
    dia = int(input(f"Ingrese un dia correcto: "))

if mes == "diciembre":
    if dia <= 20:
        periodo = 4
    else:
        periodo = 1
elif mes == "enero" or mes == "febrero":
    periodo = 1
elif mes == "marzo":
    if dia <= 20:
        periodo = 1
    else:
        periodo = 2
elif mes == "abril" or mes == "mayo":
    periodo = 2
elif mes == "junio":
    if dia <= 20:
        periodo = 2
    else:
        periodo = 3
elif mes == "julio" or mes == "agosto":
    periodo = 3
elif mes == "septiembre":
    if dia <= 20:
        periodo = 3
    else:
        periodo = 4
elif mes == "octubre" or mes == "noviembre":
    periodo = 4
else:
    print(f"Mes mal escrito")


if periodo == 1:
    if hemis == "norte":
        print(f"Se encuentra en Invierno")
    else:
        print(f"Se encuentra en Verano")
elif periodo == 2:
    if hemis == "norte":
        print(f"Se encuentra en Primavera")
    else:
        print(f"Se encuentra en Otoño")
elif periodo == 3:
    if hemis == "norte":
        print(f"Se encuentra en Verano")
    else:
        print(f"Se encuentra en Invierno")
elif periodo == 1:
    if hemis == "norte":
        print(f"Se encuentra en Otoño")
    else:
        print(f"Se encuentra en Primavera")