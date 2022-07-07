from math import sqrt,floor
op = float(input("Digite o Cateto Oposto: "))
ad = float(input("Digite o Cateto Adjacente: "))
hip = sqrt((op**2)+(ad**2))
# Para inteiros --> hip = floor(hip)
print("A hipotenusa vale: {}".format(hip))