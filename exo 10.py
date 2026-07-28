print("1. Ajouter un contact")
print("2. Afficher tous les contacts")
print("3. Rechercher un contact par nom")
print("4. Rechercher un contact par son numéro")
print("5. Quitter")
choix = 6
contacts =[]
while choix>5:
    while True:
        try:
            choix=int(input("faites votre choix en utilisant les chiffres des options:"))
            if choix>5 or choix <=0:
                print("numéro invalide réesayer")
                choix =int(input("votre choix:"))
            break
        except ValueError:
                print("numéro invalide réesayer")
    while choix < 5:
        while choix == 1:
            def ajout_de_contact(nom,tel):
                {"Nom":nom,"tel":tel}
                return {"Nom":nom,"tel":tel}


            nom=input("Nom du contact:")
            tel=input("Numéro du contact:")
            contacts.append(ajout_de_contact(nom,tel))
            break
        while choix == 2:
            print(f"{"#"*3} MES CONTACTS {"#"*3}")
            print(contacts)
            break

        while choix == 3:
            def recherche(nom_individu):
                for contact in contacts:
                    for contact in contacts:
                        if contact['Nom'] == nom_individu:
                            print(contact)
                return "FIN DE LA RECHERCHE"


            nom_individu = input("entrez le nom du contact:")
            print(recherche(nom_individu)) 
            break 


        while choix == 4:
            def recherche(numero):
                for contact in contacts:
                    if contact['tel'] == numero:
                        print(contact)
                return "FIN DE LA RECHERCHE"


            numero = input("entrez le numero du contact:")
            print(recherche(numero))
            break
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact par nom")
        print("4. Rechercher un contact par son numéro")
        print("5. Quitter")
        while True:
            try:
                choix =int(input("votre choix:"))
                break
            except ValueError:
                print("ERREUR")
print("vous avez quitter le menu")

