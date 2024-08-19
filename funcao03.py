from random import randint
def somapar(par):
    somatorio = 0
    for i in par:
        if i % 2 == 0:
            somatorio += i
    print(f'A soma dos valores pares da lista anterior são: {somatorio}')
def sortear(num):
    num = randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)
    print(f'A lista aleatória é: {num}')
    somapar(num)


lista = []
sortear(lista)
somapar(lista)
