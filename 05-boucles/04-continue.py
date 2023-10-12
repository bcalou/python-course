# L'opération "continue" est une variante de break : elle stoppe l'itération
# de la boucle, mais pas la totalité du for. Elle demande simplement à passer
# à l'élément suivant, sans exécuter la suite.

for i in [1, 2, 3]:
    print(i)
    continue
    print("Je ne serai jamais exécuté car je suis après continue")

# Cette instruction permet ainsi d'éviter les opérations inutiles ou de sortir
# d'une itération prématurément.

# On souhaite rendre tous les nombres du tableau ci-dessous positifs :
# -5 devient 5, tandis que 1 reste 1

numbers: list[int] = [-5, 1, 7, -6, 0]

# Parcourez le tableau : si vous trouvez un nombre positif, ne faîtes rien
# (grâce à l'instruction "continue"). Pour les autres, inversez-les.

###############################################################################

###############################################################################

# Le mot clé continue est moins souvent utilisé que break, car comme vous
# pouvez le remarquer, il aurait été possible de s'en sortir avec if et une
# condition inverse. Mais c'est un mot-clé à connaître.


























print('\033[92m✓ OK\033[00m' if numbers == [5,1,7,6,0] else '\033[91m❌KO\033[00m')
