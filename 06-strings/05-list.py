# Une chaîne est un tableau de caractères. Les mêmes opérations sont donc 
# possibles que sur une liste !

# Créez une fonction is_valid_time() qui prend en paramètre un temps au format
# "HHmm" et qui retourne True si le format est valide et si l'heure existe.

################################################################################

################################################################################





































print('\033[92m✓ OK\033[00m' if is_valid_time('2359') and is_valid_time('0000') and not is_valid_time('24') and not is_valid_time('2500') and not is_valid_time('abcd') else '\033[91m❌KO\033[00m')

