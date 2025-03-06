# %%

# Exercice 1 : écrire un script Python qui demande un nombre à l'utilisateur et affiche s'il est
# positif, négatif ou nul.

# Demander à l'utilisateur d'entrer un nombre
nombre = float(input("Entrez un nombre : "))

# Vérifier si le nombre est positif, négatif ou nul
if nombre > 0:
    print("Le nombre est positif.")
elif nombre < 0:
    print("Le nombre est négatif.")
else:
    print("Le nombre est nul.")
