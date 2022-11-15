# Il peut être utile de parcourir un dictionnaire pour tester ou effectuer
# une opération sur chacune de ses valeurs.

# L'écriture de la boucle est de type :
# for key in dictionnary
# Vous pouvez remplacer key par le nom que vous voulez : utilisez
# des noms explicites !

# Trouvez la note la plus élevée du dictionnaire "notes" et stockez le nom de
# la matière associée dans une variable best_course

from typing import TypedDict

class Notes(TypedDict):
    math: int
    french: int
    english: int

notes: Notes = {
    "math": 8,
    "french": 15,
    "english": 20
}

################################################################################

################################################################################

# Il est également possible d'itérer directement sur les valeurs grâce à
# dictionnary.values()
# Il est même possible d'utiliser dictionnary.items() pour itérer sur un tuple
# [clé, valeur]


































print('\033[92m✓ OK\033[00m' if best_course == "english" else '\033[91m❌KO\033[00m')
