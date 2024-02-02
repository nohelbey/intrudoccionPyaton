# Programa que pregunta dos números a l'usuari i calcula la seva suma.

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

suma = numero1 + numero2

print(f"La suma de {numero1} y {numero2} es: {suma}")


# Programa que pregunta un número i retorna el seu quadrat.

numero = float(input("Introduce un número: "))

cuadrado = numero ** 2

print(f"El cuadrado de {numero} es: {cuadrado}")


# Programa que pregunta el nom a l'usuari i retorna el text: "Hola X". On X és el nom de l'usuari.

nombre = input("Introduce tu nombre: ")

print(f"Hola {nombre}")


# Programa que demana un pes en kg a l'usuari i retorna el mateix pes convertit en lliures.

peso_kg = float(input("Introduce tu peso en kilogramos: "))

peso_libras = peso_kg * 2.20462

print(f"Tu peso en libras es: {peso_libras}")


# Programa que demana una temperatura en graus Celsius a l'usuari i retorna la temperatura en graus Fahrenheit.

temperatura_celsius = float(input("Introduce la temperatura en grados Celsius: "))

temperatura_fahrenheit = temperatura_celsius * 9/5 + 32

print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}")
