nove = tres = 0
n = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))
print(n)
print('Os números pares foram:',end='')
for i in range(0,4):
    if n[i] == 9:
        nove += 1
    elif n[i] == 3:
        tres = i+1
    elif n[i]%2 == 0:
        par = n[i]
        print(par,end=' ')
print(f'\no número 9 aparece {nove} vezes')
print(f'O número 3 apareceu na {tres}ª posição')

# print(f'o número 9 apareceu {n.count(9)}')
# print(f'o número 3 apareceu na {n.index(3)+1}')