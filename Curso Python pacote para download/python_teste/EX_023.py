#LEIA UM NUMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DIGITOS SEPARADOS
#FORMA MATEMATICA
n = int(input('Digite um numero de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o numero {}... \nSua unidade eh {} \nSua dezena eh {} \nSua centena eh {} \nSeu milhar eh {}'.format(n,u,d,c,m))