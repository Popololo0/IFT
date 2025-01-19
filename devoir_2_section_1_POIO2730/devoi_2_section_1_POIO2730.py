# Voici la section 1 du devoir 2 d'IFT 211 d'Olivier Poiré et d'Alexandre Guay. La date de remise est 22 janvier 2025.

# Exercice 1
# La fonction factorial a pour but de prendre un nombre entre 0 et 256 et de retourner son factoriel.
def factorial(nombre) :

    nombre_initiale = nombre

    compteur = nombre

    # Vérification des conditions limites de la fonction
    if 0 < nombre < 256 and type(nombre) == int :

        while compteur > 1 :

            compteur -= 1

            nombre = nombre * compteur

        print("La réponse de " + str(nombre_initiale) + " factoriel est : " + str(nombre))

    # Dans la situation ou 0! = 1
    elif nombre == 0 :

        nombre = 1

        print ("La réponse de " + str(nombre_initiale) + " factoriel est : " + str(nombre))

    # Si la personne ne respecte pas les conditions de la fonction
    else :

        print("Retourne lire le devoir...")

# Exercice 2
# La fonction liste_diviseur a pour but de trouver la liste des diviseurs d'un nombre entre 0 et 2e16, de les mettres dans une liste et d'afficher cette liste.
def liste_diviseur(n) :

    i = 1

    liste = []

    # Vérification des conditions limites de la fonctoin
    if 0 < n < 2e16 and type(n) == int :

        while i <= n :

            if n % i == 0 :

                liste.append(i)

            i += 1

        print("La liste des diviseurs de "+ str(n) + " sont : " + str(liste))

    # Si la personne ne respecte pas les conditoins de la fonction
    else :

        print("Retourne lire le devoir...")

# Exercice 3
# La fonction palindrome a pour but de prendre un mot de moin de 100 caractères et de déterminer s'il s'agit d'un palindrome ou pas.
# Le seul problème avec la fonction est que si l'on marque un nombre entre guillmet, il va le traiter comme des caractères...
def palindrome(mot) :

    # Vérification des conditions limites de la fonction
    if mot != str(mot) or len(mot) >= 100 :

        print("Franchement...")

        return 0

    liste_mot = mot.lower()

    liste_mot = list(liste_mot)

    tom = list(reversed(mot))

    i = 0

    while i < len(mot) // 2 :

        # Vérification si le mot est un palindrome
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
