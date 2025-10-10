# nous allons importer les fonctions que nous avons saisie dans le fichier opereation.py et nous allons effectuer les calcules dans cette version du mini calculateur
import operations # me permet d'importer mes fonctions dans le fichier operations.py

def main():
    while True:
        print("\n== mini calculateur v3==")
        try:
            a = float(input("entrer le premier nombre :"))
            b = float(input("entrer le deuxieme nombre :"))
        except ValueError:
            print("erreur : veuillez entrer un nombre valide")
            continue
        print("\nchoisissez l'operation:")
        print("1.Addition")
        print("2.soustraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Puissance")
        print("6.Racine du premier nombre")
        
        choix = input("entrer votre choix (1-6) :")
        
        if choix=="1":
            print("résultat :",operations.addition(a,b))
        elif choix=="2":
            print("résultat:", operations.soustraction(a,b))
        elif choix=="3":
            print("resultat:", operations.multiplication(a,b))
        elif choix=="4":
            print("resultat :",operations.division(a,b))
        elif choix=="5":
            print("resultat :", operations.division(a,b))
        elif choix=="6":
            print("resultat :", operations.racine(a))
        else:
            print("choix invalide !")
            
if __name__=="__main__":
    main()
            
            

            
    