# nombre=int(input("entrez un nombre:"))
# parite = nombre%2
# message= 0
# while not parite == 0 and message== 0:
#     print(f"le nombre {nombre} est impair")
#     message= message+1
# if parite==0:
#   print(f"le nombre {nombre} est pair")
# print("marie"=="Marie")
# print(10>5)               
# print(10 == "10")                
# print(3 > 2 and 2 > 1)           
# print(not (5 == 5))              
# print("art"< "base")
# print("e"< "yrt")
# nombre=int(input("entrez un nombre:"))
# if nombre< 0:
#     print(f"{nombre} est négatif")
# elif nombre == 0:
#     print(f"{nombre} est nul")
# else:
#     print(f"{nombre} est positif")

# nombre=int(input("entrez un nombre:"))
# if nombre%2==0:
#     print("pair")
# else:
#     print("impair")
# table=7
# for i in range(1,11):
#     print(f"{table} * {i} = {table*i}")
# mot="dimitri"
# for lettre in mot:
#     print(f"{lettre}")
# total=0
# for i in range(101):
    # total=total+i #autre notation (total += i)
# print(total)
# for i in range(2,22,2):
#     print(i)
# for i in range(21):
    # if i%2==0:
        # print(i)





## Exercice 1 — Majeur ou mineur 🔞
# > 🎯 **But** : écrire un premier `if / elif / else` correctement **indenté**.
# Demande l'âge et affiche `"Majeur"` ou `"Mineur"`. Ajoute un cas d'erreur si l'âge est négatif.
# identite=False
# while not identite:
#     age= int(input("votre age:"))
#     if age< 18 and age>0:
#         print("Mineur")
#         identite= True
#     elif age >= 18:
#         print("Majeur")
#         identite= True
#     else:
#         print("erreur reesayer:")





## Exercice 2 — L'appréciation 📊

# > 🎯 **But** : gérer **plusieurs cas** en chaînant des `elif` dans le bon ordre.

# Demande une note sur 20 et affiche : `Excellent` (≥16), `Bien` (≥12), `Passable` (≥10),
# `À revoir` (< 10). *(Pense à `elif`.)*
# note=int(input("votre note:"))
# while note<0 or note>20:
#     print("ERREUR")
#     note=int(input("votre note:"))
# if note>=16:
#     print("excellent")
# elif note>=12:
#     print("Bien")
# elif note>=10:
#     print("passable")
# else:
#     print("A revoir")






## Exercice 3 — Compte à rebours 🚀

# > 🎯 **But** : maîtriser `range` **à l'envers** (avec un pas négatif) dans une boucle `for`.

# Affiche un compte à rebours de 10 jusqu'à 0, puis « Décollage ! ».

# ```
# 10 9 8 7 6 5 4 3 2 1 0
# Décollage ! 🚀
# ```

# > 🔎 Cherche comment `range` peut compter **à l'envers** (indice : un pas négatif).

# for i in range(10,-1,-1):
#     print(i)
# print("DÉCOLLAGE")






## Exercice 4 — La somme des nombres ➕

# > 🎯 **But** : appliquer le motif **« accumuler dans un total »** avec une boucle.

# Demande un nombre `n`, puis calcule et affiche la somme de **tous** les nombres de 1 à `n`.

# ```
# n : 5
# Somme = 15   (1+2+3+4+5)
# ```
# nombre=int(input("entrez un nombre:"))
# somme=0
# for i in range(1,nombre+1):
#     print(f"{somme} + {i} = {somme+i}")
#     somme= somme + i
# print(f"somme= {somme}")        









## Exercice 5 — Table de multiplication 🔢

# > 🎯 **But** : utiliser la variable de boucle `i` dans un **calcul** à chaque tour.

# Demande un nombre, puis affiche sa table de multiplication de 1 à 10.
# nombre=int(input("entrez un nombre:"))
# for i in range(1,11):
#     print(f"{nombre} * {i} = {nombre*i}")







## Exercice 6 — FizzBuzz 🐝 (le classique des entretiens !)

# > 🎯 **But** : combiner **boucle + conditions + modulo**, et comprendre l'importance de
# > l'**ordre** des tests.

# Affiche les nombres de 1 à 30, mais :

# - si le nombre est divisible par **3**, affiche `Fizz` à la place ;
# - s'il est divisible par **5**, affiche `Buzz` ;
# - s'il est divisible par **3 et 5**, affiche `FizzBuzz`.

# ```
# 1, 2, Fizz, 4, Buzz, Fizz, 7, ... , 14, FizzBuzz, 16, ...
# ```

# > 🔎 Indice : teste le cas « 3 **et** 5 » **en premier**. Utilise `%` et `and`.
# for i in range (1,31):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)





## Exercice 7 — Défi : mot de passe 🔐

# > 🎯 **But** : utiliser une boucle **`while`** qui répète jusqu'à une bonne réponse.

