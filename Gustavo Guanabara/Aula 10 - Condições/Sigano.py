import random
adv = float(input("Você está preso em um Genjutsu,\nPara sair você terá que acertar qual número estou pensando\nDigite um número: "))
if adv>5 or adv<0:
    print("Digito fora do range!!")
else:
    cpu = int(random.choice(range(0,6)))
    while True:
        if cpu == adv:
            print("KRLLL !! Tu é bom mesmo !!")
            break
        print("\n\nERRRROOOOOOUUU!")
        cpu = int(random.choice(range(0,6)))
        print("\nPensei no número {}\n\nTente novamente, loser !!".format(int(cpu)))
        adv = int(input("Você está preso em um Genjutsu,\nPara sair você terá que acertar qual número estou pensando\nDigite um número: "))
        if adv>5 or adv<0:
            print("Digito fora do range!!")
            break