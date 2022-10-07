# Programme de conversion d'unité
# 1Pouce(inch) = 2,54cm
# 1Centimètres(cm) = 0.394inch
# 17inch = 43.18cm (17*2,54)
#cm = inch*2,54
#inch = cm/2,54

def cmToInch(cm):
    inch = str(cm/2.54)
    return inch


def inchToCm(inch):
    cm = str(inch*2.54)
    return cm


while True:
    print("1 - pouces vers cm")
    print()
    print("2 - cm vers pouces")
    print()
    print("3 - Sortir du programme")
    print()
    choix = int(input("Quel conversion voulez vous réaliser? "))
    print()
    if choix == 1:
        valeur = int(
            input("Entrez un nombre de pouces que vous souhaitez convertir en cm "))
        resultat = inchToCm(valeur)
        print()
        print(f"{valeur}inch est égale à {resultat}cm")
    elif choix == 2:
        valeur = int(
            input("Entrez un nombre de centimètres que vous souhaitez convertir en pouces "))
        resultat = cmToInch(valeur)
        print()
        print(f"{valeur}cm est égale à {resultat}inch")
    elif choix == 3:
        print()
        print("Fin du programme")
        quit()
    else:
        print()
        print("ERREUR: choisissez entre 1, 2 où 3")
