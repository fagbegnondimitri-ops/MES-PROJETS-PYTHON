Question=[
    {"question":"l'anime qui met en valeur la liberte?", "reponse":"l'attaque des titans"},
    {"question":"le meilleur groupe coreen?", "reponse":"SAJAS BOYS"},
    {"question":"le surnom de GUNS dans BERSERK apres son integration dans l'unite de griffith?", "reponse":"le tueur de 100 hommes"},
    {"question":"qui a cree le souffle de la lune", "reponse":"KOKUSHIBO"},
    {"question":"LE FANTOME DES UCHIWAS?", "reponse":"MADARA UCHIWA"},
    {"question":"LE NOM DE LA LIMACE DE TSUNADE?", "reponse":"KATSUYU"},
    {"question":"QUI A CREE LE RASENGAN?", "reponse":"ASHURA OTSUTSUKI"},
    {"question":"QuI A CREE LE CHIDORI?", "reponse":"INDRA OTSUTSUKI"},
    {"question":"LE NOM DU PREMIER MEMBRE DE LA BRIGADE FANTOME A MOURIR", "reponse":"uvoguine"},
    {"question":"EREN A T'IL PU ATTEINDRE LA LIBERTÉ?", "reponse":"NON"},
    {"question":"DE QUEL CATEGORIES DE NEN EST KURAPIKA?", "reponse":"MATERIALISATION ET SPECIALISATION"},
]
score = 0
for question in Question:
    print(question['question'])
    Reponse = input("REPONSE:").lower()
    if Reponse == question['reponse'].lower():
        score += 1
        print("✅ Correct !")
    else:
        print(f"❌ Faux. La réponse était :{question['reponse']}")
if score>=10 :
    print("bravo")
    print(f"VOTRE SCORE EST DE {score}/{len(Question)}")
else:
    print("bravo")
    print(f"VOTRE SCORE EST DE {score}/{len(Question)}")
    print("tu es trop stérile intellectuellement prrrrr")