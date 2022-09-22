# Les paramètres peuvent prendre des valeurs par défaut : ils deviennent
# alors optionnels.

# Dans l'exemple suivant, si aucun paramètre n'est passé, la valeur "John" sera
# utilisée.

def say_hi(name: str = "John"):
    """Print a greetings message"""
    print("Hello " + name)

# Créez une fonction compute_salary, prenant trois paramètres :
# hours, entier obligatoire
# hourly_rate, entier optionnel (valeur par défaut : 10)
# bonus, entier optionnel (valeur par défaut : 0)

# La fonction doit retourner le salaire, qui correspond à la multiplication
# des heures par le salaire horaire, à laquelle s'ajoute le bonus.

################################################################################

################################################################################


































print('\033[92m✓ OK\033[00m' if compute_salary(35, 20, 1000) == 1700 and compute_salary(35, 20) == 700 and compute_salary(35) == 350 else '\033[91m❌KO\033[00m')
