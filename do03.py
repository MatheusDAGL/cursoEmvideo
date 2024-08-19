'''n = int(input('Digite um número: '))
fatorial = n-1
resultado = n * fatorial
while fatorial > 2:
    fatorial = fatorial - 1
    resultado = resultado * fatorial
print(resultado)'''

n = int(input('Digite um número: '))
c = n
f = 1
print('{}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))


