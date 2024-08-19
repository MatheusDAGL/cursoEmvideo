maior = []
menor = []
dado = []
contp = maiorp = menorp = 0
while True:
    dado.append(str(input('Digite o seu nome: ')))
    contp += 1
    dado.append(int(input('Digite o seu peso: ')))
    if contp == 1:
        maiorp = dado[1]
        maior.append(dado[0])
        menorp = dado[1]
        menor.append(dado[0])
    else:
        if dado[1] > maiorp:
            maior.clear()
            maiorp = dado[1]
            maior.append(dado[0])
        elif dado[1] == maiorp:
            maior.append(dado[0])
        elif dado[1] < menorp:
            menor.clear()
            menorp = dado[1]
            menor.append(dado[0])
        elif dado[1] == menorp:
            menor.append(dado[0])
    dado.clear()
    op = str(input('Quer continuar? ')).upper().strip()[0]
    if op == 'N':
        break
print(f'Foram cadastradas {contp} pessoas.')
print(f'O maior peso foi de {maiorp},e as pessoas mais pesadas são {maior}')
print(f'O menor peso foi de {menorp},e as pessoas mais leves são {menor}')
