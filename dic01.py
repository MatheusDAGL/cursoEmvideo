mano = {}
mano['nome'] = str(input('Digite seu nome: '))
mano['media'] = int(input('Digite sua média: '))
if mano['media'] > 7:
    mano['situação'] = ('aprovado')
else:
    mano['situação'] = ('reprovado')
for k,v in mano.items():
    print(f'{k} é {v}')