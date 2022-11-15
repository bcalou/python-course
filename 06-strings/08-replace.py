# La fonction replace() remplace toute les occurences d'une chaîne par une
# autre.

"python".replace("y", "x")  # pxthon

# Écrivez une fonction replace_with_roman_numerals qui remplace les chiffres de
# 1 à 10 par leur équivalent en chiffre romains dans une chaîne donnée

# Exemple : "Je lis le chapitre 3" -> "Je lis le chapitre III"

roman_numerals: list[str] = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

################################################################################

################################################################################




































print('\033[92m✓ OK\033[00m' if replace_with_roman_numerals("Bonjour") == "Bonjour" and replace_with_roman_numerals("Je lis le chapitre 4") == "Je lis le chapitre IV" and replace_with_roman_numerals("Je lis le chapitre 10") == "Je lis le chapitre X" and replace_with_roman_numerals("5 janvier") == "V janvier" else '\033[91m❌KO\033[00m')