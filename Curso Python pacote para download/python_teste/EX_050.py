#LEIA 6 NUMEROS INTEIROS
#MOSTRE APENAS A SOMA DOS QUE SAO PARES E SE FOR IMPAR, DESCONSIDERE
s = 0
cont = 0
for c in range (1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num %2 == 0:
        s += num
        cont += 1
print('A soma dos valores pares eh {} e o total de numeros somados foi {}'.format(s, cont))