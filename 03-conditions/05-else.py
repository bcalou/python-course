# Grâce à l'instruction "else", vous pouvez dire ce qui doit se passer si le
# "if" correspondant n'a pas été utilisé (voir la fonction d'exemple).

# Créez une fonction get_max prenant deux nombres en paramètres et retournant
# le plus grand des deux.

def get_age_range(age: int) -> str:
    """Return whether this person is an adult or a minor"""
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
        
###############################################################################

###############################################################################























print('\033[92m✓ OK\033[00m' if get_max(8, 4) == 8 and get_max(5, 3) == 5 and get_max(2, 2) == 2 else '\033[91m❌KO\033[00m')
