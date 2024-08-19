e = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n >= 0 and n <=20:
        break
    print('Número inválido,digite novamente.')
print(f'Você digitou o número {e[n]}.')
