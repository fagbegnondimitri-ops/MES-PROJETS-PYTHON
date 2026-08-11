nombres=[4,7,2,9,4,1,4] 
print(max(nombres))
max=nombres[0]
compteur=0
total=0
for nombre in nombres:
    if nombre>= max:
        max=nombre
    if nombre==4:
        compteur+=1
    if nombre>3:
        total+=1
print(max)
print("4 apparait",compteur," fois")
print(nombres.count(4))
print(f"{total} nombres sont superieures a 3")