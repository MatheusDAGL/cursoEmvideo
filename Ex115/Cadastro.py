print('-'*24)
print('\tMenu Principal')
print('-'*24)
lista = []
while True:
    try:
        print('Qual opção deseja escolher? ')
        print('1 - Ver Registros')
        print('2 - Registrar novo nome')
        print('3 - Sair do Sistema')
        opcao = int(input(''))
        if opcao == 1:
            with open('RegistroNomes', 'r') as arquivo:
                p = arquivo.read()
                print(p)
                continue
        elif opcao == 2:
            with open('RegistroNomes', 'a') as arquivo:
                lista.append(arquivo.write(str(input('Digite um novo nome: '))))
                p = arquivo.write(f'\t\t')
                lista.append(arquivo.write(str(input('Digite a idade: '))))
                p = arquivo.write('\n')
        elif opcao == 3:
            break
        elif opcao > 3 or opcao < 1:
            print('Digite um valor válido.')
    except(ValueError, TypeError):
        print('Digite um valor válido')

print('Fim do Programa,volte sempre!')


