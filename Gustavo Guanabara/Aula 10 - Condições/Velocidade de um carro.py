vel = int(input("A quantos Km/h o condutor estava dirigindo? "))
if vel>80:
    print("Você recebeu uma multa de R${},00 ".format((vel-80)*7))