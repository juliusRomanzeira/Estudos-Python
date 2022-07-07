import random
tam, nomes, aux = int(input("Digite a quantidade de participantes: ")), [], 0
while True:
    aux = aux+1
    if aux == 10000:
        break
for i in range(tam):
    nomes.insert(i, input("Digite o nome da pessoa {}: ".format(i+1)))
escolha = random.choice(nomes)
print("Tranquilo, o sorteado foi: {}> {} <{}".format('-'*len(escolha),escolha,'-'*len(escolha)))
