# L'opérateur ternaire est présent dans de nombreux langages : il permet
# d'écrire un if/else en une seule ligne.

# Voici l'exemple de l'exercice précédent, mis à jour pour utiliser cette
# syntaxe :

def get_age_range(age: int) -> str:
    """Return whether this person is an adult or a minor"""
    return "Adult" if age >= 18 else "Minor"

# La condition se lit naturellement.

# Reprenez la fonction get_max et adaptez là à cette nouvelle syntaxe.

###############################################################################

###############################################################################

# Attention ! Cette syntaxe est à réserver aux conditions courtes et simples.
# La lisibilité du code doit toujours primer.






























print('\033[92m✓ OK\033[00m' if get_max(8, 4) == 8 and get_max(5, 3) == 5 and get_max(2, 2) == 2 else '\033[91m❌KO\033[00m')
