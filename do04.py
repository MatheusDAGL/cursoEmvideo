n = int(input('Digite um número: '))
r = int(input('Digite a razão:'))
i  = 1
resultado = n + r
print('{} > '.format(n),end='')
print('{} > '.format(resultado),end='')
while i < 9:
    resultado += r
    print('{}'.format(resultado),end='')
    print(' > ' if i < 8 else ' FIM!!! ',end='')
    i += 1
n2 = 1
total = i
while n2 != 0:
    n2 = int(input('Deseja verificar outra razão?Digite 0 para não'))
    i = 0
    while i < n2:
        resultado += r
        print('{}'.format(resultado),end='')
        print(' > ' if i < n2 else ' FIM!!!',end='')
        i += 1
    total2 = i
print('Progressão finazilada com {} termos.'.format(total + total2))
