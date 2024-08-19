time = []
jogador = {}
gols = []
somatorio = 0
while True:
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    partidas = int(input('Quantas partidas no campeonato? '))
    for i in range(1,partidas+1):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
    jogador['gols'] = gols[:]
    for i in gols:
        somatorio += i
    jogador['total'] = somatorio
    time.append(jogador.copy())
    gols.clear()
    somatorio = 0
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Digite uma opção válida [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print('=-'*20)
for i,item in enumerate(time):
    print(f'N° {i}   O jogador {item["nome"]} fez {item["gols"]} gols em cada partida,totalizando {item["total"]} gols.')
print('=-'*20)
while True:
    continuar = int(input('Qual jogador deseja visualizar os dados? [999 para parar] '))
    if continuar == 999:
        break
    elif continuar < 0 or continuar >= len(time):
        while continuar < 0 or continuar >= len(time):
            continuar = int(input('Número inválido,digite corretamente'))

    print('=-'*20)
    print(f'Levantamento do jogador {time[continuar]["nome"]}')
    for i,item in enumerate(time[continuar]['gols']):
        print(f'No jogo {i+1}, ele fez {item} gols.')
print('Fim do programa!')


