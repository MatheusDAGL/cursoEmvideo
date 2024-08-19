import moeda

numero = float(input('Digite um número: '))
print(f'O dobro de {moeda.moeda(numero)} é {moeda.dobro(numero,True)}')
print(f'A metade de {moeda.moeda(numero)} é {moeda.metade(numero,True)}')
print(f'O número {moeda.moeda(numero)},com aumento de 10%,é  {moeda.aumentar(numero,True)}')
print(f'O número {moeda.moeda(numero)},com decréscimo de 10%, é {moeda.diminuir(numero,True)}')

