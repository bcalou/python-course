# Un type de variable très courant est l'entier.

# En plus de la variable déjà présente, créez trois nouvelles variables :
# seconds_per_minute
# minutes_per_hour
# hours_per_day

# Donnez leur la valeur appropriée puis lancez le programme pour valider.

################################################################################
milliseconds_per_seconds: int = 1000
################################################################################

# Note : le typage n'est pas obligatoire pour que le programme fonctionne,
# mais c'est une habitude que nous allons prendre pour rendre le plus explicite
# possible nos intentions























print('\033[92m✓ OK\033[00m' if seconds_per_minute == 60 and minutes_per_hour == 60 and hours_per_day == 24 else '\033[91m❌KO\033[00m')