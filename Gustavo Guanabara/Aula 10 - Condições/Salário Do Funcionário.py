sal = float(input("Qual o salário do funcionário? "))
if sal>1250:
    print("O novo salário é R${:.2f}".format(sal*1.10))
else:
    print("O novo salário é R${:.2f}".format(sal*1.15))