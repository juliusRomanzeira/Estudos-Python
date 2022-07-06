import random
print("Jogo de  pedra papel e tesoura")
escolha = input("O que você escolhe ? Pedra, papel ou tesoura ?")
escolha = escolha.lower()
player = ['pedra', 'papel', 'tesoura']
pc = random.choice(player)
print("CPU: {}".format(pc))
if pc == 'pedra' and escolha == 'papel':
    print("Ganhou")
elif pc == 'papel' and escolha == 'papel':
    print("Empate")
elif pc == 'tesoura' and escolha == 'papel':
    print("Perdeu")
elif pc == 'pedra' and escolha == 'pedra':
    print("Empate")
elif pc == 'papel' and escolha == 'pedra':
    print("Perdeu")
elif pc == 'tesoura' and escolha == 'pedra':
    print("Ganhou")
elif pc == 'pedra' and escolha == 'tesoura':
    print("Perdeu")
elif pc == 'papel' and escolha == 'tesoura':
    print("Ganhou")
elif pc == 'tesoura' and escolha == 'tesoura':
    print("Empate")
else:
    print('Escolha indevida')
