# ceci est un prrogramme python qui permet de conertir une temperature entrée par l'utilisateur
print("bonjour nous voulons convertir une temperature que vous aurez fourni de celsius en farenrheit et vice vers ça")




print("choisissez le type de conversion")
print("1- celsius vers fahrenheit")
print("2- fahrenheit vers celsius")

choix=input("entrer le numero de la conversion")

if choix== "1":
    celsius = float(input("entrez la temperature"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°c = {fahrenheit}°f")
elif choix== "2":
    fahrenheit = float(input("entrez la temperature "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°f = {celsius}°c")
else:
    print("choix non disponible tapez un ou deux")
    
    
    
    
    
    


    
    