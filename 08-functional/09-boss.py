# ÉTAPE 1
# Vous devez générer une liste "discount_products" qui contiendra uniquement
# les produits discount.
# Pour ces produits, vous devrez ajouter une clé "discount_cost" dont la valeur
# sera calculée en fonction du coût et de la réduction
# Exemple : -25% sur le tournevis, donc discount_cost = 3

# ÉTAPE 2
# Un client commande vos deux articles en promotion.
# Créez un dictionnaire "order" de type Order (type à créer) contenant les clés
# total_cost et total_discount_cost qui sont deux float.
# Calculez dans ce dictionnaire le total des articles, avec le prix original
# et le prix discount.

from typing import TypedDict, NotRequired

class Product(TypedDict):
    name: str
    cost: float
    discount: NotRequired[float]
    discount_cost: NotRequired[float]

products: list[Product] = [
  {
    "name": "Aspi Turbo Max",
    "cost": 150,
    "discount": 50
  },
  {
    "name": "Tournevis",
    "cost": 4,
    "discount": 25
  },
  {
    "name": "Marteau",
    "cost": 10
  }
]

###############################################################################

###############################################################################

# Lorsqu'on travaille avec des types aux propriétés optionnelles, il faut
# vérifier l'existence d'une propriété avant de s'en servir.

























print('\033[92m✓ OK\033[00m' if len(discount_products) == 2 and discount_products[0]['discount_cost'] == 75.0 and discount_products[1]['discount_cost'] == 3.0 and order['total_cost'] == 154 and order['total_discount_cost'] == 78 else '\033[91m❌KO\033[00m')
