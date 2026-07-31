Question=[
    {"question":"Quel est le nom de la ville où Eren, Mikasa et Armin ont grandi ?", "reponse":"Demon slayer"},
    {"question":"Quel Titan Ymir (le personnage) possède-t-elle ?", "reponse":"HAINE"},
    {"question":"Quel est le nom du capitaine qui dirige l'Escouade d'opérations spéciales dont fait partie Eren ?", "reponse":"Livai ackerman"},
    {"question":"Quel est le nom du pere d'eren ?", "reponse":"GRISHA YEAGER"},
    {"question":"Qui est le seul survivant de la charge suicidaire d'erwin?", "reponse":"Floch forster"},
]
Question=[
    {"question":"Qui est surnommé la panthere de jade de konoha?", "reponse":"GUY MAITO"},
    {"question":"le SURNOM DE SHISUI UCHIWA?", "reponse":"le MIRAGE"},
    {"question":"Le nom du perso le plus intelligents de NARUTO", "reponse":"SHIKAMARU NARA"},
    {"question":"LE FANTOME DES UCHIWAS QUI EST CE?", "reponse":"MADARA UCHIWA"},
    {"question":"LE NOM DE LA LIMACE DE TSUNADE?", "reponse":"KATSUYU"},
]
Question=[
    {"question":"Quel est le surnom de light yagami?", "reponse":"kira"},
    {"question":"Quel était le vrai métier de Naomi Misora avant de rencontrer Light ?", "reponse":"agent du fbi"},
    {"question":"Quel est le nom du shinigami qui donne le Death Note à Light au début de l'histoire ?", "reponse":"Ryuk"},
    {"question":"Quel est le véritable nom de L ?", "reponse":"Lawliet"},
    {"question":"Quel est le nom du shinigami qui accompagne Misa Amane ?", "reponse":"Rem"},
]
Question=[
    {"question":"Quel est le second souffle utilisée par le perso principal", "reponse":"le souffle du soleil"},
    {"question":"Quel est le nom du demon originel", "reponse":"Muzan kibustsuji"},
    {"question":"Quel est le nom du souffle utilisé par Tanjiro au début de son entraînement ?", "reponse":"le souffle de l'eau"},
    {"question":"Quel est le nom du personnage principal de Demon Slayer ?","reponse":"tanjiro kama"},
    {"question":"Quel est le nom du pilier de l'eau qui rencontre Tanjiro au début de l'histoire ?", "reponse":"Tomioka giyu"},
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