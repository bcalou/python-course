# Des fonctions utilitaires permettent de modifier la casse des chaînes :

# string.upper() pour passer en majuscule
# string.lower() pour passer en minuscule
# string.title() pour ajouter une lettre en début de chaque mot

# Écrivez une fonction are_equal_strings() qui prend en paramètre deux chaînes
# et renvoit true si elles sont identiques SANS tenir compte de la casse

################################################################################

################################################################################







































print('\033[92m✓ OK\033[00m' if are_equal_strings("test", "TEST") and are_equal_strings("test", "test") and are_equal_strings("TeST", "TEsT") and not are_equal_strings("test", "teste") else '\033[91m❌KO\033[00m')
