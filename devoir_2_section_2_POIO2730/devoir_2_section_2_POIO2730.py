# Voici la section 2 du devoir 2 d'IFT 211 d'Olivier Poiré et d'Alexandre Guay. La date de remise est le 22 janvier 2025.

# Exercice 4
# La fonction convertisseur_temperature a pour but de demander à l'utilisateur de choisir le sens de la conversion, puis de convertir la températue et de retourner la réponse.
# Si l'utilisateur rentre une information invalide, le programme recommence.

def convertisseur_temperature() :

    i = 1

    while i == 1 :

        x = input("Que voulez-vous faire comme conversion? Pour °C -> °F, entrez C et pour °F -> °C, entrez F : ")

        if x == "C" or x == "c" :

            temperature = (input("Quel est la température à convertir? "))

            try : # Vérification et convertion en float
                temperature = float(temperature)

            except :
                convertisseur_temperature()
                break

            # Vérification que la valeur soit plausible
            if temperature >= -270 :

                temperature = (9 * temperature / 5) + 32

                print("La température est de " + str(temperature) + " °F.")

                i += 1

            # Si l'utilisateur ne respecte pas les limites de la fonction
            else:

                print("Il faut une valeur supérieure à -270.")

        elif x == "F" or x == "f" :

            temperature = (input("Quel est la température à convertir? "))

            try : # Vérification et convertion en float
                temperature = float(temperature)

            except :
                convertisseur_temperature()
                break

            # Vérification que la valeur soit plausible
            if temperature >= -459.67:

                temperature = (temperature - 32) * 5 / 9

                print("La température est de " + str(temperature) + " °C.")

                i += 1

            # Si l'utilisateur ne respecte pas les limites de la fonction
            else:

                print("Il faut une valeur supérieur à -459.67.")

        # Si l'utilisateur ne répond pas à la question
        else :

            print("Veuillez entrer une réponse valide.")


# Exercice 5
# La fonction convertisseur_consommation a pour but de demander à l'utilisateur de choisir le sens de la conversion, puis de convertir la consommation et de retourner la réponse.
# Si l'utilisateur rentre une information invalide, le programme recommence.

def convertisseur_consommation() :


    i = 1

    while i == 1 :

        x = input("Que voulez-vous faire comme conversion? De L/100Km -> MpG, Faire L et pour MpG -> L/100Km, Faire M : ")

        if x == "L" or x == "l":

            consommation = (input("Quel est la consommation à convertir? "))

            try : # Vérification et convertion en float
                consommation = float(consommation)

            except :
                convertisseur_consommation()
                break

            # Vérification que la valeur soit plausible
            if consommation > 0 :

                consommation = 235.215 * consommation

                print("La consommation est de " + str(consommation) + " MpG.")

                i += 1

            # Si l'utilisateur ne respecte pas les limites de la fonction
            else:

                print("La consommation ne peux pas être négative.")

        elif x == "M" or x == "m":

            consommation = (input("Quel est la consommation à convertir? "))

            try : # Vérification et convertion en float
                consommation = float(consommation)

            except :
                convertisseur_consommation()
                break

            # Vérification que la valeur soit plausible
            if consommation > 0:

                consommation = consommation / 235.215

                print("La consommation est de " + str(consommation) + " L/100km.")

                i += 1

            # Si l'utilisateur ne respecte pas les limites de la fonction
            else:

                print("La consommation ne peux pas être négative.")

        # Si l'utilisateur ne répond pas à la question
        else :

            print("Veuillez entrer une réponse valide.")

# Exercice 6
# La fonction calcul_geometrie a pour but de demander à l'utilisateur laquelle des trois formes géométriques il veut calculer l'aire, puis demande les mesures pour le calcul et donne la réponse en u^2.
# Si l'utilisateur rentre une information invalide, le programme recommence.

def calcul_geometrie() :


    i = 1

    while i == 1 :

        forme = input("Quel forme géométrique veux-tu que je calcule aujourd'hui? R pour rectangle, T pour triangle et C pour cercle. ")

        # "Sous fonction" qui calcul l'aire d'un rectangle en s'assurant d'avoir que des valeurs positives
        if forme == "R" or forme == "r" :

            base = input("Quel est la base du rectangle? ")

            hauteur = input("Quel est la hauteur du rectangle? ")

            try : # Vérification et convertion en float
                base = float(base)

            except :
                calcul_geometrie()
                break

            try : # Vérification et convertion en float
                hauteur = float(hauteur)

            except :
                calcul_geometrie()
                break

            if base > 0 and hauteur > 0 :

                resultat = base * hauteur

                resultat = round(resultat, 3)

                print("L'aire du rectangle est de " + str(resultat) + " u².")

                i += 1

        # "Sous fonction" qui calcul l'aire d'un triangle en s'assurant d'avoir que des valeurs positives
        elif forme == "T" or forme == "t":

            base = input("Quel est la base du triangle? ")

            hauteur = input("Quel est la hauteur du triangle? ")

            try: # Vérification et convertion en float
                base = float(base)

            except:
                calcul_geometrie()
                break

            try: # Vérification et convertion en float
                hauteur = float(hauteur)

            except:
                calcul_geometrie()
                break

            if base > 0 and hauteur > 0:

                resultat = (base * hauteur) / 2

                resultat = round(resultat, 3)

                print("L'aire du triangle est de " + str(resultat) + " u².")

                i += 1

        # "Sous fonction" qui calcul l'aire d'un cercle en s'assurant qu le rayon soit positif
        elif forme == "C" or forme == "c" :

            rayon = input("Quel est la rayon du cercle? ")

            try : # Vérification et convertion en float
                rayon = float(rayon)

            except :
                calcul_geometrie()
                break

            if rayon > 0 :

                resultat = rayon * rayon * 3.1715926535

                resultat = round(resultat, 3)

                print("L'aire du cercle est de " + str(resultat) + " u².")

                i += 1

        # Si l'utilisateur ne répond pas à la question
        else :

            print("Veuillez entrer une réponse valide.")

#Exercice 4
convertisseur_temperature()

#Exercice 5
convertisseur_consommation()

#Exercice 6
calcul_geometrie()