# Redemande un mot de passe **tant que** l'utilisateur ne tape pas `"python123"`.
# Affiche « Accès autorisé » quand c'est bon. *(Boucle `while`.)*
# mot_de_passe="python123"
# identifiant=input("entrez le mot de passe:")
# while  not identifiant == mot_de_passe:
#     print("mot de passe incorrect")
#     identifiant=input("entrez le mot de passe:")
# print("mot de passe correct")




## Exercice 8 — Grand défi 🌟 : améliore « Devine le nombre »

# > 🎯 **But** : assembler **tout le niveau** (variables, `while`, `if`, compteur) et intégrer
# > un module cherché seul·e (`random`).

# Reprends le jeu de la leçon 3.4 et ajoute :

# 1. un nombre **aléatoire** (module `random`) ;
# 2. un **compteur d'essais** affiché à la fin ;
# 3. un **nombre limité d'essais** (ex : 5). Perdu si dépassé.
# import random
# secret=90
# trouve=True  # trouve = False
# tentatives=5
# while trouve and tentatives<=5 and tentatives>0:  # While True avec not trouve = TRUE . while not False = while True:tant que la condition est vraie executer le programme or la condition est toujours true donc le programme s'execute. 
#      proposition=int(input("je pense a un nombre entre 10 et 68, Devine le en 5 essais"))
#      tentatives= tentatives - 1
#      if proposition==secret:
#         print("bravo vous avez devinez le nombre")
#         trouve=False   # donc not trouve vas devenir false et le programme vas s'arreter
#      elif proposition>secret:
#         print("le nombre entré est trop grand")
#      else:
#         print("le nombre entré est trop petit")
# if proposition!= secret:
#     print("vous avez perdu")
# else:
#     print(f"vous avez fini le jeu en {5-tentatives} tentatives")


# NIVEAU 4
### LISTES
# prenoms=["Dimitri","wilfrid","fructueux","mannelle"] # liste permet de stocker plusieurs variables elle est hétérogène  
# print(prenoms[0]) # appel du premier élément de la liste
# print(prenoms[1])
# print(prenoms[2])
# print(prenoms[3])
# print(prenoms[-1]) # appel du dernier élément de la liste il est utilisée pour des listes dont la taille est inconnue
# print(len(prenoms)) # Taille de la liste
# print(len(prenoms)-1) # indice du dernier élément de la liste
# ## modifier une liste
# # changer une valeur par son indice
# prenoms[2] = "freelance"  # fructueux devient freelance
# print(prenoms)
# ## ajout d'un nom à la liste grâce à la fonction append()  
# prenoms.append("roméo") # nom ajoutée
# print(prenoms)
# ##  supprimer une valeur grâce à la fonction remove()
# prenoms.remove("wilfrid") # suppression par sa valeur
# print(prenoms)
# ## supprimer une valeur grâce à la fonction pop()
# prenoms.pop(0) # suppression par son indice
# print(prenoms)
# # > `.append()`, `.remove()`, `.pop()` sont des **méthodes** : 
# # des fonctions « attachées »
# #  à la liste, qu'on appelle avec un **point**. 
# # > Retiens la syntaxe `ma_liste.methode(...)`.
# prenoms.insert(2,"dimitri")
# print(prenoms)
# print("PYTHON" in prenoms)
# print("freelance" in prenoms)
# for PRENOM in prenoms: # parcourt chaque prenom de la liste
#     print(f"salut {PRENOM}") # affiche chaque nom
# for i in range(len(prenoms)): # génére 0,1,2,3
#     print(f"{i+1}. {prenoms[i]}") # affiche les noms grâce à prenoms[i] qui récupére l'élément de cet indice
# notes=[12,20,14,6,9,10]
# total=0
# for note in notes:
#      total+= note
# print(f"somme = {total}")
# print(f"Moyenne = {round(total/len(notes),2)}")
# print(sum(notes))
# print(max(notes))
# print(min(notes))
# compteur=0
# max=notes[0]
# min=notes[0]
# for note in notes:
#     if note >10:
#         compteur+=1
# print(f"{compteur} nombres dépassent 10")
#     if note > max:
#         max = note
#     elif note < min:
#         min = note
# print(f"{max} est le maximum de la liste")
# print(f"{min} est le minimum de la liste")
# for i , prenom in enumerate(prenoms):
#     print(i+1,prenom)
# nombres = [12, 45, 7, 89, 23, 56, 91, 34, 18, 72, 5, 67, 39, 81, 14]
# vide=[]
# for nombre in nombres:
#     if nombre%2==0 :
#         vide.append(nombre)
# print(vide)

