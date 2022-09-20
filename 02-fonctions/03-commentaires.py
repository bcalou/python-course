# Une fonction évidente est une bonne fonction. Pour aider à cela, nous allons
# prendre l'habitude de décrire le but de nos fonctions dans un commentaire
# introductif.

# Sur le modèle de get_square_surface, décrivez le comportement de la fonction
# get_square_perimeter dans un commentaire introductif.

################################################################################
def get_square_surface(size: float) -> float:
    """Get the surface of a square of the given size"""
    return size * size


def get_square_perimeter(size: float) -> float:
    return size * 4
################################################################################

# Une fonction peut se passer de commentaire quand son nom est parfaitement
# clair. Mais mieux vaut commencer par prendre l'habitude de toutes les
# commenter, par défaut.
