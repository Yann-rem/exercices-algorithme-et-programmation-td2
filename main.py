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


# %%

# Exercice 2 : Créer un script qui demande l'âge de l'utilisateur et affiche s'il est majeur ou mineur.

# Demande de l'âge de l'utilisateur
age = int(input("Quel est votre âge ? "))

# Vérification de la majorité
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
