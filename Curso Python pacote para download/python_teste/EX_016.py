# import math
# n = float(input('Digite um numero real: '))
# n_parte_int = math.trunc(n)
# print('A parte inteira de {} e o valor {}'.format(n, n_parte_int))

from math import trunc
n = float(input('Digite um numero real: '))
n_parte_int = trunc(n)
print('A parte inteira de {} e o valor {}'.format(n, n_parte_int))