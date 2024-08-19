def ficha(nome,gols):
    if nome == '':
        nome = 'Desconhecido'
    if gols.isnumeric():
        print(f'O jogador {nome} fez {gols} gols.')
    else:
        gols = 0
        print(f'O jogador {nome} fez {gols} gols.')


n = str(input('Digite o nome do jogador: ')).strip()
g = str(input('Quantos gols no campeonato? ')).strip()
ficha(n,g)