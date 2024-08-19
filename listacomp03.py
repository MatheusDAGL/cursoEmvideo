matriz = [[], []]
for i in range(0, 3):
    j = 0
    matriz[0].append(int(input(f'Digite um valor para posição {i},{j} ')))
    for j in range(1, 3):
        matriz[1].append(int(input(f'Digite um valor para posição {i},{j} ')))
print(matriz[0][0], matriz[1][0], matriz[1][1])
print(matriz[0][1], matriz[1][2], matriz[1][3])
print(matriz[0][2], matriz[1][4], matriz[1][5])
