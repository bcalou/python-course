# Une variable privée est une variable d'une classe qu'on ne peut pas lire de
# l'extérieur (c'est à dire qu'on ne peut pas faire instance.variable).
# Idem pour les méthodes : la classe peut avoir des méthodes internes qu'elle
# n'appelle qu'elle-même.

# Petite décéption, elles n'existent pas en python. Mais une convention bien
# connue les remplace : préfixer les variables et méthodes privées par deux
# underscores "__".

class MyClass:
    def __init__(self, letter: str):
        self.__letter = letter

    def get_letter(self):
        return self.__letter


my_instance = MyClass("o")
# my_instance.__letter  # INTERDIT ! Underscore = variable privées
my_instance.get_letter() # Ok

# Une pratique répandue est d'avoir toutes les variables en privé, et
# d'utiliser des méthodes pour écrire et lire les variables (setters et
# getters). Cela permet de contrôler strictement les règles associées à chaque
# variable.

# En partant de l'exercice précédent, transformez toute les variables de la
# classe User en variables privées.

# Du coup, votre méthode get_oldest() ne peut plus lire l'âge directement.
# Ajoutez un getter approprié pour vous adapter.

# On souhaite que is_adult ne puisse être appelée qu'au sein de la classe
# elle-même : utilisez la convention pour en faire une méthode privée.

###############################################################################

###############################################################################

# On appelle parfois les éléments public d'une classe son interface.

# Note : les tests ne vérifient désormais que l'interface des classes, pas
# leur fonctionnement interne.














test_adult = User("bob", "doe", 18)
test_child = User("child", "doe", 10)
print('\033[92m✓ OK\033[00m' if get_oldest(test_adult, test_child) == "bob doe" else '\033[91m❌KO\033[00m')