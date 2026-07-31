Menu="1. Ajouter une recette (+)\n2. Ajouter une dépense (-)\n3. Voir l'historique\n4. Voir le solde\n5. Quitter"
print(Menu)
OPERATIONS=[]
TACHES=[]
TROUVE=True
trouve=True
while TROUVE:
    try:
        choix=int(input("Faites votre choix avec les chiffres du menu"))
        while choix>5:
            print("utiliser les chiffres du menu:")
            choix=int(input("votre choix"))
        TROUVE=False
    except ValueError:
        print("les caracteres ne sont pas autorisés")
while choix<5:
    if choix==1:
        def ajout_recette():
            libelle=input("libelle:")
            montant=float(input(f"montant(en $):"))
            print("✅ Enregistré.")
            {"LIBELLÉ":libelle,"MONTANT":montant}
            return {"LIBELLÉ":libelle,"MONTANT":montant}
        OPERATIONS.append(ajout_recette())
    if choix==2:
        def ajout_depense():
            DEPENSE=input("libelle:")
            montant_depenser=float(input("montant:"))
            print("✅ Enregistré.")
            {"LIBELLÉ":DEPENSE,"MONTANT":montant_depenser}
            return {"LIBELLÉ":DEPENSE,"MONTANT":montant_depenser} 
        TACHES.append(ajout_depense())
    if choix==3:
        print("HISTORIQUE DES RECETTES")
        print(OPERATIONS)
        print("HISTORIQUE DES DEPENSES")
        print(TACHES)
    if choix==4:
        def calcul_recette():
            total=0
            for operation in OPERATIONS:
                total+=operation['MONTANT']
            return total
        def calcul_depense():
            TOTAL=0
            for taches in TACHES:
                TOTAL+=taches['MONTANT']
            return TOTAL
        print(f"Solde = {calcul_recette()-calcul_depense()} $")
        if calcul_recette()-calcul_depense()<0:
            print("vous etes endetté de",calcul_recette()-calcul_depense(),"$")
        else:
            print("il vous reste",calcul_recette()-calcul_depense(),"$")
    print(Menu)
    while trouve:
        try:
            choix=int(input("Faites votre choix avec les chiffres du menu"))
            while choix>5:
                print("utiliser les chiffres du menu:")
                choix=int(input("votre choix"))
            break
        except ValueError:
            print("les caracteres ne sont pas autorisés")
print("vous avez quitter le menu")

        
            
            
    

                        