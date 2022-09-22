# Il est possible d'extraire un sous tableau à partir d'un tableau en
# spécifiant un début, une fin, voire les deux.

# list[0:4] donnera tous les éléments d'index 0 à 4 (4 non inclus)
# Le 0 est optionnel : list[:4]

# list[4:] donnera tous les éléments d'index 4 (inclus) à la fin du tableau

# À partir du tableau days, créez un tableau "work_days" qui ne contient pas 
# samedi et dimanche.

days: list[str] = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

################################################################################

################################################################################

# Conseil : utilisez un index négatif en borne finale, plutôt que de compter
# jusqu'où s'arrêter. Vous aurez peut-être besoin de fouiller un peu dans la
# doc de python...










































print('\033[92m✓ OK\033[00m' if work_days == ["Mon", "Tue", "Wed", "Thu", "Fri"] else '\033[91m❌KO\033[00m')
