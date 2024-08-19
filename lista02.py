nlista = []
f = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in nlista:
        nlista.append(n)
    else:
        print('Valor duplicado')
    op = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if op == 'N':
        break
    if op != 'S':
        print('Opção inválida')

nlista.sort()
print(f'Os valores digitados foram:{nlista}')