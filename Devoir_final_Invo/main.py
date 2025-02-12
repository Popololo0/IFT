def lecture_nettoyage (chemin) :
    texte = open(chemin, 'r')
    texte = texte.read()
    indesirable = ["'", "...", ">", "<", "~", ",", ".", ":", ";", "!", "?", "(", ")", "-", "[", "]", "{", "}", "#", "$", "%", "&", "*", "+", "/", "=", "|", "_"]
    for x in range(0, len(indesirable)) :
        texte = texte.replace(indesirable[x], " ")

    texte = texte.lower()
    mot = texte.split()
    liste = []
    for x in range(0, len(mot)) :
        if len(mot[x]) > 2 :
            liste.append(mot[x])
    texte = " ".join(liste)

    return texte

def analyse_texte(texte_net) :

    liste_lettre = []
    liste_mot = set()

    nope = texte_net.split()
    len_lettre = len(texte_net)
    len_mot = len(nope)


    for x in range(0, len_lettre) :
        if texte_net[x] not in liste_lettre :
            liste_lettre.append(texte_net[x])

    for x in range(0, len_mot) :
        if nope[x] not in liste_mot :
            liste_mot.add(nope[x])

    return print((len_lettre, len_mot, len(liste_lettre), len(liste_mot)))


texte_net = lecture_nettoyage("sherlock_holmes.txt")
analyse_texte(texte_net)
