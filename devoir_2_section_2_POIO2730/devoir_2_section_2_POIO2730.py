#Voici la section 1 du devoir 2 d'IFT 211 d'Olivier Poiré et d'Alexandre Guay. La date de remise est le 22 janvier 2025.

#Exercice 4
def convertisseur_temperature() :
    i = 1
    while i == 1 :
        x = input("Que voulez-vous faire comme conversion? De C -> F : Faire C. De F -> C : Faire F. ")
        if x == "C" :
            temperature = (input("Quel est la température à convertire? "))
            try :
                temperature = float(temperature)
            except :
                convertisseur_temperature()
                break
            if temperature >= -270 :
                temperature = (9 * temperature / 5) + 32
                print("La température est de " + str(temperature) + " F.")
                i += 1
            else:
                print("Ouin, non...")

        elif x == "F" :
            temperature = (input("Quel est la température à convertire? "))
            try :
                temperature = float(temperature)
            except :
                convertisseur_temperature()
                break
            if temperature >= -459.67:
                temperature = (temperature - 32) * 5 / 9
                print("La température est de " + str(temperature) + " C.")
                i += 1
            else:
                print("Ouin, non...")

        else :
            print("Recommence!")

#Exercice 5
def coucher_a_cote_de_quelqun_est_radioactif() :
    i = 1
    while i == 1 :
        x = input("Que voulez-vous faire comme conversion? De L/100Km -> MpG : Faire L. De MpG -> L/100Km : Faire M. ")
        if x == "L" :
            consommation = (input("Quel est la consommation à convertire? "))
            try :
                consommation = float(consommation)
            except :
                coucher_a_cote_de_quelqun_est_radioactif()
                break
            if consommation > 0 :
                consommation = 235.215 * consommation
                print("La consommation est de " + str(consommation) + " MpG.")
                i += 1
            else:
                print("Ouin, non...")

        elif x == "M" :
            consommation = (input("Quel est la consommation à convertire? "))
            try :
                consommation = float(consommation)
            except :
                coucher_a_cote_de_quelqun_est_radioactif()
                break
            if consommation > 0:
                consommation = consommation / 235.215
                print("La consommation est de " + str(consommation) + " L/100km.")
                i += 1
            else:
                print("Ouin, non...")

        else :
            print("Recommence!")

#Exercice 6
def mondou() :
    i = 1
    while i == 1 :
        forme = input("Quel forme géométrique veux-tu que je calcule aujourd'hui? R pour rectangle, T pour triangle et C pour cercle. ")
        if forme == "R" :
            base = input("Quel est la base du rectangle? ")
            hauteur = input("Quel est la hauteur du rectangle? ")
            try :
                base = float(base)
            except :
                mondou()
                break
            try :
                hauteur = float(hauteur)
            except :
                mondou()
                break
            if base > 0 and hauteur > 0 :
                resultat = base * hauteur
                print("L'aire du rectangle est de " + str(resultat) + " u².")
                i += 1

        elif forme == "T" :
            base = input("Quel est la base du triangle? ")
            hauteur = input("Quel est la hauteur du triangle? ")
            try:
                base = float(base)
            except:
                mondou()
                break
            try:
                hauteur = float(hauteur)
            except:
                mondou()
                break
            if base > 0 and hauteur > 0:
                resultat = (base * hauteur) / 2
                print("L'aire du triangle est de " + str(resultat) + " u².")
                i += 1
        elif forme == "C" :
            rayon = input("Quel est la rayon du cercle? ")
            try :
                rayon = float(rayon)
            except :
                mondou()
                break
            if rayon > 0 :
                resultat = rayon * rayon * 3.1715926535
                print("L'aire du cercle est de " + str(resultat) + " u².")
                i += 1
        else :
            print("Recommence!")

#Exercice 4
convertisseur_temperature()

#Exercice 5
coucher_a_cote_de_quelqun_est_radioactif()

#Exercice 6
mondou()