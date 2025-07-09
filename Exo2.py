import re
from functools import reduce
#Extraire les nombres dans un string et les additionner

sentence = "La première usine dispose de 324 employés. La deuxième usine en compte 529. L'unité de Los Angeles dispose quant à elle de 918 employés."

matches = re.findall("(\d+)",sentence)
nb_lst = list(map(int,matches))

sum_V2 = reduce(lambda x, y:x+y, nb_lst)

print(sum(nb_lst))
print(sum_V2)