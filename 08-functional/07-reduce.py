# La fonction reduce() est très utile lorsqu'on souhaite obtenir une valeur
# unique à partir des différentes valeurs d'un tableau.

# Contrairement à map et filter, elle doit être chargée à partir de la
# librairie native functools (functional tools).

# Voici par exemple comment calculer une somme (bien sûr, il serait plus simple
# d'utiliser la fonction sum() de python)

import functools

numbers: list[int] = [1, 2, 3, 4, 5]
sum_of_numbers: int = functools.reduce(
  lambda total, current: total + current, numbers
)

# La variable "sum_of_numbers" vaut ici 15.
# Il est important de comprendre que "total" contient l'accumulation des
# opérations précédentes à chaque itération.
# À la première itération, total vaut 1 (première valeur) et current vaut
# 2 (seconde valeur).
# Ensuite, total vaut 3 (addition précédente) et current vaut
# 3 (troisième valeur).
# Ensuite, total vaut 6 (addition précédente) et current vaut
# 4 (quatrième valeur).
# Etc...

# Utilisez reduce() pour calculer la somme des nombres du tableau "numbers",
# mais en prenant uniquement les nombres impairs (et sans utiliser filter).

# Stockez le résultat dans une variable odd_numbers_sum.

###############################################################################

###############################################################################

































print('\033[92m✓ OK\033[00m' if odd_numbers_sum == 9 else '\033[91m❌KO\033[00m')
