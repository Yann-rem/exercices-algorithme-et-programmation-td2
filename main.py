# %%

# Exercice 1 : Écrire un script Python qui demande un nombre à l'utilisateur et affiche s'il est
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


# %%

# Exercice 3 : Écrire un script qui prend trois nombres en entrée et affiche le plus grand des trois.

# Demande des trois nombres à l'utilisateur
try:
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    nombre3 = float(input("Entrez le troisième nombre : "))

    # Détermination du plus grand nombre
    plus_grand = max(nombre1, nombre2, nombre3)

    # Affichage du résultat
    print(f"Le plus grand nombre est : {plus_grand}")

except ValueError:
    print("Veuillez entrer des nombres valides.")


# %%

# Exercice 4 : Créer un script qui calcule la moyenne de trois notes et affiche si l'étudiant a réussi (moyenne >= 10).

# Demande des trois notes à l'utilisateur
grade1 = float(input("Entrez la première note : "))
grade2 = float(input("Entrez la deuxième note : "))
grade3 = float(input("Entrez la troisième note : "))

# Calcul de la moyenne
average = (grade1 + grade2 + grade3) / 3

# Affichage du résultat
if average >= 10:
    print(f"L'étudiant a réussi avec une moyenne de {average:.2f}")
else:
    print(f"L'étudiant a échoué avec une moyenne de {average:.2f}")
