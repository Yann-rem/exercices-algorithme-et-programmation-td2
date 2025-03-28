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

# %%

# Exercice 5 : Écrire un script qui prend un nombre en entrée et affiche "pair" ou "impair".

# Demande d'un nombre à l'utilisateur
number = int(input("Entrez un nombre : "))

# Vérification de la parité
if number % 2 == 0:
    print(f"Le nombre {number} est pair.")
else:
    print(f"Le nombre {number} est impair.")


# %%

# Exercice 6 : Créer un script qui demande un mois en entrée et affiche le nombre de jours dans ce mois.

# Demande du mois à l'utilisateur
mois = int(input("Entrez le numéro du mois (1-12) : "))

# Détermination du nombre de jours
if mois in [1, 3, 5, 7, 8, 10, 12]:
    print("Ce mois comporte 31 jours.")
elif mois in [4, 6, 9, 11]:
    print("Ce mois comporte 30 jours.")
elif mois == 2:
    print("Ce mois comporte 28 jours (29 jours si année bissextile).")
else:
    print("Numéro de mois invalide.")

# %%

# Exercice 7 : Écrire un script qui simule un login : demander un nom d'utilisateur et un mot de passe,
# et afficher un message de bienvenue si les informations sont correctes.

# Identifiants préenregistrés
username_saved = "admin"
password_saved = "1234"

# Demande du nom d'utilisateur et du mot de passe
username_input = input("Entrez votre nom d'utilisateur : ")
password_input = input("Entrez votre mot de passe : ")

# Vérification des informations
if username_input == username_saved and password_input == password_saved:
    print(f"Bienvenue, {username_input} !")
else:
    print("Nom d'utilisateur ou mot de passe incorrect.")
