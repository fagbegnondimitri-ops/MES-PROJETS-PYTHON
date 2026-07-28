notes = [12, 8, 15, 17, 9]
total=0
for i in range(len(notes)):
    print(f"Note {i+1} = {notes[i]}")
    total += notes[i]
print("somme =",total)
print("moyenne=",total/len(notes))