import time
#Abel
def generer_masque():
    """
    Cette Fonction permet de générer le masque que le joueur devra deviner.
    :return: masque, la combinaison cachée
    """
    masque = []
    print("*" * 30)
    print("Veuillez rentrer 4 couleurs un par un et ton ami essayera de deviner les couleurs rentrées!!")
    time.sleep(5)
    lst_nbre = ["rose", "orange", "gris", "vert", "jaune", "blanc", "bleu", "rouge"]
    print("Vos choix de couleur sont :", lst_nbre)
    print("*" * 30)
    time.sleep(3)
    for i in range(4):
        while True:
            couleur = input(f"quelle est la {i}e couleur de la combinaison?: ").strip().lower()
            if " " or "," or ";" in couleur:
                print("Entre UNE seule couleur, pas plusieurs.")
                continue
            if couleur not in lst_nbre:
                print("Entrer une couleur valide. La couleur doit être dans les choix de couleurs.")
                continue
            else:
                masque.append(couleur)
                break
    return masque

#Sammy
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
    lst_coul = ["rose", "orange", "gris", "vert", "jaune", "blanc", "bleu", "rouge"]
    print("*" * 30)
    print("Voici une liste de couleurs valides: rose, orange, gris, vert, jaune, blanc, bleu, rouge")
    time.sleep(5)
    print("Dans cette liste, il y a quatre couleurs qui sont rentré par ton ami!!!Essaie de les deviner en entrant un par un!!!")
    print("*" * 30)
    time.sleep(1)
    print("Bonne Chance!!")
    print("*" * 30)
    for i in range(4):
        dev_coul = input(f"Quelle est la {i}e couleur de la combinaison?: ").strip().lower()
        while True:
            if " " or "," or ";" in dev_coul:
                print("Entre UNE seule couleur, pas plusieurs.")
                continue
            if dev_coul not in lst_coul:
                print("Entre la couleur valide. La couleur doit être dans la liste des couleurs.")
                continue
            else:
                coul_deviner.append(dev_coul)
                break
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



