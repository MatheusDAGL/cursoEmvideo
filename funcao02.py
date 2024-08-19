def maior(*n):
    print(f'Os números são: {n},dando um total de {len(n)} números.')
    m = 0
    for i in range(0,len(n)):
        if i == 0:
            m = n[i]
        elif i > 0:
            if n[i] > m:
                m = n[i]
    print(f'Entre eles,o maior é {m}')



maior()
maior(2, 8, 7)
maior(6, 3, 1, 2)