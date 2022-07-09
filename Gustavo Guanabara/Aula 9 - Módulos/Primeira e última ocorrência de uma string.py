frase, aux, i, pos = input("Digite uma frase: ").lower(), [], 0, 0
print("A letra A aparece {} na frase.".format(frase.count('a')))
while frase[i] == ' ':
    i=i+1
for j in range(len(frase)):
    if frase[j]=='a':
        aux.insert(pos, j+1)
        pos = pos+1
print("A primeira letra A apareceu na posição {}".format(aux[0]-i))
print("A última letra A apareceu na posição {}".format(aux[pos-1]-i))

# Uma outra forma:
# frase = input("Digite uma frase: ").lower()
# print("A letra A aparece {} vezes na frase".forma(frase.count('a')))
# print("A primeira letra A apareceu na posição {}".format(frase.find('a')+1))
# print("A última letra A apareceu na posição {}".format(frase.rfind('a')+1))
