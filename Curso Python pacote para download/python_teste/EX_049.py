n = int(input('Digite um numero inteiro para calcularmos a TABUADA: '))
cont = 0
print('A TABUADA do numero {} eh:'.format(n))
print('='*11)
for c in range(0,10):
    cont = cont + 1
    print('{} x {} = {}'.format(n , cont, n*cont))
print('='*11)