a = float(input('Digite um valor do lado do triângulo: '))
b = float(input('Digite um valor do lado do triângulo: '))
c = float(input('Digite um valor do lado do triângulo: '))
if (b-c) < a < b+c and ( a - c ) < b < a + c and ( a - b ) < c < a + b:
    print('\033[1;37;46mParabéns,você tem um triângulo\033[m')
    if a==b==c:
        print('Triângulo equilátero')
    elif a==b or b==c or a==c:
        print('Triângulo Isósceles')
    else:
        print('Triãngulo escaleno')
else:
    print('Isso não é um triângulo')
