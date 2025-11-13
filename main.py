import time
from module import *
print("*" * 30)
time.sleep(0.5)
print("Bonjour! On va jouer à un petit Jeu de Devinette! Qui se joue à 2!")
time.sleep(0.5)
print("L'un de vous 2 doit rentrer quatre couleurs un à un. L'autre personne devra essayer de le deviner.")
time.sleep(0.5)
print("Voici la liste des couleurs que vous devez choisir: rose, orange, gris, vert, jaune, blanc, bleu, rouge")
time.sleep(0.5)
print("*" * 30)
time.sleep(3)
combinaison = generer_masque()

for i in range(10):
    deviner_couleure = deviner_couleur()
    indice=point(combinaison,deviner_couleure)
    if indice["white"]==4:
        print("Vous avez deviner correct")
        break
    else:
        print(f"Le nombre d'essai restant est {10-i}")
        print(indice)