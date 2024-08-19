def leiadinheiro(n):
    while True:
        if n.isnumeric():
            break
        else:
            print(f'Erro!!!{n} não é um dado monetário.')
            n = str(input("Digite um número: "))
    return n