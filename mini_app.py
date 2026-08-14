# IMPORT DES MODULES

from datetime import date 
import datetime
import json
from pathlib import Path

# CRÉATION OU LECTURE DU FICHIER JSON
DOSSIER=Path(__file__).parent/"mini.json"

try:
    with open(DOSSIER,"r",encoding="utf-8") as json_file:
        CLIENTS=json.load(json_file)
except FileNotFoundError:
    CLIENTS=[]
    with open(DOSSIER,"w",encoding="utf-8") as json_file:
            json.dump(CLIENTS,json_file,ensure_ascii=False,indent=4)

# FONCTION DU CHOIX

def MENU():
    while True:
        print("1.Ajouter un client\n2.Afficher tous les clients\n3.Rechercher un client\n4.Modifier\n5.modifier interaction\n6.supprimer\n7.Ajouter une interaction\n8.Relances à faire\n9.QUITTER")
        try:
            choix_menu=int(input("faites votre choix en utilisant les chiffres des options:"))
            if choix_menu>9 or choix_menu <=0:
                print("numéro invalide réesayer")
                print("1.Ajouter un client\n2.Afficher tous les clients\n3.Rechercher un client\n4.Modifier\n5.modifier interaction\n6.supprimer\n7.Ajouter une interaction\n8.Relances à faire\n9.QUITTER")
                choix_menu =int(input("votre choix:"))
            else:
                break
        except ValueError:
            print("numéro invalide réessayer")
    return choix_menu
CHOIX=MENU()

# FONCTION DU CHOIX POUR LA SUPPRESSION ET LA MODIFICATION

def choix(i,verbe):
    while True:
        try:
            choix_modifier=int(input(f"Saisir le numéro du resultat à {verbe}:"))
            while choix_modifier<=0 or choix_modifier>i+1:
                print(f"ERREUR le numéro doit être entre 1 et {i+1}")
                choix_modifier=int(input(f"Saisir le numéro du resultat à {verbe}:"))
            break            
        except ValueError:
            print("le choix doit être un entier")
    return choix_modifier
# FONCTION DU CHAMP OBLIGATOIRE NON VIDE

def vide(variable,message):
    while True:
        variable= input(message).strip()
        if variable!="":
            break
        else:
            print("ce champ est obligatoire")
    return variable

# FONCTION POUR LE CONTROLE DE LA VALEUR DU STATUT

def controle(statut,message):
    CONTROLE=["client","inactif","prospect"]
    l=0
    while True:
        statut= input(message).strip()
        for controle in CONTROLE: 
            if statut.lower()==controle:
                l+=1
                break
        if l==0:
            print("choisissez entre client,inactif et prospect pour définir le statut")
        else:
            break
    return statut

    

# PROGRAMME PRINCIPAL

