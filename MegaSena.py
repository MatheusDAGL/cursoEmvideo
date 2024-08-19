from random import randint
print('=-' *20)
print('MEGA SENA DA VIRADA'.center(35))
print('=-' *20)
megasena = []
palpite = []
acerto = 0
while len(megasena) < 6:
    n = randint(1,60)
    if n not in megasena:
        megasena.append(n)
megasena.sort()
for i in range(0,6):
    palpite.append(int(input(f'Digite o {i+1}° número, entre 1 e 60: ')))
    if palpite[i] in megasena:
        acerto += 1
palpite.sort()
print(f'\nSeu palpite foi:           {palpite}')
print(f'Os números da Megasena são: {megasena}')
print(f'Você acertou {acerto} número(s)!')
if acerto < 4:
    print('\nInfelizmente,você não ganhou nada.')
elif acerto == 4:
    print('\nParabéns!Você ganhou a quadra')
elif acerto == 5:
    print('\nParabéns!Você ganhou a quina')
elif acerto == 6:
    print('\nPARABÉNS!VOCÊ É O MAIS NOVO MILIONÁRIO DO BRASIL,E EMBOLSOU R$ 570.00 MILHÕES DE REAIS!!!')
