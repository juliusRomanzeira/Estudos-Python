km = float(input("Informe a distância percorrida: "))
dias = int(input("Informe a quantidade de dias: "))
total = (dias*60) + (km*0.15)
print("O total a ser pago é de {:.2f} reais".format(total))