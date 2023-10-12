# En reprenant l'exemple compute_salary(), comment faire pour passer un bonus
# sans changer la valeur par défaut de hourly_rate ? 

# Cela devient possible grâce aux paramètres nommés, dont voici un exemple :

def say_hi(name: str = "John"):
    """Print a greetings message"""
    print("Hello " + name)

say_hi(name = "John")

# Avec un seul paramètre, c'est inutile, mais quand ils deviennent nombreux,
# c'est intéressant.

# En effet, compute_salary(35, 20, 1000) est un appel très obscur quand on
# le prend à part. À quoi correspondent ces chiffres ?

# S'ils sont nommés, tout devient plus clair.

# Utilisez un appel nommé pour stocker dans my_salary le résultat de 39 heures
# de travail avec un bonus de 300, sans toucher au salaire horaire.

def compute_salary(hours: int, hourly_rate: int = 10, bonus: int = 0) -> int:
    """Compute the salary depending on the hourly rate and optional bonus"""
    return (hours * hourly_rate) + bonus

###############################################################################

###############################################################################

# Attention : il reste préférable de chercher à créer des fonctions claires,
# prenant peu de paramètres (zéro, un ou deux).



























print('\033[92m✓ OK\033[00m' if my_salary == 690 else '\033[91m❌KO\033[00m')
