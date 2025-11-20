import pytest
from module import *
#Zackary Ritchie
@pytest.mark.parametrize("code , essai , dictindice", [
                        (["rose","vert","bleu","rouge"],["vert","rose","gris","orange"],{"white":0,"black":2,"null":2}),
                        (["vert","vert","vert","vert"],["vert","vert","vert","vert"],{"white":4,"black":0,"null":0}),
                        (["rose","rose","rose","rose"],["rouge","bleu","jaune","rouge"],{"white":0,"black":0,"null":4}),
                        (["bleu","vert","bleu","vert"],["vert","bleu","vert","bleu"],{"white":0,"black":4,"null":0}),
                        (["rose","bleu","jaune","vert"],["jaune","jaune","jaune","bleu"],{"white":1,"black":1,"null":2})

])
def testpoint(code,essai,dictindice):

    indices=point(code,essai)

    assert indices==dictindice


#Sammy
@pytest.mark.parametrize(
    "entrees, attendu",
    [
        # Cas 1 : 4 couleurs valides
        (["rouge", "bleu", "gris", "vert"],
         ["rouge", "bleu", "gris", "vert"]),

        # Cas 2 : erreurs puis correction
        (["pomme", "rouge", "bleu", "camion", "gris", "vert"],
         ["rouge", "bleu", "gris", "vert"]),

        # Cas 3 : majuscules + espaces
        (["   ROUGE  ", "  BLEU", "gris   ", "VERT"],
         ["rouge", "bleu", "gris", "vert"]),
    ]
)
def test_deviner_couleur(entrees, attendu):
    resultat = deviner_couleur(inputs=entrees) # on a pas d'autre chose à rentrer c'est pourquoi ca ne marche pas
    assert resultat == attendu
    assert len(resultat) == 4


#Abel
@pytest.mark.parametrize(
    "entrees, attendu",
    [
        # Cas 1 : 4 couleurs valides
        (["rouge", "bleu", "gris", "vert"],
         ["rouge", "bleu", "gris", "vert"]),

        # Cas 2 : erreurs puis correction
        (["pomme", "rouge", "bleu", "camion", "gris", "vert"],
         ["rouge", "bleu", "gris", "vert"]),

        # Cas 3 : majuscules + espaces
        (["   ROUGE  ", "  BLEU", "gris   ", "VERT"],
         ["rouge", "bleu", "gris", "vert"]),
    ]
)
def test_generer_masque(entrees, attendu):
    resultat = generer_masque(inputs=entrees)
    assert resultat == attendu
    assert len(resultat) == 4

