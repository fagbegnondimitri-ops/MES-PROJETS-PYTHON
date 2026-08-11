notes = [12, 8, 15, 17, 9]
total=0
compteur=0
i=-1
while compteur<len(notes):
    i+=1
    total += notes[i]
    compteur+=1
    print(f"notes{i} = {notes[i]}")
print("somme =",total)
print("moyenne=",total/len(notes))