import random
aux, dado = 0, range(0, 7)
while True:
    aux = aux + 1
    if random.choice(dado) == 5:
        print("{} Tentativas".format(aux))
        break