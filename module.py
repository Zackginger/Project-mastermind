
#Abel
def generer_masque():
    """
    Cette Fonction permet de générer le masque que le joueur devra deviner.
    :return: masque, la combinaison cachée
    """
    masque = []
    print("*" * 30)
    print("Veuillez rentrer 4 couleurs un par un et ton ami essayera de deviner les couleurs rentrées!!")
    print("*" * 30)
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
    """
    #Pseudo-code(ish)
    #Debut
        #Initialiser liste coul_deviner comme vide
        #Pour i allant de 0 à 3 faire
            #Afficher "Quelle est la i-ème couleeur de la combinaison?
            #Lire dev_coul
            #Mettre dev_coul en minuscules et enlever les espaces
            #Ajouter dev_coul à liste coul_deviner
        #Fin Pour
        #Retourner coul_deviner
    #Fin


    coul_deviner = []
    print("Il y a quatre couleurs qui sont rentré par ton ami!!!Essaie de les deviner en entrant un par un!!!")
    print("*" * 30)
    print("Il y a quatre couleurs qui sont rentrées par ton ami!!!Essaie de les deviner en entrant un par un les couleurs!!!")
    print("*" * 30)
    print("Bonne Chance!!")
    print("*" * 30)
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
    indice={}
    white=0
    black=0
    null=0

    for i in range(len(code)): # pour chaque couleur
        if essai[i] == code[i]: #vérifie la bonne couleur à la place
            white+=1
        elif essai[i] in code: #vérifie si la bonne couleur à la mauvaise place
            black+=1
        else:
            null+=1# fait que les couleur restant sont null

    #pour conter les indices

    indice["white"]=white
    indice["black"]=black
    indice["null"]=null

    return indice



