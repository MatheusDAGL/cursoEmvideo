inter = []
dados = []
while True:
    inter.append(str(input('Digite o nome: ')))
    inter.append(float(input('Digite a nota 1: ')))
    inter.append(float(input('Digite a nota 2: ')))
    dados.append(inter[:])
    inter.clear()
    op = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if op == 'N':
        break
print('=-' * 20)
for i in range(0, len(dados)):
    print(f'{i} Nome: {dados[i][0]} / Nota média: {(dados[i][1]+dados[i][2])/2}\n')
while op != 999:
    op = int(input('Digite um número para visualizar as notas individuais: [999 para finalizar]'))
    print('=-' * 20)
    print(f'As notas de {dados[op][0]} foram {dados[op][1]} e {dados[op][2]}')
    print('=-' * 20)
print('Programa finalizado')

