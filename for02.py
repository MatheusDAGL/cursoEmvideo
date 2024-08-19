from datetime import date
atual = date.today().year
cont = 0
cont2 = 0
for i in range (0,7):
    nasc = int(input('Em que ano a pessoa {} nasceu?'.format(i+1)))
    if (atual-nasc)>=18:
        cont += 1
    else:
        cont2 += 1
print('{} pessoas de maior e {} pessoas de menor'.format(cont,cont2))
