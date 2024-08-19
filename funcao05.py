def fatorial(n,show=False):
    """Essa função é loucura faz fatorial e várias merdas
    te amo b volta pra mim
    """
    f = 1
    for i in range(n, 0, -1):
        if show == True:
            print('1 = ' if i == 1 else f'{i} X ',end='')
        f *= i
    return f




print(fatorial(200,True))
help(fatorial)

