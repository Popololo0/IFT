#Voici la section 1 du devoir 2 d'IFT 211 d'Olivier Poiré et d'Alexandre Guay. La date de remise est oui.

# Exercice 1

def factorial(nombre) :

    affichage = nombre

    compteur = nombre

    if 0 <= nombre < 256 and type(nombre) == int :
        while compteur > 1 :
            compteur -= 1
            nombre = nombre * compteur

        print ("La réponse de " + str(affichage) + " factoriel est : " + str(nombre))
    else :
        print("Retourne lire le devoir...")

#Exercice 2

def liste_diviseur(n) :
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

def palindrome(mot) :

    if mot != str(mot) or len(mot) >= 100 :
        print("Franchement...")
        return 0

    liste_mot = mot.lower()

    liste_mot = list(liste_mot)

    tom = list(reversed(mot))
    i = 0
    while i < len(mot) // 2 :
        if liste_mot[i] != tom[i] :
            print(mot + " n'est pas un palindrome!")
            return 0
        i += 1
    print(mot + " est un palindrome!")
    return 1

#Exercice 1
factorial()
#Exercice 2
liste_diviseur()
#Exercice 3
palindrome()
