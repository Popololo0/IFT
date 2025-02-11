def lecture_nettoyage (chemin) :
    texte = open(chemin, 'r')
    texte = texte.read()
    indesirable = ["'", "...", ">", "<", "~", ",", ".", ":", ";", "!", "?", "(", ")", "-", "[", "]", "{", "}", "#", "$", "%", "&", "*", "+", "/", "=", "|", "_"]
    for x in range(0, len(indesirable)):
        texte = texte.replace(indesirable[x], " ")
        #texte = texte.strip() # Wtf que ça ne fonctionnne pas...
        texte_net = texte.lower()

    # Vérifier if len(mot) < 2 : strip (mot)
    print(texte_net)

def analyse_texte (texte_net) :
    lettre = len(texte_net)


lecture_nettoyage("sherlock_holmes.txt")
