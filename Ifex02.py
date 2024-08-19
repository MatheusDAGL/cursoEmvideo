km = int(input('Quantos quilômetros? '))
if km <=200:
    print('O valor da viagem é de ',km*0.50)
else:
    print('O valor da viagem é de R${:.2f} reais'.format(km*0.45))
