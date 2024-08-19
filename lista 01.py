n = list()
vezes = 0
for i in range(0,5):
    n.append(int(input('Digite um valor: ')))
    vezes += 1
    if vezes == 1:
        maior = n[i]
        menor = n[i]
        menorp = n.index(n[i])
        maiorp = n.index(n[i])
    elif n[i] > maior:
        maior = n[i]
        maiorp = n.index(n[i])
    elif n[i] < menor:
        menor = n[i]
        menorp = n.index(n[i])

print(f'A lista digitada foi {n}')
print(f'O menor valor encontrado foi {menor},na posição {menorp}')
for i ,v in enumerate(n):
    if v == menor:
        print(i)
print(f'O maior valor encontrado foi {maior},na posição {maiorp}')


