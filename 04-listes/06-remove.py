# Les fonctions remove et pop permettent de retirer des valeurs d'un tableau.

# Remove retire la première valeur correspondante trouvée :
# [7, 8, 8, 9].remove(8) -> [7, 8, 9]

# pop permet de retirer une valeur en fonction de son index :
# [7, 8, 8, 9].pop(1) -> [7, 8, 9]

# Retirez les éléments intrus dans le tableau des voyelles

voyels: list[str] = ['A', 'E', 'X', 'I', 'O', 'X', 'U', 'Y']

###############################################################################

###############################################################################

# Non, il n'existe pas de méthode removeAll() en python... (mais d'autres
# astuces sont envisageables)








































print('\033[92m✓ OK\033[00m' if voyels == ["A", "E", "I", "O", "U", "Y"] else '\033[91m❌KO\033[00m')
