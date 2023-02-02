# Attention : si on décore une fonction qui renvoit quelque chose, il faut
# faire attention à renvoyer cette valeur dans la fonction décorée.

# Voici comment faire :

from typing import Callable

def print_before_and_after(function: Callable):
    def wrapper(*args, **kwargs):
        print("Before")
        # On stocke le résutat (car on a encore des choses à faire)
        result = function(*args, **kwargs) 
        print("After")

        return result # On retourne le résultat

    return wrapper

@print_before_and_after
def say_hello(name: str) -> str:
    # La fonction ne fait plus un print mais renvoit une valeur
    return "Hello " + name

print(say_hello("jane")) # Exécutez et regardez l'output !

# Vous devriez observer que l'ordre des print a changé :
# Before, After, Hello Jane
# En effet, la fonction est exécutée PUIS on print le résultat de cette
# fonction. Le print ne se fait plus dans la fonction elle-même.

# À nouveau, mettez à jour votre code.
# sort_array doit maintenant retourner le tableau trié.
# test_duration doit renvoyer la valeur de la dernière itération.

###############################################################################

###############################################################################

# Pas de vérification automatique. Vérifiez que vous récupérez bien le tableau
# trié.

# Faîtes systématiquement un return : on ne sait jamais quelle fonction on va
# décorer. Au pire, vous retournerez None.