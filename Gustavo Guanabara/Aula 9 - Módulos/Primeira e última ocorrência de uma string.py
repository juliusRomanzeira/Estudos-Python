frase, aux, esp, var = input("Frase: ").lower(), 0, 0, []
while frase[esp] == ' ':
    esp=esp+1
for i in range(len(frase)):
    if frase[i] == 'a':
        var.insert(aux, i)
        aux = aux+1
print("A letra A aparece {} vezes na frase".format(aux))
print("A primeira letra A apareceu na posição {}".format((var[0]+1)-esp))
# print(len(frase))
# print(esp)
# print("A última letra A apareceu na posição {}".format(var[aux]-esp))