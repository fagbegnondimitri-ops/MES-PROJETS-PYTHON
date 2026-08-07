from datetime import date 
import datetime
import json
import pprint

try:
    with open("C:/Users/USER/Documents/MES-PROJETS-PYTHON/EXOS PYTHON/mini.json","r") as json_file:
        CLIENTS=json.load(json_file)
        print(type(CLIENTS))
        pprint.pprint(CLIENTS,sort_dicts=False,width=50)
except FileNotFoundError:
    CLIENTS=[]
    with open("mini.json","w") as json_file:
            json.dump(CLIENTS,json_file)

print("1.Ajouter un client\n2.Afficher tous les clients\n3.Rechercher un client\n4.Modifier\n5.Supprimer\n6.Ajouter une interaction\n7.Voir les relances à faire\n8.Sauvegarde automatique")
while True:
      try:
        CHOIX=int(input("faites votre choix en utilisant les chiffres des options:"))
        if CHOIX>7 or CHOIX <=0:
            print("numéro invalide réesayer")
            CHOIX =int(input("votre choix:"))
        break
      except ValueError:
        print("numéro invalide réesayer")

while CHOIX>0 and CHOIX<8:
    if CHOIX==1:
        def ajout_client():
                while True:
                    nom= input("NOM DE L'ENTREPRISE:").strip()
                    if nom!="":
                        break
                    else:
                        print("ce champ est obligatoire")

                while True:
                    contact= input("CONTACT:").strip()
                    if nom!="":
                        break
                    else:
                        print("ce champ est obligatoire")
        

                while True:
                    e_mail= input("E-MAIL:").strip()
                    if nom!="":
                        break
                    else:
                        print("ce champ est obligatoire")  

                while True:
                        tel= input("TÉLÉPHONE:").strip()
                        if nom!="":
                            break
                        else:
                            print("ce champ est obligatoire")

                while True:
                        statut= input("STATUT:").strip()
                        if nom!="":
                            break
                        else:
                            print("ce champ est obligatoire")      
                date_de_modification=None
                date1=date.today()
                return {"ENTREPRISE":nom,"CONTACT":contact,"E_MAIL":e_mail,"TEL":tel,"STATUT":statut,"DATE_DE_CREATION":str(date1),"DATE_DE_MODIFICATION":date_de_modification,"INTERACTIONS":[]}
        CLIENTS.append(ajout_client())

    if CHOIX==2:
        def affiche_client():
            if CLIENTS==[]:
                print("AUCUN CLIENT")
            else:
                pprint.pprint(CLIENTS, sort_dicts=False, width=50)
            
        if __name__ == "__main__":
            affiche_client()
            
    if CHOIX==3:
        def recherche_client():
            i=0
            recherche= input("Nom du client rechercher:")
            for client in CLIENTS:
                if client['CONTACT'].lower()== recherche.lower():
                    pprint.pprint(client,sort_dicts=False,width=50)
                    i+=1
            if i==0:
                print("CONTACT INEXISTANT")
        if __name__ == "__main__":
            recherche_client()

    if CHOIX==4:
        def modifie_client():
            i=0
            print("Saissisez les informations de l'entreprise à modifier")
            recherche_nom= input("NOM DE L'ENTREPRISE:")
            recherche_contact= input("CONTACT:")
            recherche_e_mail= input("E-MAIL")
            recherche_tel= input("TÉLÉPHONE:")
            recherche_statut= input("STATUT:")
            for client in CLIENTS:
                if recherche_nom.lower() ==client['ENTREPRISE'].lower() and recherche_contact.lower() == client['CONTACT'].lower() and recherche_e_mail.lower()== client['E_MAIL'] and recherche_tel.lower() == client['TEL'] and recherche_statut.lower()== client['STATUT']:
                    print("Saissisez les modifications")
                    client['ENTREPRISE']=input("NOM DE L'ENTREPRISE:")
                    client['CONTACT']=input("NOUVEAU CONTACT:")
                    client['E_MAIL']=input("NOUVELLE E-MAIL:")
                    client['TEL']=input("TÉLÉPHONE:")
                    client['STATUT']=input("NOUVEAU STATUT:")
                    client['DATE_DE_MODIFICATION']=str(date.today())
                    i+=1
                if i==1 :
                    if client['INTERACTIONS']!=[]:
                        REPONSE=input("Voulez vous modifier une interaction?(oui/non)")
                        if REPONSE.lower()=="oui":
                            ANNEE= input("ancienne annee d'interaction:")
                            mois= input("ancien mois d'interaction:")
                            jour= input("ancien jour d'interaction:")
                            recherche_type= input("ancien type d'interaction:")
                            recherche_note= input("ancienne note d'interaction:")
                            date=str(date(ANNEE,mois,jour))
                            for interaction in client['INTERACTIONS']:
                                if recherche_type.lower()==interaction['TYPE'].lower() and recherche_note.lower() == interaction['NOTE'].lower() and date== interaction['DATE']:
                                    interaction['TYPE']= input("Nouveau type d'interaction:")
                                    interaction['NOTE']= input("Nouvelle note d'interaction")
                                    ANNEE1= input("nouvelle annee d'interaction:")
                                    mois1= input("nouveau mois d'interaction:")
                                    jour1= input("nouveau jour d'interaction:")
                                    interaction['DATE']=str(date(ANNEE1,mois1,jour1))
                        else:
                            print("BIEN RECU")
            if i==0:
                print("CONTACT INEXISTANT")

        if __name__ == "__main__":
            modifie_client()

    if CHOIX==5:
        def supprime_client():
                recherche_nom= input("NOM DE L'ENTREPRISE:")
                recherche_contact= input("CONTACT:")
                recherche_e_mail= input("E-MAIL")
                recherche_tel= input("TÉLÉPHONE:")
                recherche_statut= input("STATUT:")
                for client in CLIENTS:
                    if recherche_nom.lower() ==client['ENTREPRISE'].lower() and recherche_contact.lower() == client['CONTACT'].lower() and recherche_e_mail.lower()== client['E_MAIL'] and recherche_tel.lower() == client['TEL'] and recherche_statut.lower()== client['STATUT']:
                        reponse=input ("Voulez vous vraiment supprimer les informations de cet client(oui/non)?")
                        if reponse.lower()== "oui":
                            CLIENTS.remove(client)
                        else:
                            print("Annulation de la suppression")
                    pprint.pprint(CLIENTS,sort_dicts=False,width=50)
        if __name__ == "__main__":
            supprime_client()

    if CHOIX==6:
        def interaction_client():
            global date1
            recherche_nom= input("NOM DE L'ENTREPRISE:")
            recherche_contact= input("CONTACT:")
            recherche_e_mail= input("E-MAIL")
            recherche_tel= input("TÉLÉPHONE:")
            recherche_statut= input("STATUT:")
            for client in CLIENTS:
                if recherche_nom.lower() ==client['ENTREPRISE'].lower() and recherche_contact.lower() == client['CONTACT'].lower() and recherche_e_mail.lower()== client['E_MAIL'] and recherche_tel.lower() == client['TEL'] and recherche_statut.lower()== client['STATUT']:
                    annee=int(input("Année d'interaction"))
                    mois=int(input("Mois d'interaction"))
                    jour=int(input("jour d'interaction"))
                    type=input("Type d'interaction:")
                    note=input("note d'interaction")
                    date1=date(annee,mois,jour)
                    client['INTERACTIONS'].append({"DATE":str(date1),"TYPE":type,"NOTE":note})
        if __name__ == "__main__": 
            interaction_client()
        

    if CHOIX==7:
        def relance_client():
            i=0
            for client in CLIENTS:
                if client['INTERACTIONS']==[]:
                    Duree=date.today()- datetime.datetime.strptime(client['DATE_DE_CREATION'],"%Y-%m-%d").date() 
                else:
                    Duree=date.today()-date1
                if Duree.days>=30:
                    print(client)
                    i+=1
            if i==0:
                print("aucun client n'a été oublié")
        if __name__ == "__main__": 
            relance_client()
    with open("C:/Users/USER/Documents/MES-PROJETS-PYTHON/EXOS PYTHON/mini.json","w") as json_file:
                json.dump(CLIENTS,json_file,indent=4)
    while True:
                try:
                    CHOIX =int(input("votre choix:"))
                    break
                except ValueError:
                    print("ERREUR")
print("Vous avez quitter le menu")

            









