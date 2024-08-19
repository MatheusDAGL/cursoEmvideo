import moeda
import dado

numero = str(input('Digite um número: '))
formato = dado.leiadinheiro(numero)
valor = float(formato)
moeda.resumo(valor)

with open('RegistroNomes', 'a') as arquivo:
    p = arquivo.write(str(input("Digita")))
    p = arquivo.write('\n')
