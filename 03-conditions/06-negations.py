# Le mot clé "not", devant une condition, permet de tester son inverse

# Créez une variable "can_drink" qui sera true si is_sober est vraie et si
# is_minor est faux (en utilisant le mot clé "not")

age: int = 17
is_sober: bool = True
is_minor: bool = age < 18

################################################################################

################################################################################

print(can_drink)




































print('\033[92m✓ OK\033[00m' if not can_drink else '\033[91m❌KO\033[00m')
