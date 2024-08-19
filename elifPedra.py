from random import randint

j = int(input('1 - Pedra\n2 - Papel\n3 - Tesoura\n'))
cpu = randint(1,3)
if j == 1:
    if cpu == 1:
        print('O pc escolheu Pedra,então deu empate')
    elif cpu == 2:
        print('Você perdeu KKKKKKKKKKK,o cpu escolheu papel')
    elif cpu == 3:
        print('Você GANHOU!O cpu burro escolheu tesoura.')
elif j == 2:
    if cpu == 1:
        print('VOCÊ venceu,o cpu escolheu pedra')
    elif cpu == 2:
        print('Deu empate')
    elif cpu == 3:
        print('Você perdeu!O cpu GÊNIO escolheu tesoura.')
elif j == 3:
    if cpu == 1:
        print('O pc escolheu Pedra,então tu PERDEU KKKKKKKK')
    elif cpu == 2:
        print('Você GANHOU !!o cpu escolheu papel')
    elif cpu == 3:
        print('Empatou!O cpu burro escolheu tesoura também.')
else:
    print('EU DISSE PRA DIGITAR ALGO ENTRE 1 E 3,JUMENTO')