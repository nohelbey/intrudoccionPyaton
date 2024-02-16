#Fes un programa que pregunta un número i et retorna tots els números que són divisors del número (els que la seva divisió no té residu).
def trobar_divisors(numero):
    divisors = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisors.append(i)
    return divisors

numero = int(input("Introdueix un número: "))
divisors = trobar_divisors(numero)
print("Els divisors de", numero, "són:", divisors)


#Fes un programa que pregunti números a l'usuari i calculi la seva mitjana, el programa preguntarà números fins que l'usuari escrigui un 0.
def calcular_mitjana():
    numeros = []
    while True:
        num = float(input("Introdueix un número (0 per sortir): "))
        if num == 0:
            break
        numeros.append(num)
    if len(numeros) == 0:
        print("No s'han proporcionat números.")
    else:
        mitjana = sum(numeros) / len(numeros)
        print("La mitjana dels números és:", mitjana)


#Fes un programa que pregunti un número i sumi els números imparells entre 1 i el número introduït.
def suma_impares_fins_a(numero):
    suma = 0
    for i in range(1, numero + 1, 2):
        suma += i
    return suma

numero = int(input("Introdueix un número: "))
suma_impares = suma_impares_fins_a(numero)
print("La suma dels números imparells fins a", numero, "és:", suma_impares)
