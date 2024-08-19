par = 0
matriz = [[], []]
for i in range(0, 3):
    j = 0
    matriz[0].append(int(input(f'Digite um valor para posição {i},{j} ')))
    for j in range(1, 3):
        matriz[1].append(int(input(f'Digite um valor para posição {i},{j} ')))
print(matriz[0][0], matriz[1][0], matriz[1][1])
print(matriz[0][1], matriz[1][2], matriz[1][3])
print(matriz[0][2], matriz[1][4], matriz[1][5])
for numero in matriz[0]:
    if numero % 2 == 0:
        par += numero
for numero in matriz[1]:
    if numero % 2 == 0:
        par += numero
print(f'a soma dos valores pares é de {par}')
print(f'A soma dos valores da terceira coluna é de {matriz[1][1]+matriz[1][3]+matriz[1][5]}')
if matriz[0][1] > matriz[1][2] and matriz[0][1] > matriz[1][3]:
    print(f'O maior valor da segunda linha foi {matriz[0][1]}')
elif matriz[1][2] > matriz[0][1] and matriz[1][2] > matriz[1][3]:
    print(f'O maior valor da segunda linha foi {matriz[1][2]}')
elif matriz[1][3] > matriz[0][1] and matriz[1][3] >matriz[1][2]:
    print(f'O maior valor da segunda linha foi {matriz[1][3]}')