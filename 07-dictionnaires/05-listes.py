# Une liste peut contenir des dictionnaires, et un dictionnaire peut contenir
# des listes !

# Creéz un tableau "students" qui contiendra 3 dictionnaires de type "Student"
# que vous aurez créé. Typez bien le tableau pour qu'il ne puisse contenir que
# des dictionnaires de type "Student".

from typing import TypedDict

class Student(TypedDict):
    firstname: str
    lastname: str
    notes: list[int]

###############################################################################

###############################################################################






































print('\033[92m✓ OK\033[00m' if len(students) == 3 else '\033[91m❌KO\033[00m')
