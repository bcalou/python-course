# Il est pratique de pouvoir séparer une chaîne en plusieurs sous-chaînes en
# fonction d'un séparateur.

# L'opération split() le permet et renvoit un tableau contenant les différentes
# chaînes.

# "one-two-three".split('-') -> ["one", "two", "three"]

# join() permet l'opération inverse :

# '-'.join(["one", "two", "three"]) -> "one-two-three"

# Transformez la liste des ingrédients en tableau, retirez le fromage, et
# reformatez la chaîne ainsi : "tomato ~ lettuce ~ pickles"

################################################################################
ingredients: str = "tomato, cheese, lettuce, pickles"
################################################################################



























print('\033[92m✓ OK\033[00m' if ingredients == "tomato ~ lettuce ~ pickles" else '\033[91m❌KO\033[00m')
