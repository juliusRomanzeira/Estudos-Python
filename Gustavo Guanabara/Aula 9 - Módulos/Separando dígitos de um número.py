num = int(input("Infore um inteiro: "))
print("Analisando o número {}...\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(num, num%10, int((num%100)/10), int((num%1000)/100), int((num%10000)/1000)))
# Outra forma, seria:
#
# Unidade == (num//1)%10
# Dezena == (num//10)%10
# Centena == (num//100)%10
# Milhar == (num//1000)%10
#
