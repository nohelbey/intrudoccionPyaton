#Programa que pregunta el nom de l'usuari i només dona la benvinguda si l'usuari es diu "Amilcar" o "Sila".
def donar_benvinguda():
    nom_usuari = input("Si us plau, introdueix el teu nom: ")
    if nom_usuari.lower() == "amilcar" or nom_usuari.lower() == "sila":
        print("Benvingut, " + nom_usuari + "!")
    else:
        print("Ho sentim, només es dóna la benvinguda als usuaris amb els noms 'Amilcar' o 'Sila'.")




 #Programa que pregunta un número a l'usuari i diu si és major o menor que 100.
def comparar_numero():
    numero = float(input("Si us plau, introdueix un número: "))
    if numero > 100:
        print("El número introduït és major que 100.")
    elif numero < 100:
        print("El número introduït és menor que 100.")
    else:
        print("El número introduït és igual a 100.")




#Programa que pregunta un número a l'usuari i diu si és senar o parell.
def verificar_senar_o_parell():
    numero = int(input("Si us plau, introdueix un número: "))
    if numero % 2 == 0:
        print("El número introduït és parell.")
    else:
        print("El número introduït és senar.")




#Programa que pregunta la nota a l'usuari i segons la nota diu el resultat obtingut: 1 a 4 - Insuficient, 5 - Suficient, 6 - Bé, 7 a 8 - Notable, 9 a 10 - Excel·lent.
def verificar_nota():
    nota = float(input("Si us plau, introdueix la teva nota: "))
    if nota >= 1 and nota <= 4:
        print("Insuficient")
    elif nota == 5:
        print("Suficient")
    elif nota == 6:
        print("Bé")
    elif nota >= 7 and nota <= 8:
        print("Notable")
    elif nota >= 9 and nota <= 10:
        print("Excel·lent")
    else:
        print("Nota incorrecta. La nota ha d'estar entre 1 i 10.")

verificar_nota()


#Fes un programa que pregunti quants anys portes treballant de programador i et digui que ets junior si portes menys de 5 anys i senior si portes més de 5.
def determinar_categoria():
    anys_treballats = int(input("Quants anys portes treballant de programador? "))
    if anys_treballats < 5:
        print("Ets un programador junior.")
    else:
        print("Ets un programador senior.")




