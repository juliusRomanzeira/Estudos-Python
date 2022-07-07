frase, aux, pos, space = input("Digite uma frase: "), 1, [], 2
for i in range(len(frase)):
    if frase[i] == ' ' and frase[i-1] == ' ':
        space = space+1
    if frase[i] == 'a':
        pos.insert(aux, i)
        aux = aux+1
print("A letra A aparece {} vezes na frase.\nA primeira letra A apareceu na posição {}".format(aux, (pos[0])-space))
print("A última letra A apareceu na posição {}".format((pos[len(pos)-1])-space+2))
print(space)