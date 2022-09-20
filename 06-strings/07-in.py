# L'opérateur "in" permet de savoir si une chaîne est présente dans une autre.
# Voici un exemple :

"y" in "Python"  # true 
"x" in "Python"  # false

# Écrivez une fonction is_valid_sentence() qui retourne True si la chaîne
# passée en paramètre ne contient aucun des mots interdits contenus dans le
# tableau forbidden_words (sans tenir compte de la casse)

forbidden_words: list[str] = ["mince", "zut", "oups", "damned", "fichtre"]

################################################################################

################################################################################


































print('\033[92m✓ OK' if is_valid_sentence("Bien le bonjour") and not is_valid_sentence("Mince alors !") and not is_valid_sentence("Je suis en retard, fichtre !") else '\033[91m❌KO')