### DICTIONNAIRES          
# personne = {"Nom": "dimitri","age": 17,"teint": "noir","e-mail":"fagbegnondimitri@gmail.com"} # Dictionnaire
# print(personne["teint"]) #affiche les éléments du dictionnaire
# print(personne["e-mail"])#affiche les éléments du dictionnaire
# print(personne.get("tel", "unknown")) # affiche unknown car la clé tel n'existe pas
# personne["tel"]= "0166123445" # Ajout de la clé "tel" et de sa valeur
# del personne["age"] #suppression d'une clé et de sa valeur
# print(personne) # affichage des couples clés-valeur
# print(personne.items()) # AFFICHE LES COUPLES (CLÉ,VALEUR)
# for caracteristiques, caracteres in personne.items(): # PARCOURT TOUT LE DICTIONNAIRE avec caracteristiques les clés et caracteres les valeurs
#     print(f"{caracteristiques}:{caracteres}") # AFFICHE LA CLÉ : VALEUR
# print(personne.keys()) #affichage des clés uniquement
# print(personne.values()) #affichage des valeurs uniquement
# for caracteres in personne: #parcourt les clés
#     print(caracteres) # affiche les clés

### LISTES DE DICTIONNAIRES
# contacts=[ # listes de dictionnaires
#     {"Nom":"ITACHI","tel":"015928"},
#     {"Nom":"eren","tel":"014182"},
# ]
# for contact in contacts: # parcourt la liste contacts
#     print(f"{contact['Nom'] , contact['tel']}") # affiche les valeurs contenues dans chaque dictionnaire
# print("age" in personne) # vérifie qu'une clé appartient a un dictionnaire avant de l'utiliser

###  COMPTE DU NOMBRES D'APPARITION DES ÉLÉMENTS D'UNE LISTE GRACE A UN DICTIONNAIRE
# animal=["chat","chien","chien","crabe","chien","chat","chien","chat","crabe","chat","crabe"]
# compteur={} # dictionnaire vide qui servira de compteur
# for mot in animal: # parcourt chaque valeur de la liste animal
#     if mot in compteur: # si le mot est dans le dictionnaire compteur alors
#         compteur[mot]+= 1 # prends la valeur précédente du mot ou clé et y ajoute 1 cela permet de compter les apparitions de chaque mot
#     else: #sinon
#         compteur[mot]=1 # ajoute une clé (mot) qui aura pour valeur 1 c-a-d compteur={"mot": 1} ainsi de suite et cela pour chaque mot
# print(compteur)
##Autre methode de comptage
#     compteur[mot]=compteur.get(mot,0)+1 # verifie d'abord que la clé(mot) existe ou appartient a compteur et si ce n'es pas le cas alors get(mot,0) renvoie la valeur 0 qui va s'ajouter a +1 pour permettre l'ajout de la clé(mot) au dictionnaire compteur ainsi de suite pour les autres mots et quand la clé existe déja alors get(mot,0) renvoie la valeur précédemment enrégistrer et l'ajoute a 1 pour compter le nombre d'apparitions
# print(compteur)

### FONCTIONS
# def age():
#     # age=int(input("votre age:"))
    # nom=input("votre nom:")
    # mois=input("votre mois de naissance:")
    # print(f"{nom} vous aurez {age+1} ANS en {mois} prochain")
    # print("j'espere que votre entourage vous fera une belle surprise je dis ca je dis rien ah ")
# age()
# def personne(nom,age):
#     print(f"{nom} vous avez {age} ans")
# personne("christ",19)
# def addition(a,b):
#     return a+b
# resultat= addition(10,45)
# print(resultat)
# print(addition(10,45))
# def est_majeur(age):             # retourne un BOOLÉEN
#     return age >= 18
# print(est_majeur(15))
# if est_majeur(20):
#      print("acces autorisé")
# def moyenne(notes):
#     return sum(notes)/len(notes)
# print(moyenne([12,13,13,20])) # pour avoir plusieurs elements comme le cas suivant utilise des crochets[]
# def saluer(nom="l'ami"): # la valeur au parametre nom a deja ete donnée ici
#     print(f"bonjour {nom}")
#     saluer() # fonction récursive a chaque fois que la fonction finit d'afficher bonjour nom elle se rencontre elle meme or en elle meme il y a encore elle meme ainsi de suite. c'est une fonction récursive
# def saluer(nom="l'ami"): # la valeur au parametre nom a deja ete donnée ici
#     print(f"bonjour {nom}")
# saluer() # plus besoin d'ecrire la valeur de nom
# print(saluer()) # affiche None
# def dire_bonjour(): 
#     print("Bonjour")
# resultat = dire_bonjour()
# print(resultat) #affiche bonjour et ensuite None. une fonction qui ne retourne rien affiche toujours None apres avoir executé son programme

###fonction paires
# def pair(n):
#     return n%2==0
# for i in range(1,21):
#     print(pair(i))

# def calcul_mean(notes):
#     return sum(notes)/ len(notes)

# def appreciation(moyenne):
#     if moyenne>=10:
#         return"accepté"
#     return "refuse"
# moyenne=calcul_mean([7,3,6])
# print("la moyenne est ",moyenne)
# print(appreciation(moyenne))






