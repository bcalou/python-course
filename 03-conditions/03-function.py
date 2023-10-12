# Une fonction peut retourner le résultat d'une comparaison.

# La fonction is_centenary renvoit true si l'âge passé en paramètre est
# supérieur ou égal à 100.

# Créez une fonction can_drink qui prend en premier paramètre "USA" ou
# "France", et en second paramètre l'âge de la personne.
# Cette fonction doit retourner un booléen.

def is_centenary(age: int) -> bool:
    """Return true if the given age is above 100"""
    return age >= 100

###############################################################################

###############################################################################

























print('\033[92m✓ OK\033[00m' if not can_drink("USA", 20) and can_drink("USA", 21) and not can_drink("France", 17) and can_drink("France", 18) else '\033[91m❌KO\033[00m')
