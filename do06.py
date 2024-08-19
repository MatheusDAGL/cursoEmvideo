n = 1
contn = 0
vezes = 0
while n != 999:
    n = int(input('Digite um número [999 para encerrar]: '))
    if n != 999:
        contn += n
        vezes += 1
print('Você digitou {} valores e a soma deles é de {}'.format(vezes,contn))
