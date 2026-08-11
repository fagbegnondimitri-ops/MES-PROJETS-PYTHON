def demander_notes():
    notes =[]
    for i in range(0,3):
        notes.append(input("entrer une note"))
    return notes

notes=demander_notes()
def calcul_moyenne(notes):
    total=0
    for i in notes :
        total+=int(i)
    moy=total/len(notes)
    return moy
print("Moyenne = ",calcul_moyenne(notes))
def appreciation(moyenne):
    if moyenne>=10:
        appreciation="Admis"
    else:
        appreciation="Recalé"
    return appreciation
print(appreciation(calcul_moyenne(notes)))