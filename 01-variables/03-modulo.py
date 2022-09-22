# L'opération modulo est indispensable pour de nombreux algorithmes.
# Elle permet de récupérer le reste d'une division.

# Exemple : 65 % 10 = 5, car 5 est le reste
# En effet, 65 = 6*10 + 5

# Imaginons que l'on souhaite partager les 8 parts de pizza, mais sans les
# couper, et en donnant le même nombre de parts aux 3 personnes.
# Combien de parts va-t-il rester ?

# En utilisant l'opérateur modulo (%), stockez le résultat dans une variable
# remaining_slices

################################################################################
pizza_slices: int = 8
persons: int = 3
################################################################################

# Le modulo permet de savoir facilement si un nombre est pair. Si c'est le cas,
# en le divisant par 2, il n'y a pas de reste (module égal à 0).





























print('\033[92m✓ OK\033[00m' if remaining_slices == 2 else '\033[91m❌KO\033[00m')
