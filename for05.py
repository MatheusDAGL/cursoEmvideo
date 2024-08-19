frase = str(input('Digite uma frase: ')).strip().upper()
frase2 = frase.replace(' ','')
inv = frase2[::-1]
if inv == frase2:
    print('A frase {} invertida é {},ou seja,um palíndromo'.format(frase2,inv))
else:
    print('A frase {} invertida é {},ou seja,não é palíndromo'.format(frase2,inv))