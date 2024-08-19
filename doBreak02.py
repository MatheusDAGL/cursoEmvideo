print('Cadastro Bacana')
contidade = conthomem = contmulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        contidade += 1
    while True:
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
        if sexo == 'M':
            conthomem += 1
        if sexo == 'F' and idade < 20:
            contmulheres += 1
        if sexo == 'M' or sexo == 'F':
            break
        print('Digite uma opção válida')
    while True:
        op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if op == 'S' or op == 'N':
            break
        print('Digite uma opção válida!')

    if op == 'N':
        break
print(f'No total,{contidade} pessoas tem mais de 18 anos.')
print(f'{conthomem} homens foram cadastrados.')
print(f'Foram cadastradas {contmulheres} mulheres com menos de 20 anos.')

# sexo = ''
# while sexo not in 'MF'

