# Il est très fréquent de vouloir rendre certaines clés d'un type optionnelles.

# Cela est possible grâce à l'annotation NotRequired[str].
# Note : vous devrez peut-être éxécuter la commande
# "pip install typing_extensions"

from typing import TypedDict
from typing_extensions import NotRequired

class Album(TypedDict):
    artist: str  
    title: str
    year: int
    reviews: NotRequired[list[str]]

# Créez un type "Meal" possédant les clés firstcourse, maincourse
# et desert (entrée, plat principal et dessert). L'entrée et le dessert
# seront optionnels.

# Créez un dictionnaire utilisant ce type.

################################################################################

################################################################################

# Pas de validation automatique pour cet exercice. À nouveau, vérifiez que
# votre éditeur vous informe de vos erreurs. Cette fois, il ne devrait pas
# relever l'absence d'une clé (mais toujours la présence d'une clé innatendue).

# Pour information, la syntaxe suivante rendra TOUTES les clés optionelles
# (notez le total=False) :

class Movie(TypedDict, total=False):
    title: str
    director: str  
    year: int
    reviews: list[str]
