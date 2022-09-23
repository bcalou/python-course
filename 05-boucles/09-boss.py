# En mathématiques, la suite de Fibonacci est une suite d'entiers dans laquelle
# chaque terme est la somme des deux termes qui le précèdent (Wikipédia).

# En voici le début (on choisit arbitrairement 0 et 1 pour débuter) :
# 0, 1, 1, 2, 3, 5, 8...

# Écrivez une fonction find_in_fibonacci_suite()
# Cette fonction prendra un tableau d'entiers.
# La fonction doit retourner le premier entier de la listequi appartient à la
# suite de Fibonacci (ou 0 si aucun ne correspond).

# Exemple : [584, 987, 2] donne 987 (premier élément de la liste correspondant)

################################################################################

################################################################################

find_in_fibonacci_suite([584, 987, 2])

# D'abord, trouvez comment faire. Votre première version sera peut-être un peu
# brute de décoffrage et peu optimisée. C'est alors la seconde partie du
# travail qui commence : clarifiez et optimisez votre code.


































print('\033[92m✓ OK\033[00m' if find_in_fibonacci_suite([1, 15, 75]) == 1 and find_in_fibonacci_suite([584, 987, 2]) == 987 and find_in_fibonacci_suite([144, 50, 89]) == 144 and find_in_fibonacci_suite([16, 87, 154]) == 0 else '\033[91m❌KO\033[00m')
