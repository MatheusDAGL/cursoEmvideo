idadecont = 0
maior = 0
contsexo = 0

for i in range(1,5):
    nome = str(input('Qual o nome da {}ª Pessoa? '.format(i)))
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo? (m para masculino,f para feminino) ')).upper().strip()
    if  sexo == 'M' and maior < idade:
        maior = idade
        nomevelho = nome
    elif sexo == 'F' and idade <20:
        contsexo += 1
    idadecont += idade
print('A média de idade do grupo é de ',idadecont/i)
print('O homem mais velho se chama {},e tem {} anos.'.format(nomevelho,maior))
print('O número de mulheres com menos de 20 anos é de ',contsexo)





