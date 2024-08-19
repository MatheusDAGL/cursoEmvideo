cinquenta = 0
vinte = 0
dez = 0
um = 0
n = int(input('Digite o valor que deseja sacar: '))
cinquenta = n//50
resto = n%50
if resto > 20:
    vinte = resto//20
    resto = n%20
dez = resto//10
resto = n%10
um = resto//1
print(f'{cinquenta} cédulas de R$50.00;')
print(f'{vinte} cédulas de R$20.00;')
print(f'{dez} cédulas de R$10.00;')
print(f'{um} cédulas de R$1.00.')
