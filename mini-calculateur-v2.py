# ceci est un mini calculateur amélioré avec une boucle
import math

while True: 
    print("\n===mini calculateur===")
    
    try:
        a = float(input("entrer le premier nombre :"))
    except  ValueError:
        print("erreur: entrer un nombre valide ")
        continue
    operateur = input("choisissez une operation(+,-,*,/,sqrt):")
    # si l'opération sqrt est choisie,elle n'a besoin que d'un seul nombre
    if operateur== "sqrt":
        print("résultat :",math.sqrt(a))
    else:
          try:
              b = float(input("entrer un deuxieme nombre :"))
          except ValueError:
              print("erreur: entrer un nombre valide")
              continue
    if operateur=="+":
        print("resultat :",a+b)
    elif operateur=="-":
        print("resultat :",a-b)
    elif operateur=="*":
        print("resultat :",a*b)
    elif operateur=="/":
        if b==0:
            print("erreur : division par 0 interdite")
        else:
            print("resultat :",a/b)
    # demander a l'utilisateur si il veut recommencer
    choix = input("\nSouhaitez-vous faire un autre calcul ? (o/n) : ")
    if choix.lower() != "o":
        print("👋 Merci d’avoir utilisé le mini calculateur !")
        break
                
        
        
        
        