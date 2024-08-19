def voto(condicao):
    if condicao < 18:
        votar = 'Voto Negado.'
        return votar
    if condicao >= 18 and condicao < 65:
        votar = 'Voto Obrigatório.'
        return votar
    else:
        votar = 'Voto Opcional.'
        return votar


from datetime import date
ano = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
idade = ano - nascimento
decisao = voto(idade)
print(f'Com {idade} anos,{decisao}')