from string import whitespace


def generer_masque():
    """
    Cette Fonction permet de générer le masque que l'utilisateur devra deviner.
    :return:
    """
    masque = []
    lst_nbre = ["rose", "orange", "gris", "vert", "jaune", "blanc", "bleur", "rouge"]
    for i in range(3):
        print("Vos choix de couleur sont :",lst_nbre)
        chiffre = input(f"quelle est {i} couleur de la combinaison : ")
        masque.append(chiffre)
    return masque

def verifier_combinaison(deviner_combi, masque):
    """
    La fonction permet de à l'utisateur de reconnaitre s'il a deviner la bonne combinaison ou la mauvaise combinaison.
    :param deviner_combi: La combinaison à deviner
    :param masque: La combinaison générer que l'utisateur doit deviner
    :return:
    """
    essaie = 0
    while essaie < 10:
        if deviner_combi == masque:
            print("Bravo vous avez trouvé la combinaison.")
            break
        else:
            print("Désolé, ce n'est pas la bonne réponse.")
            essaie += 1

def point(code:list,essai:list):
    """
    la fonction trouve si les couleurs est dans la combinaison et si elles sont dans la bonne position.
    :param code: le code donné par l'utilisateur
    :param essai: essai au code donné par l'adversaire
    :return: les indices blanc==bonne position et bonne couleur et noir == bonne couleur mauvaise position

    copie du code et essai pour garder valeur initial
    list 2d (correct) pour garder l'ordre et les valeur des couleur

    for in range(len(code)) et un if pour verifier si il y a un couleur à la bonne position
    puis l'ajouté à correct pour qu'on connait s'il y a une bonne couleur à la bonne position

    2 for
    1er pour que les verifications soit fait avec tout les couleurs
    2e pour pour que les verifications des la couleur éssai se fait dans tout les couleurs de la combinaison
    if la couleur est déja réppondu
    if la couleur est égale


    """

    correct=[
        ["1"],
        ["2"],
        ["3"],
        ["4"]
    ]
    code2 =code.copy()
    essai2=essai.copy()
    for i in range(len(code2)):
        if essai[i] == code[i]:
            correct[i].append("white")
            break

    for ses in range(len(code2)-1):
        if len(correct[ses])==1:
            for c in range (len(code2) - 1):
                if essai2[ses] == code2[c] :
                    correct[ses].append("black")
                    break
    for a in range(len(correct)):
        if len(correct[a]) == 1:
            correct[a].append("null")

    return correct

"""
if __name__ == "__main__":
    while True:
        try:
            nbre_combi = int(input("Combien de nombre voulez-vous que la combinaison comporte: "))
            gen_masque = generer_masque(nbre_combi)
            deviner_combinaison = int(input(f"Veillez deviner la combinaison. Les chiffres dans la combinaison sont {nbre_combi}: "))
            verifier_combinaison(deviner_combinaison,gen_masque)
        except ValueError:
            print("Veuillez entrer un chiffre.")
        break

"""


masques=["rose","bleu","vert","vert"]
essait=["rose","rouge","bleu","rouge"]

print(point(masques,essait))