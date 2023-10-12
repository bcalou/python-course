# Combinaison de else et de if, elif permet de tester une autre condition si la
# précédente à échoué. On peut en faire suivre autant que nécessaire.

# On peut finir (ou non) par un else classique, qui sera exécuté si toutes les
# conditions ont été ignorées.

# if (condition):
#   ...
# elif (condition):
#   ...
# else
#   ...

# Créez une fonction get_mention qui retourne la mention correspondant à une 
# note au bac.
# "Très bien" à partir de 16
# "Bien" à partir de 14
# "Assez bien" à partir de 12
# "Passable" à partir de 10
# "Rattrapage" en dessous de 10

###############################################################################

###############################################################################

print(get_mention(17))




















print('\033[92m✓ OK\033[00m' if get_mention(7) == "Rattrapage" and get_mention(11) == "Passable" and get_mention(12) == "Assez bien" and get_mention(15.5) == "Bien" and get_mention(20) == "Très bien" else '\033[91m❌KO\033[00m')
