totpessoas = []
pessoa = {}
mulheres = []
somatorio = 0
while True:
    pessoa['nome'] = str(input('Digite seu nome: '))
    pessoa['sexo'] = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
        pessoa['sexo'] = str(input('Digite uma opção válida [M/F] ')).upper().strip()[0]
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Digite sua idade: '))
    somatorio += pessoa['idade']
    totpessoas.append(pessoa.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Digite uma opção válida [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
media = somatorio / len(totpessoas)
print('-='*25)
print(f'No total,temos {len(totpessoas)} pessoas cadastradas.')
print(f'A idade média das pessoas cadastradas é de {media}')
print(f'As mulheres cadastradas foram {mulheres}')
print('A lista de pessoas cuja idade é maior do que a média é:')
for i in range(0,len(totpessoas)):
    if totpessoas[i]['idade'] > media:
        print(totpessoas[i])