while CHOIX>0 and CHOIX<9:

    # FONCTION D'AJOUT D'UN CLIENT

    def ajout_client():
        nom=vide("",message="NOM DE L'ENTREPRISE:")
            
        contact=vide("","NOM DU CLIENT:")

        e_mail=vide("","E_MAIL:") 

        tel=vide("","NUMÉRO DE TÉLÉPHONE:")

        statut=controle("","STATUT:")  

        date_de_modification=None

        date1=date.today()

        return {"ENTREPRISE":nom,"CONTACT":contact,"E_MAIL":e_mail.lower(),"TEL":tel,"STATUT":statut.lower(),"DATE_DE_CREATION":str(date1),"DATE_DE_MODIFICATION":date_de_modification,"INTERACTIONS":[]}

    # FONCTION D'AFFICHAGE 

    def affiche_client():
        if CLIENTS==[]:
            print("AUCUN CLIENT")
        else:
            print(f"{"__"*7} CLIENTS {"__"*7}")
            for i,client in enumerate(CLIENTS):
                print(f"{"**"*3} CLIENT {i+1} {"**"*3}")
                print(f"ENTREPRISE :  {client['ENTREPRISE']}")
                print(f"CONTACT :  {client['CONTACT']}")
                print(f"E-MAIL :  {client['E_MAIL']}")
                print(f"NUMÉRO DE TÉLÉPHONE :  {client['TEL']}")
                print(f"STATUT :  {client['STATUT']}")
                for j,interaction in enumerate(client['INTERACTIONS']):
                    print(f"** INTERACTION {j+1} **")
                    print(f"DATE :  {interaction['DATE']}")
                    print(f"TYPE :  {interaction['TYPE']}")
                    print(f"NOTE :  {interaction['NOTE']}")
            
    # FONCTION POUR LA RECHERCHE       
    
    def recherche_client():
        resultats=0
        i=0
        recherche=vide("","Nom du client rechercher:")
        RECHERCHE=[]
        for client in CLIENTS:
            if client['CONTACT'].lower()== recherche.lower():
                resultats+=1
                RECHERCHE.append(client)
        print(f"{"_"*10}RÉSULTATS{"_"*10}")
        print(f"{resultats} résultats trouvés")
        for cherche in RECHERCHE:
            print(f"{"**"*2} RÉSULTATS {i+1} {"**"*2}")
            print(f"ENTREPRISE :  {cherche['ENTREPRISE']}")
            print(f"CONTACT :  {cherche['CONTACT']}")
            print(f"E-MAIL :  {cherche['E_MAIL']}")
            print(f"NUMÉRO DE TÉLÉPHONE :  {cherche['TEL']}")
            print(f"STATUT :  {cherche['STATUT']}")
            i+=1
        if resultats==0:
            print("CONTACT INEXISTANT")

    # FONCTION POUR MODIFIER LES INFOS DU CLIENT

    def modifie_client():
        date2=date.today()
        RECHERCHE=[]
        print("Saissisez les informations du client à modifier")
        recherche_contact=vide("","NOM DU CLIENT:")
        for client in CLIENTS:
            if recherche_contact.lower() == client['CONTACT'].lower():
                RECHERCHE.append(client)
        for i,recherche in enumerate(RECHERCHE):
            print(f"{"**"*2} CLIENTS {i+1} {"**"*2}")
            print(f"ENTREPRISE :  {recherche['ENTREPRISE']}")
            print(f"CONTACT :  {recherche['CONTACT']}")
            print(f"E-MAIL :  {recherche['E_MAIL']}")
            print(f"NUMÉRO DE TÉLÉPHONE :  {recherche['TEL']}")
            print(f"STATUT :  {recherche['STATUT']}")
        if RECHERCHE!=[]:
            choix_modifier=choix(i,"modifier")
            for client in CLIENTS:
                for i,recherche in enumerate(RECHERCHE):
                    if choix_modifier==i+1 and client==recherche:
                            client['ENTREPRISE']=vide("","NOM DE L'ENTREPRISE:")
                            client['CONTACT']=vide("","NOUVEAU CONTACT:")
                            client['E_MAIL']=vide("","NOUVELLE E-MAIL:")
                            client['TEL']=vide("","TÉLÉPHONE:")
                            client['STATUT']=controle("","NOUVEAU STATUT:")
                            client['DATE_DE_MODIFICATION']=str(date2)
        else:
            print("CONTACT INEXISTANT")

    # FONCTION POUR MODIFIER LES INTERACTIONS D'UN CLIENT

    def modifie_interaction():
        compteur=0
        compteur1=0
        print("Saissisez les informations du client à modifier")
        recherche_contact=vide("","NOM DU CLIENT:")
        for client in CLIENTS:
            if recherche_contact.lower()== client['CONTACT'].lower():
                compteur+=1
                if client['INTERACTIONS']!=[]:
                    compteur1+=1
                    for i,interaction in enumerate(client['INTERACTIONS']):
                        print(f"{"**"*2} INTERACTION {i+1} {"**"*2}")
                        print(f"DATE :  {interaction['DATE']}")
                        print(f"TYPE :  {interaction['TYPE']}")
                        print(f"NOTE:  {interaction['NOTE']}")
                    choix_interaction= choix(i,"modifier") 
                    for i,interaction in enumerate(client['INTERACTIONS']):  
                        if choix_interaction==i+1:
                            while True:
                                try:       
                                    ANNEE1=int(input("Entrez la nouvelle annee d'interaction:"))
                                    mois1=int(input("Entrez le nouveau mois d'interaction:"))
                                    jour1=int(input("Entrez le nouveau jour d'interaction:"))
                                    date3=date(ANNEE1,mois1,jour1)
                                    while date3>date.today():
                                        print("Vous ne pouvez pas avoir eu une interaction à une date supérieure à aujourd.hui,réessayer")
                                        ANNEE1=int(input("Entrez la nouvelle annee d'interaction:"))
                                        mois1=int(input("Entrez le nouveau mois d'interaction:"))
                                        jour1=int(input("Entrez le nouveau jour d'interaction:"))
                                        date3=date(ANNEE1,mois1,jour1)
                                    break
                                except ValueError:
                                    print("Les informations entrées ne sont pas du bon type,réessayer")
                            interaction['DATE']=str(date3)
                            interaction['TYPE']=vide("","Entrez le nouveau type d'interaction:")
                            interaction['NOTE']=vide("","Entrez la nouvelle note prise lors de cette interaction:")
                        

        if compteur==0:
                print("CONTACT INEXISTANT") 
        else:
            if compteur1==0:
                print("AUCUNE INTERACTION N'A ÉTÉ TROUVÉE POUR CET CLIENT")                                      

    # FONCTION POUR SUPPRIMER UN CLIENT DE LA BASE DE DONNÉES
                      
    def supprime_client():
        RECHERCHE=[]
        print("Saissisez les informations du client à supprimer")
        recherche_contact=vide("","NOM DU CLIENT:")
        for client in CLIENTS:
            if recherche_contact.lower() == client['CONTACT'].lower():
                RECHERCHE.append(client)
        for i,recherche in enumerate(RECHERCHE):
            print(f"{"**"*2} RÉSULTATS {i+1} {"**"*2}")
            print(f"ENTREPRISE :  {recherche['ENTREPRISE']}")
            print(f"CONTACT :  {recherche['CONTACT']}")
            print(f"E-MAIL :  {recherche['E_MAIL']}")
            print(f"NUMÉRO DE TÉLÉPHONE :  {recherche['TEL']}")
            print(f"STATUT :  {recherche['STATUT']}")
        if RECHERCHE!=[]:
            choix_remove=choix(i,"supprimer")
            for client in CLIENTS:
                for i,recherche in enumerate(RECHERCHE):
                    if choix_remove==i+1 and client==recherche:
                        trouve=True
                        while trouve:
                            reponse=input ("Voulez vous vraiment supprimer les informations de cet client(oui/non)?:")
                            if reponse.lower()=="oui" or reponse.lower()=="non":
                                trouve=False
                            else:
                                print("RÉPONDEZ PAR OUI/NON")
                        if reponse.lower()== "oui":
                            CLIENTS.remove(client)
                        elif reponse.lower()=="non":
                            print("Annulation de la suppression")
            if reponse.lower()== "oui":        
                for i,client in enumerate(CLIENTS):
                    print(f"{"**"*4} CLIENT {i+1} {"**"*4}")
                    print(f"ENTREPRISE :  {client['ENTREPRISE']}")
                    print(f"CONTACT :  {client['CONTACT']}")
                    print(f"E-MAIL :  {client['E_MAIL']}")
                    print(f"NUMÉRO DE TÉLÉPHONE :  {client['TEL']}")
                    print(f"STATUT :  {client['STATUT']}")
                    for i,interaction in enumerate(client['INTERACTIONS']):
                        print(f"** INTERACTION {i+1} **")
                        print(f"DATE :  {interaction['DATE']}")
                        print(f"TYPE :  {interaction['TYPE']}")
                        print(f"NOTE:  {interaction['NOTE']}")
        else:
            print("CONTACT INEXISTANT")
            
    # FONCTION POUR AJOUTER UNE INTERACTION

    def interaction_client():
        i=0
        recherche_contact=vide("","NOM DU CLIENT:")
        RECHERCHE=[]
        for client in CLIENTS:
            if recherche_contact.lower() == client['CONTACT'].lower():
                i+=1 
                RECHERCHE.append(client)
        print(f"{"_"*10}RÉSULTATS{"_"*10}")
        print(f"{i} résultats trouvés")
        for j,cherche in enumerate(RECHERCHE):
            print(f"{"**"*2} RÉSULTATS {j+1} {"**"*2}")
            print(f"ENTREPRISE :  {cherche['ENTREPRISE']}")
            print(f"CONTACT :  {cherche['CONTACT']}")
            print(f"E-MAIL :  {cherche['E_MAIL']}")
            print(f"NUMÉRO DE TÉLÉPHONE :  {cherche['TEL']}")
            print(f"STATUT :  {cherche['STATUT']}")
            for k,interaction in enumerate(cherche['INTERACTIONS']):
                print(f"{"**"*2} INTERACTION A{k+1} {"**"*2}")
                print(f"DATE :  {interaction['DATE']}")
                print(f"TYPE :  {interaction['TYPE']}")
                print(f"NOTE:  {interaction['NOTE']}")
        if RECHERCHE!=[]:
            choix_ajout=choix(j,"qui vous voulez ajouter une interaction")
            for client in CLIENTS:
                for j,cherche in enumerate(RECHERCHE):                    
                    if choix_ajout==j+1 and client==cherche:
                        while True:
                            try:       
                                ANNEE=int(input("Entrez l'annee d'interaction:"))
                                mois=int(input("Entrez le mois d'interaction:"))
                                jour=int(input("Entrez le jour d'interaction:"))
                                date4=date(ANNEE,mois,jour)
                                while date4>date.today():
                                    print("Vous ne pouvez pas avoir eu une interaction à une date supérieure à aujourd.hui,réessayer")
                                    ANNEE=int(input("Entrez l'annee d'interaction:"))
                                    mois=int(input("Entrez le mois d'interaction:"))
                                    jour=int(input("Entrez le jour d'interaction:"))
                                    date4=date(ANNEE,mois,jour)
                                break
                            except ValueError:
                                print("Les informations entrées ne sont pas du bon type,réessayer")
                        type_interaction=vide("","Type d'interaction:")
                        note=vide("","note d'interaction:")
                        client['INTERACTIONS'].append({"DATE":str(date4),"TYPE":type_interaction,"NOTE":note})
        if i==0:
            print("CONTACT INEXISTANT")
        
    # FONCTION POUR AFFICHER LES CLIENTS À RELANCER
     
    def relance_client():
        i=0
        RELANCES=[]
        date5=date.today()
        for client in CLIENTS:
            if client['INTERACTIONS']==[]:
                Duree=date5- datetime.datetime.strptime(client['DATE_DE_CREATION'],"%Y-%m-%d").date() 
            else:
                DATES=[]
                for interaction in client['INTERACTIONS']:
                    DATES.append(interaction['DATE'])
                Duree=date5-datetime.datetime.strptime(max(DATES),"%Y-%m-%d").date()
                        
            if Duree.days>=30:
                RELANCES.append(client)
                i+=1
        if i==0:
            print("aucun client n'a été oublié")
        else:
            print(f"{"__"*7} RELANCES {"__"*7}")
            for i,relances in enumerate(RELANCES):
                    print(f"{"**"*3} CLIENT {i+1} {"**"*3}")
                    print(f"ENTREPRISE :  {relances['ENTREPRISE']}")
                    print(f"CONTACT :  {relances['CONTACT']}")
                    print(f"E-MAIL :  {relances['E_MAIL']}")
                    print(f"NUMÉRO DE TÉLÉPHONE :  {relances['TEL']}")
                    print(f"STATUT :  {relances['STATUT']}")
                    for j,interaction in enumerate(relances['INTERACTIONS']):
                        print(f"** INTERACTION {j+1} **")
                        print(f"DATE :  {interaction['DATE']}")
                        print(f"TYPE :  {interaction['TYPE']}")
                        print(f"NOTE:  {interaction['NOTE']}")

     #               
    

    # ATTRIBUTION DES FONCTIONS

    if CHOIX==1:
        CLIENTS.append(ajout_client())

    if CHOIX==2:
        affiche_client()

    if CHOIX==3:
        recherche_client()

    if CHOIX==4:
        modifie_client()

    if CHOIX==5:
        modifie_interaction()

    if CHOIX==6:
        supprime_client()

    if CHOIX==7:
        interaction_client()

    if CHOIX==8:
        relance_client()

    
        

    with open(DOSSIER,"w",encoding="utf-8") as json_file:
                json.dump(CLIENTS,json_file,indent=4,ensure_ascii=False)
    
    while True:
        print("1.Ajouter un client\n2.Afficher tous les clients\n3.Rechercher un client\n4.Modifier\n5.modifier interaction\n6.supprimer\n7.Ajouter une interaction\n8.Relances à faire\n9.QUITTER")
        try:
            CHOIX =int(input("votre choix:"))
            if CHOIX>9 or CHOIX<=0:
                print("NUMÉRO INVALIDE")
            else:
                break
        except ValueError:
            print("ERREUR")
if CHOIX==9:
    print("Vous avez quitter le menu")

            









