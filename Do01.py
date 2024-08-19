from random import randint
tent = 1
cpu = randint(0,100)
j = int(input('Acabei de pensar em número entre 1 e 100.Tente adivinhar qual é,em dez tentativas: '))
while j != cpu and tent < 10:
    tent += 1
    if cpu > j:
        print('Errou!Mais...')
    elif cpu < j:
        print('Errou!é menos')
    j = int(input('Tente novamente: '))

if j == cpu:
    print('Você levou {} tentativas para acertar o número {}'.format(tent,cpu))
else:
    print('As tentativas se esgotaram.Você PERDEU!')

