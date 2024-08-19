n = []
p = []
impar = []
for i in range (0,7):
    n.append(int(input(f'Digite o {i+1}º número: ')))
    if n[i] % 2 == 0:
        p.append(n[i])
    else:
        impar.append(n[i])
n.clear()
p.sort()
impar.sort()
n.append(p[:])
n.append(impar[:])
print(f'Os números ímpares foram {n[1]}')
print(f'Os números pares foram {n[0]}')



