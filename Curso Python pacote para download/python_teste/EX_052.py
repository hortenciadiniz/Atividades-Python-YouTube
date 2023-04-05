#LEIA UM NUMERO INTEIRO E DIGA SE ELE EH OU NAO UM NUMERO PRIMO
#NUM PRIMO EH AQUELE QUE EH DIVISIVEL APENAS POR UM E POR ELE MESMO
#TODO NUMERO EH DIVISIVEL POR 1, PORTANTO, NAO PRECISAMOS TESTAR ISSO

num = int(input('Digite um numero para testarmos se ele eh ou nao PRIMO: '))
cont = 0

for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')

print('\033[m\nO numero {} eh divisivel {} vezes!'.format(num,cont))
if cont == 2:
    print('O numero digitado eh PRIMO pois ele eh divisivel APENAS por 1 e por ele mesmo!')
else:
    print('O numero digitado NAO eh PRIMO!!!')