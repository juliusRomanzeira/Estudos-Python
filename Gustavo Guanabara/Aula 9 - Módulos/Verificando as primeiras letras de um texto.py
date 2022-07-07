from itertools import count


city = input("Em que cidade você nasceu? ")
nome = city.split()[0]
nome = nome.lower()
if nome == 'santo':
    print(True)
else:
    print(False)