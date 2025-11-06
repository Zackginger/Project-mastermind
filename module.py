


#Abel
def generer_masque():
    """
    Cette Fonction permet de générer le masque que le joueur devra deviner.
    :return:
    """
    masque = []
    lst_nbre = ["rose", "orange", "gris", "vert", "jaune", "blanc", "bleu", "rouge"]
    print("Vos choix de couleur sont :", lst_nbre)

    for i in range(4):
        couleur = input(f"quelle est la {i}e couleur de la combinaison?: ").strip().lower()
        masque.append(couleur)
    return masque


def deviner_couleur():
    """
    Cette fonction permet au joueur de deviner les couleurs rentrer par l'utisateur.
    :return:

    Pseudo-code(ish)
    on demander au joueur de rentrer les couleurs rentrer par son ami(ou l'utilisateur)
    on met ces couleurs dans une liste qui les enregistre.
    """
    coul_deviner = []
    print("Il y a quatre couleurs qui sont rentré par ton ami!!!Essaie de les deviner en entrant un par un!!!")
    for i in range(4):
        dev_coul = input(f"Quelle est la {i}e couleur de la combinaison?: ").strip().lower()
        coul_deviner.append(dev_coul)
    return coul_deviner

#Zackary Ritchie
def point(code:list,essai:list):
    """
    la fonction trouve si les couleurs sont dans la combinaison et si elles sont dans la bonne position.
    :param code: le code donné par l'utilisateur
    :param essai: essai au code donné par l'adversaire
    :return: les indices blanc==bonne position et bonne couleur et noir == bonne couleur mauvaise position

    créer variable
    faire boucle
        faire condition pour vérifier si bonne couleur et position

    faire boucle
        faire condition pour vérifier si couleur est deja prise en charge
            faire boucle
                faire condition pour vérifier couleur est bonne mais pas bonne position

    faire boucle
        faire condition pour vérifier si couleur est deja prise en charge
            faire condition pour vérifier si la couleur est mauvaise

    """

    correct=[
        ["1"],
        ["2"],
        ["3"],
        ["4"]
    ]
    code2=code.copy()
    for i in range(len(code)): # pour chaque couleur
        if essai[i] == code[i]: #vérifie la bonne couleur à la place
            correct[i].append("white")
            code2.pop(i)
            code2.insert(i,"_")
            break

    for a in range(len(code)): #pour chaque couleur
        if len(correct[a])==1: #vérifie si la couleur a déja un résultat
            for b in range(len(code2)): #boucle pour  verifier chaque couleur dans la code initial
                if essai[a] == code2[b] : #vérifie si la bonne couleur à la mauvaise place
                    correct[a].append("black")
                    break

    for c in range(len(correct)): #pour chaque couleur
        if len(correct[c]) == 1: #vérifie si la couleur a déja un résultat
            correct[c].append("null") # fait que les couleur restant sont null

    #pour conter les indices
    indice={}
    null=0
    for d in range(4):
        null+=correct[d].count("null")
    black=0
    for e in range(4):
        black+=correct[e].count("black")
    white=0
    for f in range(4):
        white+=correct[f].count("white")
    indice["white"]=white
    indice["black"]=black
    indice["null"]=null

    return indice

cd=["bleu","vert","rouge","rose"]
es=["vert","bleu","gris","orange"]
print(point(cd,es))

