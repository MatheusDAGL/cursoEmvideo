n = int(input('Digite um termo: '))
r = int(input('Digite a razão: '))
décimo = n + (11-1) * r
for i in range(n,décimo,r):
    print(i,end=' > ')
print('ACABOU!!')
