import unicodedata
import string

def supprimer_accents(texte_net):
    """
    Supprime les accents d'une chaîne de caractères.
    Fonction utilitaire pour le devoir 5.
    """
    forme_nfkd = unicodedata.normalize('NFKD', texte_net)
    uniquement_ascii = forme_nfkd.encode('ASCII', 'ignore')
    uniquement_utf8 = uniquement_ascii.decode("utf-8")
    return str(uniquement_utf8)

def lecture_nettoyage (texte) :

    texte = open(texte, 'r')
    texte = texte.read()

    texte = texte.lower()
    yes = list(string.ascii_lowercase)

    for x in range(0, len(texte)) :
        if texte[x] not in yes :
            texte = texte.replace(texte[x], " ")

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
    #print(o)
    #print(k)
    return o, k

def score_scrable(texte_net) :

    valeur = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':5,'h':4,'i':1,'j':8,'k':10,'l':1,'m':2,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,'w':10,'x':10,'y':10,'z':10}
    mot = texte_net.split()
    resultat = {}

    for i in range(0, len(mot)) :
        score_mot = 0
        evaluation = list(mot[i])

        for x in range(0,len(evaluation)):
            evaluation[x] = valeur[evaluation[x]]
            score_mot = score_mot + evaluation[x]

        resultat[mot[i]] = score_mot

    resultat = dict(sorted(resultat.items(), key=lambda item: item[1]))
    liste_mot = list(resultat.keys())
    liste_score = list(resultat.values())

    liste_mot50 = liste_mot[::-1]
    liste_score50 = liste_score[::-1]
    affichage = []

    for i in range(0, 49) :
        affichage.append(str(liste_mot50[i]) + ', ' + str(liste_score50[i]))

    affichage = affichage[::-1]

    for i in range(0,49) :
        print(affichage[i])




texte_net = lecture_nettoyage("sherlock_holmes.txt")

analyse_texte(texte_net)

inversoin_texte(texte_net)

score_scrable(texte_net)
