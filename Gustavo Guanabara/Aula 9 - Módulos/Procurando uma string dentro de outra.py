from itertools import count
nome, Resposta = (input("Qual é seu nome completo? ")).lower(), False
for i in range(0, len(nome.split())):
    if nome.split()[i] == 'silva':
        Resposta = 'True'
        break
print("Seu nome tem Silva? {}".format(Resposta))

# Uma outra forma:
# nome = input("Qual seu nome completo? ").strip()
# print("Seu nome tem Silva? {}".format('silva' in nome.lower()))