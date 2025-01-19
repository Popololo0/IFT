#Voici la section 1 du devoir 2 d'IFT 211 d'Olivier Poiré et d'Alexandre Guay. La date de remise est le 22 janvier 2025.

# Exercice 1
def factorial() :

    nombre = int(input("Valeur nombre factoriel? "))

    Yes = nombre

    compteur = nombre

    if 0 < nombre < 256 and type(nombre) == int :
        while compteur > 1 :
            compteur -= 1
            nombre = nombre * compteur

        print ("La réponse de " + str(Yes) + " factoriel est : " + str(nombre))

    elif nombre == 0 :
        nombre = 1
        print("La réponse de " + str(Yes) + " factoriel est : " + str(nombre))

    else :
        print("Retourne lire le devoir...")

#Exercice 2
def liste_diviseur() :
    n = int(input("Valeur nombre de la diviseur : "))
    i = 1
    liste = []
    if 0 < n < 2e16 and type(n) == int :
        while i <= n :
            if n % i == 0 :
                liste.append(i)
            i += 1
        print("La liste des diviseurs de "+ str(n) + " sont : " + str(liste))
    else :
        print("Retourne lire le devoir...")

#Exercice 3
'''def palindrome(mot) :

    longueur = len(mot)
    i = 0
    liste_mot = [mot]
    print(longueur)
    print(mot[i])
    while i < longueur :
       if mot[i] == mot[-i] :
           i += 1
            print()'''

#Exercice 1
factorial()

#Exercice 2
liste_diviseur()

#Exercice 3
#palindrome("ete")
