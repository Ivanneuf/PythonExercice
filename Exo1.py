#Demander un nombre en entrée et affichée les multiplications jusqu'a un deuxième nombre
#Pas besoin de vérifié validité

print("Veuillez entre un nombre : ")
nb_to_mult = int(input())
print("A multiplier jusqu'a : ")
nb_mult = int(input())

for x in range(nb_mult):
    print(f"{nb_to_mult} X {x} = {nb_to_mult*x}")