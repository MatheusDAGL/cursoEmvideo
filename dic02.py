from random import randint
from operator import itemgetter
jogadores = {'Jogador 1':randint(1,6),'Jogador 2':randint(1,6),'Jogador 3':randint(1,6),'Jogador 4':randint(1,6)}
for k,v in jogadores.items():
    print(f'{k} tirou {v} no dado')
ranking = sorted(jogadores.items(),key=itemgetter(1,0),reverse=True)
for i,v in enumerate(ranking):
    print(f'{i},{v}')


