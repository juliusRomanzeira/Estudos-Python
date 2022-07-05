# Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# - O nome com todas as letras maiúsculas e minúsculas.
#
# - Quantas letras ao todo (sem considerar espaços)
#
# - Quantas letras tem o primeiro nome.
#

nome = input("\n\nDigite seu nome completo: ")
print("\nNome em caixa alta --> {}\nNome em minúsculas --> {}".format(nome.upper(),nome.lower()))
print("\nTamanho da string --> {}".format(len(nome)))
