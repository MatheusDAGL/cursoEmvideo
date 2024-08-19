n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))

if n1>n2 and n1>n3:
    print('O maior número é ',n1)
    if n2<n1 and n2<n3:
        print('O menor número é ',n2)
    else:
        print('O menor número é ',n3)
elif n2>n1 and n2>n3:
    print('O maior número é ',n2)
    if n1<n2 and n1<n3:
        print('O menor número é ',n1)
    else:
        print('O menor número é ',n3)
elif n3>n1 and n3>n2:
    print('O maior número é ',n3)
    if n1<n2 and n1<n3:
        print('O menor número é ',n1)
    else:
        print('O menor número é ',n2)

