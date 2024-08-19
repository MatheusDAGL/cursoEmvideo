from time import sleep
op = '4'
while op == '4':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite outro valor: '))
    voltar = True
    while voltar == True:
        op = str(input('Qual operação deseja realizar?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair\n'))
        if op == '1':
            print('A soma entre {} e {} é igual a {}'.format(n1,n2,n1+n2))
            sleep(1)
        elif op == '2':
            print('A multiplicação entre {} e {} é igual a {}'.format(n1,n2,n1*n2))
            sleep(1)
        elif op == '3':
            if n1 > n2:
                print('{} é maior que {}'.format(n1,n2))
            elif n2 > n1:
                print('{} é maior que {}'.format(n2,n1))
            else:
                print('{} é igual a {}'.format(n1,n2))
            sleep(1)
        elif op == '4':
            break
        elif op == '5':
            print('Obrigado,volte sempre!')
            break
        else:
            print('Por favor,digite uma opção válida')
            sleep(1)
