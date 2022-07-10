ano = int(input("Digite o ano: "))
if (ano%4 == 0 and ano%10 != 0) or (ano%4 == 0 and ano%100 == 0 and ano%400 == 0):
    print("Ano BISSEXTO")
else:
    print("Não é Bissexto")