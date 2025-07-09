#Afficher Fizz pour chaque nombre divisible par 3, Buzz pour 5

for x in range(1,101):
    res = ""
    res = ("Fizz" if x%3 == 0 else "") + ("Buzz" if x%5 == 0 else "")
    if res == "":
        print(x)
    else:
        print(res)