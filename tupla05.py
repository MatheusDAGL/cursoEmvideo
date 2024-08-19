l = ('RegistroNomes','futuro','escondidinho','sua mãe é minha')
a = 3
for i in l:
    print(f'\nna palavra {i} temos',end=' ')
    for i2 in i:
        if i2 in 'aeiou':
            print(f' {i2}',end='')





    '''print(f'Na palavra {i},temos ',end='')
    print('a 'if 'a'in i else '',end='')
    print('e ' if 'e' in i else '',end='')
    print('i ' if 'i' in i else '',end='')
    print('o ' if 'o' in i else '',end='')
    print('u ' if 'u' in i else '')'''



