Zackary Ritchie
test de la fonction points

| # | essayer de l'utilisateur | combinaison            | Résultat attendu       | Résultat observé       |
|---|--------------------------|------------------------|------------------------|------------------------|
| 1 | rose,vert,bleu,rouge     | vert,rose,gris,orange  | white:0,black:2,null:2 | white:0,black:2,null:2 |
| 2 | vert,vert,vert,vert      | vert,vert,vert,vert    | white:4,black:0,null:0 | white:4,black:0,null:0 |
| 3 | rose,rose,rose,rose      | rouge,bleu,jaune,rouge | white:0,black:0,null:4 | white:0,black:0,null:4 |
| 4 | bleu,vert,bleu,vert      | vert,bleu,vert,bleu    | white:0,black:4,null:0 | white:0,black:4,null:0 |
| 5 | bleu,bleu,rouge orange   | bleu,vert,orange,jaune | white:1,black:1,null:2 | white:1,black:1,null:2 |

Uwumwami Peace Sammy/
test de la fonction deviner_couleur

| # | Entré utilisateur simulé          | Résultat attendu                    | explication                           | 
|---|-----------------------------------|-------------------------------------|---------------------------------------|
| 1 | rose, bleu, jaune, vert           | ["rose", "bleu", "jaune", "vert"]   | couleurs enregistrées dans la liste   |
| 2 | pomme -> rouge, bleu, vert, jaune | ["rouge", "bleu", "vert", "jaune"]  | on redemande pour la couleur          |
| 3 | rouge, rouge, bleu, blanc         | ["rouge", "rouge", "bleu", "blanc"] | la couleur est enregistrer 2 fois     |
| 4 | BLEU, vert, jaUne, Rouge          | ["bleu", "vert", "jaune", "rouge"]  | il y a la fonction lower              |
| 5 | gris, , orange, bleu              | ["gris", ...?, "orange", "bleu"]    | on demande pour la couleur qui manque |
| 6 | camion ->bleu, jaune, vert, rose  | ["bleu", "jaune", "vert", "rose"]   | on redemande pour la couleur          |


Abel Lopis
test de la fonction generer_masque

| # | Entré utilisateur simulé          | Résultat attendu                    | explication                           | 
|---|-----------------------------------|-------------------------------------|---------------------------------------|
| 1 | rose, bleu, jaune, vert           | ["rose", "bleu", "jaune", "vert"]   | couleurs enregistrées dans la liste   |
| 2 | zebre -> rouge, bleu, vert, jaune | ["rouge", "bleu", "vert", "jaune"]  | on redemande pour la couleur          |
| 3 | bleu, rouge, bleu, blanc          | ["rouge", "rouge", "bleu", "blanc"] | la couleur est enregistrer 2 fois     |
| 4 | BLEU, vert, jaUne, Rouge          | ["bleu", "vert", "jaune", "rouge"]  | il y a la fonction lower              |
| 5 | gris, , orange, bleu              | ["gris", ...?, "orange", "bleu"]    | on demande pour la couleur qui manque |
| 6 | bateau ->bleu, jaune, vert, rose  | ["bleu", "jaune", "vert", "rose"]   | on redemande pour la couleur          |