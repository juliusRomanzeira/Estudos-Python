dis = float(input("Qual a distância da viagem em km? "))
if dis<=200:
    print("O preço dessa viagem, será R${:.2f}".format(dis*0.5))
else:
    print("O preço dessa viagem, será R${:.2f}".format(dis*0.45))