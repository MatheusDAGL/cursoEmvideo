from random import shuffle
n1 = str(input('Digite seu nome,gafanhoto '))
n2 = str(input('Digite seu nome,gafanhoto '))
n3 = str(input('Digite seu nome,gafanhoto '))
n4 = str(input('Digite seu nome,gafanhoto '))
lista = [n1,n2,n3,n4]

print('O aluno escolhido foi {}'.format(lista))
shuffle(lista)
print('A nova ordem é de ',lista)