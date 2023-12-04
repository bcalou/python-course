# Le propre d'une classe est de posséder un ou plusieurs attributs.

# Voici une classe qui possède trois attributs : letter, number et array.

class MyClass:
    array: list[int] = []

    def __init__(self, letter: str, number: int):
        self.letter: str = letter
        self.number: int = number


my_instance = MyClass("a", 1)

# La variable array est un attribut dont la valeur sera automatiquement fixée
# à chaque instance.
# Les deux autres attributs sont passés en paramètre à l'instanciation de la
# classe.

# Modifiez votre classe User pour qu'elle possède les attributs :
# - firstname
# - lastname
# - age
# - adult (attention, cette propriété ne doit pas être passée à la
# méthode __init__ mais directement déduite de l'âge. Un adulte a 18 ans ou
# plus dans notre programme)
# - followers (cette propriété n'est pas non plus passée à la méthode, elle
# vaut automatiquement 0 au départ)

# Créez une variable "bob" qui sera un utilisateur nommé "Bob Doe" ayant 18
# ans.

###############################################################################

###############################################################################

























print('\033[92m✓ OK\033[00m' if isinstance(bob, User) and bob.firstname == "Bob" and bob.lastname == "Doe" and bob.age == 18 and bob.adult and bob.followers == 0 else '\033[91m❌KO\033[00m')
