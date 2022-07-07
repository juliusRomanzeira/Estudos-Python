nome = input("Digite seu nome completo: ")
print("Analizando seu nome...")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(1+(len(nome)-len(nome.split()))))
# Uma outra resposta para a linha 5 é:
# print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
print("Seu primeiro nome é {} e tem {} letras".format(nome.split()[0], len(nome.split()[0])))
