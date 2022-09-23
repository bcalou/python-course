# Il est souvent nécessaire de faire une boucle allant de 0 à n, sans se baser
# sur un tableau existant. 

# Pour cela, on peut générer la boucle automatiquement grâce à range.

for i in range(3):
    print(i)

# La boucle ci dessus sera exécutée avec les valeurs 0, 1, 2.

# La fonction range peut prendre jusqu'à trois paramètres :
# start, stop et step (voir la documentation)

# Créez une fonction "factorial" prenant en entrée un nombre et retournant
# sa factorielle.

# Exemple : la factorielle de 4 est 1*2*3*4 = 24

################################################################################

################################################################################


































print('\033[92m✓ OK\033[00m' if factorial(10) == 3628800 and factorial(11) == 39916800 else '\033[91m❌KO\033[00m')
