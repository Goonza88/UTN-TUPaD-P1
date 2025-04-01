from statistics import mode, median, mean
import random

# Ejercicio 1
# Pido edad, si no es valida, la pido de vuelta, si es correcta doy respuesta
edad = int(input("Por favor ingrese su edad: "))
while edad < 0: 
    edad = int(input("Por favor ingrese su edad correcta: "))
if edad > 18: 
   print(f"Usted es mayor de edad")
else: 
    print(f"Usted es menor de edad")

# Ejercicio 2
# Pido nota y devuelvo resultado
nota = int(input("Por favor ingrese su nota: "))
if nota >= 6: 
    print(f"Aprobado")
else: 
   print(f"Desaprobado")

# Ejercicio 3
# Pido un numero par, si no es par lo pido de devuelta, si es par respondo
num = int(input("Por favor ingrese un numero par: "))
while num % 2 != 0:
    num = int(input("Por favor ingrese un numero par: "))

if num % 2 == 0: 
    print(f"Ha ingresado un número par")


# Ejercicio 4
# Pido edad, si es un numero negativo lo pido de vuelta
edad = int(input("Por favor ingrese su edad: "))
while edad < 0: 
    edad = int(input(f"Por favor ingrese una edad correcta: "))

# Segun la edad, las condicionales van a dar un respuesta u otra
if edad > 0 and edad < 12: 
   print(f"Usted es un Niño/a")
elif edad >= 12 and edad < 18: 
   print(f"Usted es un Adolescente")
elif edad >= 18 and edad < 30: 
   print(f"Usted es un Adulto/a joven")
else: 
   print(f"Usted es un Adulto/a")

# Ejercicio 5
# Pido la contraseña con las condiciones requeridas, si no las cumple, la pido de vuelta, si las cumple, doy respuesta
contra = input("Por favor ingrese una contraseña entre 8 y 14 caracteres: ")
while len(contra) < 8 or len(contra) > 14:
    contra = input("Por favor ingrese una contraseña entre 8 y 14 caracteres: ")
if len(contra) >= 8 and len(contra) <= 14: 
    print(f"Ha ingresado una contraseña correcta")


# Ejercicio 6
# Se genera una lista de numeros aleatorios, luego pongo en variables la moda, la mediana y la media de la lista
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
# Dependiendo de como se den los numeros aleatorios, va a ser una respuesta u otra
if media > mediana and mediana > moda: 
    print(f"Es sesgo positivo")
elif media < mediana and mediana < moda:
    print(f"Es sesgo negativo")
elif media == mediana == moda:
    print(f"Sin sesgo")

# Ejercicio 7
# Pido una frase o palabra, tomo la ultima letra, si termina en una vocal, devuelvo la frase con "!", sino devuelvo la misma frase
frase = input("Por favor ingrese una frase o palabra: ")
letra = frase[len(frase) - 1].lower()
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"{frase}!")
else:
    print(f"{frase}")

# Ejercicio 8
# Pido el nombre y que se selecciona la accion deseada, si el usuario no pone un numero correcto, se lo pido devuelta
nombre = input("Por favor ingrese su nombre: ")
num = int(input("Si quiere que su nombre aparezca en mayusculas, presione 1, si lo quiere en minusculas, presione 2, si quiere la primera letra en mayusculas, presione 3: "))
while num < 0 or num > 3:
    num = int(input("Ingrese uno de los 3 numeros porfavor: "))
# Dependiendo lo elegido se muestra un resultado u otro
if num == 1:
    print(f"{nombre.upper()}")
elif num == 2:
    print(f"{nombre.lower()}")
elif num == 3:
    print(f"{nombre.title()}")

# Ejercicio 9
# Pido un numero de magnitud, dependiendo de lo que el usuario escriba, va a ver un resultado u otro
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
# Creo variable periodo para evitar futuros errores
periodo = 0

# Pido un hemisferio, si no pone Norte o Sur, se lo vuelvo a pedir
hemis = input("Por favor ingrese en que hemisferio se encuentra: ").lower()
while hemis != "norte" and hemis != "sur":
    hemis = input("Por favor ingrese un hemisferio correcto (Norte o Sur): ").lower()

# Pido mes del año
mes = input("Por favor ingrese que mes es: ").lower()

# Pido dia del mes, si ingresa un numero incorrecto, se lo pido devuelta
# (No se tienen en consideracion los meses que tienen 30 dias o menos, no lo especifica la consigna)
dia = int(input("Por favor ingrese que dia es: "))
while dia < 1 or dia > 31:
    dia = int(input(f"Ingrese un dia correcto: "))

# Segun el mes y el dia puesto, se selecciona el periodo del año en que se encuentra, entre 1 y 4, si el mes estuvo mal escrito, se avisa
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

# Dependiendo el periodo y el hemisferio en el que se encuentre, se determina la estacion y se muestra resultado
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