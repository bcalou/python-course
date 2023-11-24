# map() n'est pas la seule fonction de ce type à nous intéresser.

# filter() permet aussi de transformer un tableau en un autre tableau. Mais lui
# ne transforme pas les valeurs, il les filtre en fonction d'une condition, ce
# qui est extrèmement utile.

# Voici par exemple un filtre qui garde uniquement les nombres pairs :

numbers: list[int] = [1, 7, 5, 6, 8, 3]
even_numbers: list[int] = list(filter(lambda number: number % 2 == 0, numbers))

# Le résultat est [6, 8]

# Utilisez un filtre pour créer un tableau "adult_users" contenant uniquement
# les utilisateurs dont l'age est supérieur ou égal à 18.

from typing import TypedDict

class User(TypedDict):
    firstname: str
    lastname: str
    age: int

users: list[User] = [
  {
    "firstname": "John",
    "lastname": "Doe",
    "age": 28
  },
  {
    "firstname": "Jane",
    "lastname": "Doe",
    "age": 32
  },
  {
    "firstname": "Allan",
    "lastname": "Doe",
    "age": 12
  }
]

###############################################################################

###############################################################################






























print('\033[92m✓ OK\033[00m' if len(adult_users) == 2 else '\033[91m❌KO\033[00m')
