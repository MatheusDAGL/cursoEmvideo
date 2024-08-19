par = []
impar = []
op = ''
while True:
    if op == 'N':
        break
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    while True:
        op = str(input('Quer continuar? ')).upper().strip()[0]
        if op == 'N' or op == 'S':
            break
        elif op != 'S':
            print('Digite uma opção válida')

todos = par + impar
print('Os números pares digitados foram: ', par)
print('Os números ímpares digitados foram: ', impar)
print('Todos os números: ', todos)
