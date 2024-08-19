lista = []
c = 0
while True:
    n = int(input('Digite um valor: '))
    c += 1
    lista.append(n)
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {c} números')
print(f'Os números digitados,em ordem decrescente,são: ',lista)
if 5 in lista:
    print('O número 5 aparece na lista')
else:
    print('O número 5 não aparece.')
