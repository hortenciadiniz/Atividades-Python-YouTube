#LEIA O PRIMEIRO TERMO E A RAZAO DE UMA PA E NO FINAL MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSAO
#TEM QUE SABER A FORMULA PARA CALCULAR O DECIMO TERMO DA PA
n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
enesimo = n1 + (10-1) * r #FORMULA PARA CALCULAR O ENESIMO TERMO DE UMA PA

for c in range (n1, enesimo + r ,r):
    print('{}'.format(c), end=' ')