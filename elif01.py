v = float(input('Digite o valor da casa: '))
s = float(input('Digite o seu salário: '))
a = int(input('Em quantos anos vai pagar? '))

prest = (v/12)/a

if prest < s*30/100:
    print('Você pagará R${:.2f} por mês,seu empréstimo está aprovado'.format(prest))
else:
    print('Empréstimo negado,pois você teria que pagar R${:.2f} por mês.'.format(prest))
