import time
from module import *
print("*" * 30)
time.sleep(1)
print("Bonjour! On va jouer à un petit Jeu de Devinette! Qui se joue à 2!")
time.sleep(5)
print("L'un de vous 2 doit rentrer quatre couleurs un à un. L'autre personne devra essayer de le deviner.")
time.sleep(5)
print("Voici la liste des couleurs que vous devez choisir: rose, orange, gris, vert, jaune, blanc, bleu, rouge")
print("*" * 30)

combinaison = generer_masque()
deviner_couleur = deviner_couleur()
de = point(combinaison, deviner_couleur)
