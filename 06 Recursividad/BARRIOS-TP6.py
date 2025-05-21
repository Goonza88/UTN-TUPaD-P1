# Ejercicio 1
# Creacion de la funcion factorial
def factorial(n):

   #Si el numero ingresado es 0 devuelve 1
    if n == 0:
        return 1
    
    # Si el numero no es 0, devuelve el numero multiplicado por el mismo menos 1, y como llamas a la funcion de vuelta sigue asi hasta que el numero sea 0
    else:
        return n * factorial(n - 1)

# Pides al usuario el numero
n = int(input("Ingrese un numero: "))

# Loop para ejecutar la funcion entre 1 y el numero ingresado
for i in range(1, n + 1):
  print(f"El factorial de {i} es: {factorial(i)}")

# Ejercicio 2
# Se crea la funcion fibonacci
def fibonacci(p):

    # Si la posicion ingresada es 0, devuelve 0, si es 1, devuelve 1, estas serian las posiciones base
   if p == 0:
        return 0
   elif p == 1:
       return 1
    
    # Si la posicion es arriba de las posiciones base, se devuelve la suma de la posicion menos uno con la posicion menos dos
   else:
       return fibonacci(p - 1) + fibonacci(p - 2)

# Se pide la posicion
p = int(input("Ingrese la posicion: "))

# Loop para ejecutar la funcion entre 1 y la posicion ingresada
for i in range(1, p + 1): 
  print(f"El numero fibonacci de la serie {i} es: {fibonacci(i)}")

# Ejercicio 3
# Se crea la funcion potencia, pidiendo una base y un exponente
def potencia(b, e):

    # Si el exponente es 0 devuelve 1
    if e == 0:
       return 1
    
    # Si el exponente no es 0, multiplica la base por la potencia con exponente menos uno hasta llegar a 0
    else:
      return b * potencia(b, e - 1)

# Se le pide los numeros al usuario y luego se muestra el resultado
b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))

print(f"El resultado es: {potencia(b,e)}")

# Ejercicio 4
# Se crea la funcion decimal a binario
def dec_a_bin(n):

    # Cuando el numero llega a cero, termina devolviendo nada
  if n == 0:
      return ""
    
    # Toma el numero ingresado, lo divide por dos de forma entera y suma a un string el resto
  else:
      return dec_a_bin(n // 2) + str(n % 2)

# Se le pide al usuario un numero y se ejecuta la funcion
n = int(input("Ingrese un numero mayor a 0: "))

print(f"El numero {n} pasado a binario es: {dec_a_bin(n)}")

# Ejercicio 5
# ACLARACION: La consigna pide no usar [::-1], yo use [1:-1], no se si es lo mismo o no pero no encontre otra forma
# Se crea la funcion 
def es_palindromo(str):
   
    # Si la longitud del string es menor o igual a 1 devuelve True
    if len(str) <= 1:
      return True
    
    # Compara la primera y ultima letra, si no son iguales corta y devuelve false
    if str[0] != str[-1]:
        return False
    
    # Se llama la funcion devuelta y se "cortan" el inicio y final
    return es_palindromo(str[1:-1])

# Se le pide al usuario un string y se muestra el resultado
str = input(str("Ingrese una cadena de texto sin espacios ni tildes: "))

print(es_palindromo(str))

# Ejercicio 6
# Se crea la funcion para sumar digitos
def suma_digitos(n):
    
    # Si el numero es menor que 10, devuelve el mismo numero
    if n < 10:
        return n
    
    # Sino detecta el ultimo digito con el resultado de modulo 10, y luego elimina el ultimo digito con la division entera a 10
    else:
        return (n % 10) + suma_digitos(n // 10)

# Pide numero al usuario y muestra el resultado
n = int(input("Ingrese un numero: "))

print(f"La suma de los digitos de {n} es: {suma_digitos(n)}")

# Ejercicio 7
# Se crea la funcion para contar bloques
def contar_bloques(n):

    # Si el numero es menor o igual a 1, devuelve que necesita 1 bloque
    if n <= 1:
        return 1

    # Sino toma el numero y le va sumando el mismo menos uno
    else:
        return n + contar_bloques(n - 1)

# Pide numero al usuario y muestra el resultado
n = int(input("Ingrese un numero: "))

print(f"Para construir toda la piramide necesita {contar_bloques(n)} bloque/s.")

# Ejercicio 8
# Se crea funcion para contar cuantas veces aparece un digito en un numero
def contar_digito(n, d):

    # Si el numero es 0 devuelvo 0
    if n == 0:
        return 0
    
    # Se crea una variable para guarda la suma de coincidencias
    contador = 0

    # Se compara el ultimo numero con el digito
    if n % 10 == d:
        contador = 1

    # Se elimina el ultimo numero hasta terminar
    return contador + contar_digito(n // 10, d)

# Pide numero y digito al usuario y se muestra el resultado
n = int(input("Ingrese un numero: "))
d = int(input("Ingrese un digito entre 0 y 9: "))

print(f"El digito {d} aparece {contar_digito(n, d)} veces.")