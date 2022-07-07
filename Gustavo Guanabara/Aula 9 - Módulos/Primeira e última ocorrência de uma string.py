frase, aux, pos, space = input("Digite uma frase: ").lower(), 0, [], 0
for i in range(len(frase)):
    if frase[i] == 'a':
        pos.insert(aux, i)
        aux = aux+1
print("A letra A aparece {} vezes na frase.\nA primeira letra A apareceu na posição {}".format(aux, pos[0]))
# print("A última letra A apareceu na posição {}".format((pos[len(pos)-1])))
# print(space)