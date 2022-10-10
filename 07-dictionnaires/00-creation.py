# Un dictionnaire est un ensemble de clé / valeurs.

# Le dictionnaire user ci dessous possède une clé "firstname" ayant la valeur
# "Patrick".
# Ajoutez lui un attribut "lastname" ayant pour valeur "Sébastien"
# Ajoutez lui un attribut "year_of_birth" ayant pour valeur 1953
# Ajoutez lui un attribut booleen "french" ayant la valeur True

################################################################################
user = {
    "firstname": "Patrick"
}
################################################################################

# Dans d'autres langages, le dictionnaire est parfois appelé "objet" ou
# "tableau associatif"










































print('\033[92m✓ OK\033[00m' if user['firstname'] == "Patrick" and user['lastname'] == "Sébastien" and user['year_of_birth'] == 1953 and user['french'] == True else '\033[91m❌KO\033[00m')