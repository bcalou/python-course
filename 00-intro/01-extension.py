# Le code ci-dessous est incorrect (car il essaie d'additionner un entier et
# une chaîne de caractère).

# Essayez de lancer ce programme. La console vous communiquera une erreur.

# Nous allons installer une extension permettant de relever cette erreur
# directement dans notre code, sans attendre l'éxécution.

# Dans le menu des extensions de VSCode, cherchez et installez l'extension
# "Python" de Microsoft. Il peut être nécessaire de redémarrer VSCode.

# Si vous utilisez VSCode, modifiez le paramètre "Type Checking Mode" pour la 
# valeur "basic"

# La ligne de code devrait maintenant être soulignée en rouge, prouvant que
# l'extension fonctionne bien.
# Elle vous aidera à ne pas commettre ce genre d'erreur.

# Si vous voyez "18 + ans" souligné en rouge, c'est bon !

age: int = 18 + "ans"
