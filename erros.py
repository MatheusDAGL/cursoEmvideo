def leiaint(n=0):
    while True:
        n = str(input('Digite um número: ')).strip()
        if n.isnumeric():
            carlos = int(n)
            return carlos
        else:
            print('Digite um número de verdade paizão!')


def leiafloat(f=0):
    while True:
        try:
            f = float(input('digite um numero real: '))
        except (ValueError,TypeError):
            print('Digite um número real,porra: ')
            continue
        else:
            return f





n = leiaint()
f = leiafloat()
print(f'Você acabou de digitar o número inteiro {n} e o número real {f}')
