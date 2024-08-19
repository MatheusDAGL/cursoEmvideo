def metade(n,form=False):
    res = n/2
    if form==True:
        res = 'R${:.2f}'.format(res)
    return res


def dobro(n,form=False):
    res = n*2
    if form==True:
        res = 'R${:.2f}'.format(res)
    return res


def aumentar(n,form=False):
    res = n+(n/10)
    if form==True:
        res = 'R${:.2f}'.format(res)
    return res


def diminuir(n,form=False):
    res = n-(n/10)
    if form==True:
        res = 'R${:.2f}'.format(res)
    return res

def moeda(n):
    res = 'R${:.2f}'.format(n)
    return res

def resumo(n,form=False):
    print(f'O dobro de {moeda(n)} é {dobro(n,True)}')
    print(f'A metade de {moeda(n)} é {metade(n,True)}')
    print(f'O número {moeda(n)},com aumento de 10%,é  {aumentar(n,True)}')
    print(f'O número {moeda(n)},com decréscimo de 10%, é {diminuir(n,True)}')
