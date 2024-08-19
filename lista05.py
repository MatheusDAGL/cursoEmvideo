par = []
rap = []
x = str(input('Digite uma expressão com parênteses: '))
for i in range (0,len(x)):
    if '(' in x[i]:
        par.append('(')
    elif ')' in x[i]:
        rap.append(')')
if len(par) == len(rap):
    print('Expressão válida')
else:
    print('Expressão INVÁLIDA')