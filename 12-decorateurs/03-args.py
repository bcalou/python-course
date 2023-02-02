# Comment faire un décorateur si la fonction décorée prend des paramètres ?
# Par exemple say_hello(name: str) ?
# Quand on renvoit la fonction say_hello décorée, comment savoir quelle valeur
# il faut utiliser en paramètre ?

# Voici la réponse à cette question :

from typing import Callable

def print_before_and_after(function: Callable):
    # On récupère les arguments et on les fait passer
    def wrapper(*args, **kwargs):
        print("Before")
        function(*args, **kwargs) # Idem
        print("After")

    return wrapper

@print_before_and_after
def say_hello(name: str): # La fonction prend désormais un paramètre
    print("Hello", name)

say_hello("jane") # Exécutez et regardez l'output !

# *args représente les arguments classiques et **kwargs les arguments nommés.
# Vous n'avez pas besoin de comprendre le fonctionnement exact : cette syntaxe
# couvre tous les cas, elle ne change jamais.

# Reprenez votre fonction test_duration. Grâce à ces nouvelles informations,
# changez la fonction sort_array pour qu'elle prenne en paramètre le tableau à
# trier : sort_array(array: list[int])

###############################################################################

###############################################################################

# Pas de validation automatique. Appelez sort_array avec plusieurs tableaux
# et vérifiez que tout fonctionne.
