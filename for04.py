n = int(input('Digite um número: '))
if n == 1:
    print('Esse número não é primo')
elif  n ==2 or n==3 or n==5 or n==7 or n%2!=0 and n%3!=0 and n%7!=0 and n%5!=0:

    print('Esse número é primo')
else:
    print('Esse número não é primo')

"""tot = 0
n = int(input('Digite um número: '))
for i in range(1, n + 1):
    if n % i == 0:
            print(i)
            tot += 1
if tot == 2:
        print('número primo')
else:
        print('número composto')"""