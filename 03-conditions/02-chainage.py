# Il est également possible de chaîner les comparateurs.

# Voici un exemple :

all_equals = 5 == 10 == 15

# Écrivez une fonction is_ascending(), prenant en paramètre trois nombres et
# renvoyant True si les nombres sont triés par ordre croissant

# La suite (1, 1, 2) est considérée comme croissante.

################################################################################

################################################################################



































print('\033[92m✓ OK' if is_ascending(1, 1, 2) and is_ascending(-5, 0, 5) and not is_ascending(1, 0, 2) else '\033[91m❌KO')