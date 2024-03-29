# Il est également possible de préciser un peu mieux le nombre d'occurences
# souhaitées.

# a{3} demande la lettre a trois fois
# a{3,} demande la lettre a trois fois ou plus
# a{3,6} demande la lettre a entre trois et six fois

# Voici un exemple :

import re

match = re.search('(hello){2,}', 'hellohello')
if match:
    print("La chaîne contient hello au moins deux fois")

# Grâce à cela, vous allez encore pouvoir simplifier la vérification du numéro
# de version ! (rappel : 0.0 ou 0.0.0)

###############################################################################
def is_valid_version(version: str) -> bool:
    return True
###############################################################################


























print('\033[92m✓ OK\033[00m' if is_valid_version("0.2") and is_valid_version("0.2.2") and not is_valid_version("a0.2") and not is_valid_version("0.2a") and not is_valid_version("0!2") and not is_valid_version("0.2.2.2") else '\033[91m❌KO\033[00m')

