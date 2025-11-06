import pytest
from module import *


@pytest.mark.parametrize("code , essai , dictindice", [
                         (["rose","vert","bleu","rouge"],["vert","rose","gris","orange"],{"white":0,"black":2,"null":2})
])
def testpoint(code,essai,dictindice):

    indices=point(code,essai)

    assert dictindice==indices
