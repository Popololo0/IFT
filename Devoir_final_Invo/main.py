import unicodedata

def supprimer_accents(texte_net):
    """
    Supprime les accents d'une chaîne de caractères.
    Fonction utilitaire pour le devoir 5.
    """
    forme_nfkd = unicodedata.normalize('NFKD', texte_net)
    uniquement_ascii = forme_nfkd.encode('ASCII', 'ignore')
    uniquement_utf8 = uniquement_ascii.decode("utf-8")
    return str(uniquement_utf8)

def lecture_nettoyage (chemin) :

    texte = open(chemin, 'r')
    texte = texte.read()

    indesirable = ["'", "...", ">", "<", "~", ",", ".", ":", ";", "!", "?", "(", ")", "-", "[", "]", "{", "}", "#", "$", "%", "&", "*", "+", "/", "=", "|", "_", "@", "^", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for x in range(0, len(indesirable)) :
        texte = texte.replace(indesirable[x], " ")

    texte = texte.lower()
    mot = texte.split()
    liste = []
    for x in range(0, len(mot)) :
        if len(mot[x]) > 2 :
            liste.append(mot[x])

    texte = " ".join(liste)
    texte = supprimer_accents(texte)
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
    liste_lettre.remove(" ")

    for x in range(0, len_mot) :
        if nope[x] not in liste_mot :
            liste_mot.add(nope[x])

    return print((len_lettre, len_mot, len(liste_lettre), len(liste_mot)))

def inversoin_texte(texte_net) :

    o = texte_net[::-1]

    x = str(texte_net)
    h = x.split()
    j = h[::-1]
    k = " ".join(j)

    return o, k

texte_net = lecture_nettoyage("sherlock_holmes.txt")

analyse_texte(texte_net)

inversoin_texte(texte_net)
