#LEIA DOIS NUMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA:
#O PRIMEIRO VALOR EH MAIOR
#O SEGUNDO VALOR EH MAIOR
#NAO EXISTE VALOR MAIOR, OS DOIS SAO IGUAIS

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('ANALISANDO OS DOIS NUMEROS...')
#teste MAIOR
maior = n1

if n2>n1:
    maior = n2
    print('O maior valor eh o SEGUNDO que foi digitado, ou seja, {}'.format(maior))
elif n1 == n2:
    print('Nao existe valor maior, os dois sao IGUAIS, ou seja, {}'.format(n1))
elif n1>n2:
    maior = n1
    print('O maior valor eh o PRIMEIRO que foi digitado, ou seja, {}'.format(n1))