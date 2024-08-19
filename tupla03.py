from random import randint
vezes = maior = menor = 0
a = (randint(0,47574),randint(0,47574),randint(0,47574),randint(0,47574),randint(0,47574))
print(a)
for i in a:
    vezes += 1
    if vezes == 1:
        maior = i
        menor = i
    else:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
print(maior)
print(menor)
print(max(a),min(a))