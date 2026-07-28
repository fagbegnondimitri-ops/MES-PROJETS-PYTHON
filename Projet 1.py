print("1. Ajouter une tache")
print("2. Afficher une tache")
print("3. Supprimer une tache")
print("4. Quitter")
choix = 6
tache =[]
while choix>4:
    while True:
        try:
            choix=int(input("faites votre choix en utilisant les chiffres des options:"))
            if choix>4 or choix <=0:
                print("numéro invalide réesayer")
                choix =int(input("votre choix:"))
            break
        except ValueError:
            print("numéro invalide réesayer")
    while choix < 4:
        while choix == 1:
            def ajout_de_tache():
                ajout=input("Tache:")
                print("✅Ajouter")
                return ajout

            tache.append(ajout_de_tache())
            break
        while choix == 2:
            print(f"{"#"*3} MA LISTE DE TACHE {"#"*3}")
            i=0
            for taches in tache:
                i += 1
                print(f"{i}. {taches}")
            break
       
        while choix == 3:
            def suppression(indice):
                for j in range(len(tache)):
                        if indice==j+1:
                            tache.pop(j)
                j=0
                for taches in tache:
                    j += 1
                    print(f"{j}. {taches}")
                                           
                
                return "fin de la suppression"
            while True:
                try:
                    indice = int(input("Quel tache voulez vous supprimer.Utiliser les numeros de tache:"))
                    break
                except ValueError:
                    print("utiliser les numéros de tache")
            if indice>len(tache) or indice<=0:
                print("la tache N° ",indice," n'existe pas" )
                while True:
                        print("faites un autre choix")
                        break
            else:
                print(suppression(indice))
                
            break
        while True:
            try:
                choix =int(input("votre choix:"))
                break
            except ValueError:
                print("ERREUR")
print("vous avez quitter le menu de gestion des taches")

            

                    
       