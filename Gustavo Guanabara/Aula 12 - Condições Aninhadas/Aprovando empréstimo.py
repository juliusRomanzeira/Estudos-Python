val, sal, ano = float(input("\nQual o valor da casa? ")), float(input("Qual seu salário? ")), int(input("Em quanto anos você pretende quitar sua dívida? "))
# 1ano ----- 12meses
# xano ----- ymeses ------ y = xanos.12
meses = ano*12
parcelas = val/meses
if parcelas>sal*0.3:
    print("Negada a sua compra !")