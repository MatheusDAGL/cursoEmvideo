val = float(input('Qual o valor do produto que deseja comprar? '))
pag = int(input('Qual a forma de pagamento?\n1 - Dinheiro\n2 - Cartão Débito\n3 - Cartão 2x\n4 - Cartão 3x ou mais\n'))
if pag == 1:
    print('Com 10% de desconto,você pagará R${:.2f}'.format(val-(val*(10/100))))
elif pag == 2:
    print('Com 5% de desconto,você pagará R${:.2f}'.format(val-(val*(5/100))))
elif pag == 3:
    print ('Você pagará R${:.2f} por mês'.format(val/2))
elif pag == 4:
    p = int(input('Quantas parcelas?'))
    print('Você pagará R${:.2f} por mês,com juros de 20%'.format((val+(val*(20/100)))/p))
else:
    print('Digite uma opção entre 1 e 4,jumento.')
