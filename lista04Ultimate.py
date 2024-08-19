par = []
impar = []
todos = []
op = ''
while True:
    if op == 'N':
        break
    n = int(input('Digite um valor: '))
    todos.append(n)
    while True:
        op = str(input('Quer continuar? ')).upper().strip()[0]
        if op == 'N' or op == 'S':
            break
        elif op != 'S':
            print('Digite uma opção válida')
for i in range(0,len(todos)):
    if todos[i] % 2 == 0:
        par.append(todos[i])
    else:
        impar.append(todos[i])
print('Os números pares digitados foram: ', par)
print('Os números ímpares digitados foram: ', impar)
print('Todos os números: ', todos)