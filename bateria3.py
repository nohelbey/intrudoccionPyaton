#Fes un programa que demana un número a l'usuari i imprimeix la seva taula de multiplicar (del 1 al 10).
def taula_de_multiplicar():
    numero = int(input("Introdueix un número per veure la seva taula de multiplicar: "))
    print("Taula de multiplicar de", numero)
    for i in range(1, 11):
        resultat = numero * i
        print(numero, "x", i, "=", resultat)


#Fes un programa que pregunti un número a l'usuari i retorni la suma de tots els números fins el que ha introduït l'usuari.
def suma_hasta_numero():
    numero = int(input("Introdueix un número: "))
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    return suma

resultat = suma_hasta_numero()
print("La suma de tots els números fins al número introduït és:", resultat)


#Modifica el programa anterior per a que només sumi els números parells.
def suma_numeros_parells_fins_a(numero):
    suma = 0
    for i in range(2, numero + 1, 2):  # Empezamos desde 2 y aumentamos de 2 en 2
        suma += i
    return suma

numero = int(input("Introdueix un número: "))
resultat = suma_numeros_parells_fins_a(numero)
print("La suma dels números parells fins al número introduït és:", resultat)


#Modifica el programa anterior per que sigui l'usuari si vol sumar els números parells o els senars.
def suma_numeros_fins_a(numero, es_parell):
    suma = 0
    if es_parell:
        for i in range(2, numero + 1, 2):
            suma += i
    else:
        for i in range(1, numero + 1, 2):
            suma += i
    return suma

numero = int(input("Introdueix un número: "))
es_parell = input("Vols sumar els números parells? (respon 'si' o 'no'): ").lower()
while es_parell not in ['si', 'no']:
    es_parell = input("Per favor, respon 'si' o 'no': ").lower()

if es_parell == 'si':
    resultat = suma_numeros_fins_a(numero, True)
    print("La suma dels números parells fins al número introduït és:", resultat)
else:
    resultat = suma_numeros_fins_a(numero, False)
    print("La suma dels números senars fins al número introduït és:", resultat)


#Fes un programa que imprimeixi per pantalla els números primers.
def es_primer(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def imprimir_primers_fins_a(limite):
    print("Els números primers fins a", limite, "són:")
    for num in range(2, limite + 1):
        if es_primer(num):
            print(num)

limite = int(input("Introdueix el límit superior: "))




