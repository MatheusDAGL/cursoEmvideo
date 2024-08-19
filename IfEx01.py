v = int(input('Qual a velocidade máxima que você andou ontem? '))
if v>80:
    print('Você foi MULTADO!!!!')
    m = (v-80)*7
    print('O valor da multa é de R${},00 reais'.format(m))
else:
    print('Se foda kkkkkkkk')

