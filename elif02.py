n = int(input('Digite um valor inteiro '))
print('Qual opção deseja?\n1 - Binário\n2 - Octa\n3 - Hexadecimal')
r = int(input())
if r == 1:
    print('O valor de {} em binário é {}.'.format(n,bin(n)[2:]))
elif r == 2:
    print('O valor de {} em octa é {}'.format(n,oct(n)[2:]))
elif r == 3:
    print('O valor de {} em hexadecimal é de {}'.format(n,hex(n)[2:]))
else:
    print('{} não está entre 1 e 3,burro'.format(n))