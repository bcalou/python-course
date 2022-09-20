# Les nombres décimaux (à virgule) sont très souvent appelé float en
# programmation.

# C'est un type différent des nombres entiers (int), et python ne sera pas
# content si vous mélangez les deux.

# Utilisez le type float pour déclarer une variable qui contiendra le nombre de
# part de pizza par personnes (slices_per_person), en utilisant les deux
# données déjà présentes.

################################################################################
pizza_slices: int = 8
persons: int = 3
################################################################################

print("Résultat: ", slices_per_person)

# Remarquez que, même si vous changez le nombre de personnes pour avoir un
# chiffre rond, vous devrez quand même utiliser un float ! python part du
# principe qu'une division donne toujours un float (même si le chiffre après la
# virgule s'avère nul).






























print('\033[92m✓ OK' if slices_per_person == 8 / 3 else '\033[91m❌KO')