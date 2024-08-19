contp = gasto = menorv = vezes = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = int(input('Qual o valor? '))
    gasto += preco
    vezes += 1
    if preco > 1000:
        contp += 1
    if vezes == 1:
        menorv = preco
        menorp = produto
    else:
        if preco < menorv:
            menorv = preco
            menorp = produto
    op = 'k'
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if op == 'N':
        break
print(f'Você gastou R${gasto:.2f} reais')
print(f'Você comprou {contp} produtos acima de R$1.000 reais.')
print(f'O produto mais barato foi {menorp},que custou {menorv}')

