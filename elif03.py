from datetime import date
ano = date.today().year
nasc = int(input('Digite seu ano de nascimento'))
if (ano-nasc)<18:
    print('Relaxa,ainda falta {} ano(s) para você se alistar.'.format((ano-(nasc+18))*-1))
    print('Seu alistamento será em ',nasc+18)
elif (ano-nasc)==18:
    print('VÁ SE ALISTAR AGORA ')
else:
    print('Você devia ter se alistado há {} anos'.format(ano-(nasc+18)))
