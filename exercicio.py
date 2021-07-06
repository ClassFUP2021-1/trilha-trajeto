import sys

gasto_indo = 0
gasto_voltando = 0
tamanho = int(sys.argv[1])

if tamanho >=2: 
    altura_inicial = int(sys.argv[2])
    for i in range(1,tamanho):
        novo = int(sys.argv[i+2])
        if altura_inicial - novo > 0:

            gasto_voltando = gasto_voltando
        elif (novo - altura_inicial) > 0:

            gasto_indo = gasto_indo + (novo - altura_inicial)
        altura_inicial = novo    

    print(gasto_voltando)
else:
    print('entrada invalida')
