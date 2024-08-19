def notas(*n,sit=False):
    maior = menor = soma = 0
    for i in range(0,len(n)):
        soma += n[i]
        if i == 0:
            maior = n[i]
            menor = n[i]
        else:
            if n[i] > maior:
                maior = n[i]
            elif n[i] < menor:
                menor = n[i]
    dic = {}
    dic['total'] = len(n)
    dic['maior nota'] = maior
    dic['menor nota'] = menor
    media = soma/len(n)
    dic['média'] = media
    if sit == True:
        if media < 5:
            dic['Situação'] = 'Ruim'
        elif media >= 5 and media < 7:
            dic['Situação'] = 'Ok'
        else:
            dic['Situação'] = 'Boa'
    return dic


resp = notas(3.5,8,4,2.7,3,6,10,6,7,5,2.1,10,sit=True)
print(resp)

# sun,max,min

