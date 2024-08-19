soma = 0
total = 0
for i in range(1,500,2):
    if i%3 == 0:
        total = total+1
        soma = soma+i
print('a soma de todos os {} valores é de {}'.format(total,soma))


