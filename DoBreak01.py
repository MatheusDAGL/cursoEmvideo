from random import randint
cont = 0
while True:
    j = int(input('Digite um valor de 1 a 9: '))
    ip = str(input('Par ou impar?')).upper().strip()
    cpu = randint(0,10)
    ip2 = cpu + j
    if ip2%2==0 and ip=='P':
        print(f'Você Venceu!{j} + {cpu} deu {ip2},ou seja,é par')
        cont += 1
    elif ip2%2!=0 and ip=='I':
        print(f'Você venceu!{j} + {cpu} dá {ip2},ou seja,impar')
        cont += 1
    elif ip2%2==0 and ip=='I':
        print(f'Você PERDEU!{j} + {cpu} dá {ip2},ou seja,par')
        break
    else:
        print(f'Você PERDEU!{j} + {cpu} dá {ip2},ou seja,impar')
        break
print(f'Você venceu {cont} vezes')

