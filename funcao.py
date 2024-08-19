from time import sleep


def contador(inicio,fim,passo):
    if fim > inicio or passo<0:
        for i in range(inicio,fim+1,passo):
            print(i,end=' ')
            sleep(0.2)
    else:
        for i in range(inicio,fim-1,passo* -1):
            print(i,end=' ')
            sleep(0.2)


contador(1,10,1)
print('\n')
print('-=' * 20)
contador(10,0,2)
print('\n')
print('-=' * 20)
contador(int(input('Digite o ínicio: ')),int(input('Digite o fim: ')),int(input('Digite o passo: ')))

