def leiaint(n=0):
    while True:
        n = str(input('Digite um número: ')).strip()
        if n.isnumeric():
            carlos = int(n)
            return carlos
        else:
            print('Digite um número de verdade paizão!')


def leiafloat(f=0):
    f = str(input('digite um numero'))
    f.__class__=float
        print('cu')
    else:
        print('erro')


n = leiaint()
f = leiafloat()
print(f'Você acabou de digitar o número inteiro {n} e o número real {f}')
