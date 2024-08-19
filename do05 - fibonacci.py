termos = int(input('Quantos termos você quer mostrar? '))
f1 = 0
f2 = 1
print(f1)
print(f2)
vezes = 0
while vezes < (termos-2):
    fib = f1 + f2
    f1 = f2
    f2 = fib
    vezes += 1
    print(fib)