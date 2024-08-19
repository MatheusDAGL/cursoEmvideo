from datetime import date
dados = {}
dados['nome'] = str(input('Digite seu nome: '))
dados['data'] = int(input('Digite sua data de nascimento: '))
dados['sexo'] = str(input('Digite o seu sexo:[M/F] ')).strip().upper()[0]
idade = date.today().year - dados['data']
dados['cpts'] = int(input('Qual o número do CPTS?0 para não tem. '))
if dados['cpts'] != 0:
    dados['contrato'] = int(input('Qual o ano de contratação? '))
    dados['salario'] = int(input('Qual seu salário? '))
    if dados['sexo'] == 'M':
        anoaposentadoria = dados['contrato'] + 35
        dados['aposentadoria'] = idade + (anoaposentadoria - date.today().year)
    elif dados['sexo'] == 'F':
        anoaposentadoria = dados['contrato'] + 30
        dados['aposentadoria'] = idade + (anoaposentadoria - date.today().year)
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')



