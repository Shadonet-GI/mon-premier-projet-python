# je veux rendre mon mini calculateur précedent interactif pour permettre a l'utilisateur de choisir son propre operation

# demander a l'utilisateur de saisir deux nombres
a =float(input("entrer le premier nombre :"))
b =float(input("entrer le deuxieme nombre :"))
# afficher le menu

print("choisissez l'operation :")
print("1- Addition")
print("2-soustraction")
print("3-multiplication")
print("4-division")
print("5-puissance")
print("6-reste de la division")

choix = input("entrer le numero de l'operation:")
# effectuer l'operation choisie
if choix=="1":
   print("resulat :",a+b)
elif choix=="2":
    print("resultat :",a-b)
elif choix=="3":
    print("resultat :",a*b)
elif choix=="4":
    print("resultat :",a/b)
elif choix=="5":
    print("resultat :",a**b)
elif choix=="6":
    print("resultat :",a%b)
else:
    print("choix invalide")
    
# j'ajoute un gestionnaire d'erreure dans mon programme
try:
    a= float(input("entrer un premier nombre"))
    b= float(input("entrer le secong nombre"))
except ValueError:
    print("erreur:vous devez entrer un nombre valide !")
    
        
