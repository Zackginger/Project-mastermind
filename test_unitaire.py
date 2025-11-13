import pytest
from module import *

@pytest.mark.parametrize("code , essai , dictindice", [
                        (["rose","vert","bleu","rouge"],["vert","rose","gris","orange"],{"white":0,"black":2,"null":2}),
                        (["vert","vert","vert","vert"],["vert","vert","vert","vert"],{"white":4,"black":0,"null":0}),
                        (["rose","rose","rose","rose"],["rouge","bleu","jaune","rouge"],{"white":0,"black":0,"null":4}),
                        (["bleu","vert","bleu","vert"],["vert","bleu","vert","bleu"],{"white":0,"black":4,"null":0}),
                        (["bleu","bleu","rouge","orange"],["bleu","vert","orange","jaune"],{"white":1,"black":1,"null":2})

])
def testpoint(code,essai,dictindice):

    indices=point(code,essai)

    assert dictindice==indices

@pytest.mark.parametrize("couleur", "resultat_attendu",[
    ("rose", "rose"),
    ("jaune", "Jaune"),
    ("violet", "Entrez la couleur valide ou rentrez une couleur à la fois."),
    ("2", "Entrez la couleur valide ou rentrez une couleur à la fois."),
    ("jaune, vert, bleu", "Entrez la couleur valide ou rentrez une couleur à la fois."),
    ("rouge,", "Entrez la couleur valide ou rentrez une couleur à la fois.")

])
def test_deviner_couleur(couleur, resultat_attendu):

    couleur_obtenu = deviner_couleur()

    assert couleur_obtenu == resultat_attendu