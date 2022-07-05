# Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# - O nome com todas as letras maiúsculas e minúsculas.
#
# - Quantas letras ao todo (sem considerar espaços)
#
# - Quantas letras tem o primeiro nome.
#
from unicodedata import name


aux = 0
nome = input("\n\nDigite seu nome completo: ")
string = [nome]
tam = []
print("\nNome em caixa alta --> {}\nNome em minúsculas --> {}".format(nome.upper(),nome.lower()))
print("\nTamanho da string --> {}".format(len(nome)))
for i in range(nome):
    if string[i] == ' ':
        tam.insert[i] = aux
        aux = 0
    aux += 1
print("\nTamanho do primeiro nome: {}".format(tam[0]))
