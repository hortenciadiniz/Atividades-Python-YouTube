#CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SAO MULTIPLOS DE TRES
#NO INTERVALO DE 1 ATE 500
s = 0 # a soma
cont = 0 # contador
for c in range(1,501):
    # teste pra saber se eh impar
    if c%2 == 1 and c%3 ==0 :
        cont = cont + 1 #contador soma 1
        s = s + c #a soma s faz a soma dos numeros
print('''A soma de todos os numeros impares entre 1 e 500 
que sao multiplos de 3 eh 
{}
Alem disso, o total de numeros que existem nessas condicoes eh 
{}'''.format(s,cont))
