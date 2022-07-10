num, aux = [], 0
for i in range(0,3):
    num.insert(i, float(input("Digite o {}º número: ".format(i+1))))
for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                aux = num[j]
                num[j] = num[j+1]
                num[j+1] = aux
print("O maior é: {}".format(num[-1]))